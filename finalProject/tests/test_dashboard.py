# tests/test_dashboard.py
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard

@pytest.mark.skipif(Config.LANG != "en", reason="Only valid for English UI texts")
class TestDashboard:


    #dashboard confirms after loading
    def test_dashboard_loads_after_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_loaded()
    #testing if all widgets are presented
    def test_time_at_work_widget_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_time_at_work_visible()

    def test_my_actions_widget_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_my_actions_visible()

    def test_quick_launch_widget_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_quick_launch_visible()

    def test_buzz_widget_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_buzz_widget_visible()

    def test_leave_today_widget_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_leave_today_widget_visible()

    def test_employee_distribution_charts_visible(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_employee_distribution_charts_visible()

#this part test if the widgets of quick launch works and leads to a right directory or page
    def test_quick_launch_assign_leave(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_assign_leave()

        assert "/leave/assignLeave" in driver.current_url

    def test_quick_launch_leave_list(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_leave_list()

        assert "/leave/viewLeaveList" in driver.current_url

    def test_quick_launch_apply_leave(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_apply_leave()

        assert "/leave/applyLeave" in driver.current_url

    #test script for testing My Actions form
    def test_my_actions_loads_in_dashboard(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_my_actions_loaded()
        time.sleep(5)


    def test_pending_self(self,driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin","admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_pending_review()
        time.sleep(4)
        assert "/performance/myPerformanceReview" in driver.current_url
        time.sleep(5)

    def test_review_candidate(self,driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin","admin123")

        dashboard_page = Dashboard(driver)
        dashboard_page.click_candidate_interview()
        time.sleep(4)
        assert "/recruitment/viewCandidates?statusId=4" in driver.current_url
        time.sleep(5)

    def test_my_buzz_post_dashboard(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.is_buzz_loaded()
        time.sleep(4)

    def test_user_post(self,driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.buzz_post()
        time.sleep(4)

    #this is for Subunit chart testing
    def test_sub_unit(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.subunit_panel()
        time.sleep(4)

    def test_subunit_toggle(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard = Dashboard(driver)
        panel = dashboard.get_subunit_panel()

        legend_items = panel.find_elements(By.XPATH, './/ul/li')

        for item in legend_items:
            item.click()

            WebDriverWait(driver, 2).until(
                lambda d: d.execute_script(
                    'return document.querySelectorAll("svg path[opacity=\\"0\\"]").length > 0'
                )
            )

        visible_paths = driver.find_elements(
            By.XPATH,
            '//*[name()="svg"]//*[name()="path" and (@opacity and @opacity!="0")]'
        )

        assert len(visible_paths) == 0

    #this is for location chat testing
    def test_loc_unit(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard_page = Dashboard(driver)
        assert dashboard_page.location_panel()
        time.sleep(4)

    def test_location_toggle(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("Admin", "admin123")

        dashboard = Dashboard(driver)
        panel = dashboard.get_location_panel()

        legend_items = panel.find_elements(By.XPATH, './/ul/li')

        for item in legend_items:
            item.click()
            time.sleep(0.3)

        visible_paths = driver.find_elements(
            By.XPATH,
            '//*[name()="svg"]//*[name()="path" and @opacity!="0"]'
        )

        assert len(visible_paths) == 0, f"Expected 0 visible paths, but found {len(visible_paths)}"
    #this is for On leave section

    def test_on_leave_icon(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("Admin", 'admin123')

        dashboard = Dashboard(driver)
        gear_icon = dashboard.icon_test()

        gear_icon.click()
        time.sleep(2)

        wait = WebDriverWait(driver,15)

    def test_on_leave_configuration(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("Admin", "admin123")

        dashboard = Dashboard(driver)
        wait = WebDriverWait(driver, 10)

        gear_icon = dashboard.icon_test()
        gear_icon.click()

        config_modal = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(normalize-space(), 'Configurations')]")
            )
        )

        assert config_modal.is_displayed(), "Config modal should open"

    #testinf punch in button
    def test_punch_in(self,driver):
        login = LoginPage(driver)
        login.open()
        login.login('Admin','admin123')

        dashboard = Dashboard(driver)
        dashboard.punch_in().click()

        assert "/attendance/punchIn" in driver.current_url
        time.sleep(2)