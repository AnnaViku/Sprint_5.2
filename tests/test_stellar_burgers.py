from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
import time


def generate_email(username):
    return f"{username}@example.com"


def test_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Успешная регистрация
    driver.find_element(By.CSS_SELECTOR, Locators.NAME_INPUT).send_keys("Тест")
    driver.find_element(By.CSS_SELECTOR, Locators.EMAIL_INPUT).send_keys(generate_email("testtestov1999"))
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_BUTTON).click()

    time.sleep(2)  # Ждем загрузки страницы
    assert "Личный кабинет" in driver.title  # Проверяем вход в личный кабинет

    driver.quit()


def test_registration_invalid_password():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Проверка на некорректный пароль
    driver.find_element(By.CSS_SELECTOR, Locators.NAME_INPUT).send_keys("Тест")
    driver.find_element(By.CSS_SELECTOR, Locators.EMAIL_INPUT).send_keys(generate_email("testtestov1999"))
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys("123")
    driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_BUTTON).click()

    time.sleep(2)  # Ждем сообщения об ошибке
    error_message = driver.find_element(By.CSS_SELECTOR, Locators.ERROR_MESSAGE).text
    assert "Пароль должен содержать как минимум 6 символов" in error_message

    driver.quit()


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(By.CSS_SELECTOR, Locators.EMAIL_INPUT).send_keys(generate_email("testtestov1999"))
    driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_BUTTON).click()

    time.sleep(2)  # Ждем загрузки страницы
    assert "Личный кабинет" in driver.title  # Проверяем вход в личный кабинет

    driver.quit()


def test_logout():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.CSS_SELECTOR, Locators.ACCOUNT_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, Locators.LOGOUT_BUTTON).click()

    time.sleep(2)  # Ждем завершения выхода
    assert "Войти в аккаунт" in driver.page_source  # Проверяем наличие кнопки "Войти"

    driver.quit()


def test_constructor_navigation():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.CSS_SELECTOR, Locators.CONSTRUCTOR_LINK).click()
    time.sleep(2)  # Ждем загрузки конструктора

    # Проверка навигации
    driver.find_element(By.CSS_SELECTOR, Locators.BUNS_TAB).click()
    assert "Булки" in driver.page_source  # Проверяем, что открылась вкладка "Булки"

    driver.find_element(By.CSS_SELECTOR, Locators.SAUCES_TAB).click()
    assert "Соусы" in driver.page_source  # Проверяем, что открылась вкладка "Соусы"

    driver.find_element(By.CSS_SELECTOR, Locators.TOPPINGS_TAB).click()
    assert "Начинки" in driver.page_source  # Проверяем, что открылась вкладка "Начинки"

    driver.quit()