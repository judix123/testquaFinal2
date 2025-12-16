from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    # 🔥 ALL possible error locators
    ERROR_ALERT = (By.CSS_SELECTOR, ".oxd-alert.oxd-alert--error")
    FIELD_ERROR = (By.CSS_SELECTOR, ".oxd-input-field-error-message")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 6)

    def open(self):
        self.driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT)).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_error_visible(self):
        """
        Handles:
        - Invalid credentials
        - Empty fields
        - Delayed error rendering
        """
        try:
            WebDriverWait(self.driver, 5).until(
                EC.any_of(
                    EC.visibility_of_element_located(self.ERROR_ALERT),
                    EC.visibility_of_element_located(self.FIELD_ERROR),
                )
            )
            return True
        except TimeoutException:
            return False
