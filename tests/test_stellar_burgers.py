from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from locators import Locators
from urls import REGISTER_URL, LOGIN_URL
from data import VALID_USERNAME, VALID_PASSWORD, INVALID_PASSWORD, generate_email

class TestStellarBurgers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)  # Устанавливаем неявное ожидание

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_registration(self):
        self.driver.get(REGISTER_URL)

        # Успешная регистрация
        self.driver.find_element(By.CSS_SELECTOR, Locators.NAME_INPUT).send_keys("Тест")
        self.driver.find_element(By.CSS_SELECTOR, Locators.EMAIL_INPUT).send_keys(generate_email(VALID_USERNAME))
        self.driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_BUTTON).click()

        WebDriverWait(self.driver, 10).until(EC.title_contains("Личный кабинет"))
        self.assertIn("Личный кабинет", self.driver.title)

    def test_registration_invalid_password(self):
        self.driver.get(REGISTER_URL)

        self.driver.find_element(By.CSS_SELECTOR, Locators.NAME_INPUT).send_keys("Тест")
        self.driver.find_element(By.CSS_SELECTOR, Locators.EMAIL_INPUT).send_keys(generate_email(VALID_USERNAME))
        self.driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.ERROR_MESSAGE))
        ).text
        self.assertIn("Пароль должен содержать как минимум 6 символов", error_message)

    def test_login(self):
        self.driver.get(LOGIN_URL)

        # Вход через кнопку "Войти в аккаунт"
        self.driver.find_element(By.CSS_SELECTOR, Locators.EMAIL_INPUT).send_keys(generate_email(VALID_USERNAME))
        self.driver.find_element(By.CSS_SELECTOR, Locators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_BUTTON).click()

        WebDriverWait(self.driver, 10).until(EC.title_contains("Личный кабинет"))
        self.assertIn("Личный кабинет", self.driver.title)

    def test_logout(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.CSS_SELECTOR, Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(By.CSS_SELECTOR, Locators.LOGOUT_BUTTON).click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.LOGIN_BUTTON)))
        self.assertIn("Войти в аккаунт", self.driver.page_source)

    def test_constructor_navigation_buns(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.CSS_SELECTOR, Locators.CONSTRUCTOR_LINK).click()
        self.driver.find_element(By.CSS_SELECTOR, Locators.BUNS_TAB).click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("buns"))
        self.assertEqual(self.driver.current_url, f"{BASE_URL}/constructor#buns")  # Проверка URL

    def test_constructor_navigation_sauces(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.CSS_SELECTOR, Locators.CONSTRUCTOR_LINK).click()
        self.driver.find_element(By.CSS_SELECTOR, Locators.SAUCES_TAB).click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("sauces"))
        self.assertEqual(self.driver.current_url, f"{BASE_URL}/constructor#sauces")  # Проверка URL

    def test_constructor_navigation_toppings(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(By.CSS_SELECTOR, Locators.CONSTRUCTOR_LINK).click()
        self.driver.find_element(By.CSS_SELECTOR, Locators.TOPPINGS_TAB).click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("toppings"))
        self.assertEqual(self.driver.current_url, f"{BASE_URL}/constructor#toppings")  # Проверка URL

if __name__ == "__main__":
    unittest.main()
