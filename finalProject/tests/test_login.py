import pytest
from selenium.webdriver.common.by import By
from config import Config
from pages.login_page import LoginPage


@pytest.mark.skipif(Config.LANG != "en", reason="Only valid for English UI")
class TestLogin:

    def test_login_page_loads(self, driver):
        login_page = LoginPage(driver)
        login_page.open()

        assert driver.find_element(*LoginPage.USERNAME_INPUT)
        assert driver.find_element(*LoginPage.PASSWORD_INPUT)
        assert driver.find_element(*LoginPage.LOGIN_BUTTON)

    @pytest.mark.parametrize("username,password", [
        ("InvalidUser", "WrongPass123"),
        ("InvalidUser", "admin123"),
        ("Admin", ""),
        ("", ""),
        ("Admin1", "admin123"),
        ("Admin", "admin456"),
    ])
    def test_login_with_invalid_credentials(self, driver, username, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)

        assert login_page.is_error_visible()

    def test_link_text(self, driver):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        link = driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc")
        link.click()

        driver.switch_to.window(driver.window_handles[-1])
        assert "orangehrm.com" in driver.current_url
