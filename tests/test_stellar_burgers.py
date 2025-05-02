import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import REGISTER_URL, LOGIN_URL
from data import VALID_USERNAME, VALID_PASSWORD, INVALID_PASSWORD, generate_email


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Устанавливаем неявное ожидание
    yield driver
    driver.quit()


def test_registration(driver):
    driver.get(REGISTER_URL)

    # Успешная регистрация
    driver.find_element(By.CSS_SELECTOR, Locators.NAME_INPUT).send_keys("Тест")
    driver.find_element(By.CSS_SELECTOR, Locators.EMAIL_INPUT).send_keys(generate_email(VALID_USERNAME))
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.title_contains("Личный кабинет"))
    assert "Личный кабинет" in driver.title


def test_registration_invalid_password(driver):
    driver.get(REGISTER_URL)

    driver.find_element(By.CSS_SELECTOR, Locators.NAME_INPUT).send_keys("Тест")
    driver.find_element(By.CSS_SELECTOR, Locators.EMAIL_INPUT).send_keys(generate_email(VALID_USERNAME))
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_BUTTON).click()

    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.ERROR_MESSAGE))
    ).text
    assert "Пароль должен содержать как минимум 6 символов" in error_message


def test_login(driver):
    driver.get(LOGIN_URL)

    # Вход через кнопку "Войти в аккаунт"
    driver.find_element(By.CSS_SELECTOR, Locators.EMAIL_INPUT).send_keys(generate_email(VALID_USERNAME))
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.title_contains("Личный кабинет"))
    assert "Личный кабинет" in driver.title


def test_logout(driver):
    driver.get(REGISTER_URL)
    driver.find_element(By.CSS_SELECTOR, Locators.NAME_INPUT).send_keys("Тест")
    driver.find_element(By.CSS_SELECTOR, Locators.EMAIL_INPUT).send_keys(generate_email(VALID_USERNAME))
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_BUTTON).click()

    driver.find_element(By.CSS_SELECTOR, Locators.ACCOUNT_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, Locators.LOGOUT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.LOGIN_BUTTON)))
    assert "Войти в аккаунт" in driver.page_source


def test_constructor_navigation_buns(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.CSS_SELECTOR, Locators.CONSTRUCTOR_LINK).click()
    driver.find_element(By.CSS_SELECTOR, Locators.BUNS_TAB).click()

    # Проверяем, что раздел "Булки" выделен и отображается текст "Булки"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    h2_text = driver.find_element(By.TAG_NAME, "h2").text
    assert "Булки" in h2_text
    assert "tab_index_selected" in driver.find_element(By.CSS_SELECTOR, Locators.BUNS_TAB).get_attribute(
        "class")  # Пример класса


def test_constructor_navigation_sauces(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.CSS_SELECTOR, Locators.CONSTRUCTOR_LINK).click()
    driver.find_element(By.CSS_SELECTOR, Locators.SAUCES_TAB).click()

    # Проверяем, что раздел "Соусы" выделен и отображается текст "Соусы"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    h2_text = driver.find_element(By.TAG_NAME, "h2").text
    assert "Соусы" in h2_text
    assert "tab_index_selected" in driver.find_element(By.CSS_SELECTOR, Locators.SAUCES_TAB).get_attribute(
        "class")  # Пример класса


def test_constructor_navigation_toppings(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.CSS_SELECTOR, Locators.CONSTRUCTOR_LINK).click()
    driver.find_element(By.CSS_SELECTOR, Locators.TOPPINGS_TAB).click()

    # Проверяем, что раздел "Начинки" выделен и отображается текст "Начинки"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    h2_text = driver.find_element(By.TAG_NAME, "h2").text
    assert "Начинки" in h2_text
    assert "tab_index_selected" in driver.find_element(By.CSS_SELECTOR, Locators.TOPPINGS_TAB).get_attribute(
        "class")  # Пример класса
