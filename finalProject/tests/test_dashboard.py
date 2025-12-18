import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard


# ---------- FIXTURE ----------
@pytest.fixture(scope="function")
def logged_in_dashboard(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("Admin", "admin123")

    dashboard = Dashboard(driver)
    WebDriverWait(driver, 10).until(lambda d: dashboard.is_loaded())
    return dashboard


@pytest.mark.skipif(Config.LANG != "en", reason="Only valid for English UI texts")
class TestDashboard:

    # ---------- DASHBOARD LOAD ----------
    def test_dashboard_loads(self, logged_in_dashboard):
        assert logged_in_dashboard.is_loaded()

    # ---------- WIDGET VISIBILITY ----------
    def test_time_at_work_widget_visible(self, logged_in_dashboard):
        assert logged_in_dashboard.is_time_at_work_visible()

    def test_my_actions_widget_visible(self, logged_in_dashboard):
        assert logged_in_dashboard.is_my_actions_visible()

    def test_quick_launch_widget_visible(self, logged_in_dashboard):
        assert logged_in_dashboard.is_quick_launch_visible()

    def test_buzz_widget_visible(self, logged_in_dashboard):
        assert logged_in_dashboard.is_buzz_widget_visible()

    def test_leave_today_widget_visible(self, logged_in_dashboard):
        assert logged_in_dashboard.is_leave_today_widget_visible()

    def test_employee_distribution_charts_visible(self, logged_in_dashboard):
        assert logged_in_dashboard.is_employee_distribution_charts_visible()

    # ---------- QUICK LAUNCH ----------
    def test_quick_launch_assign_leave(self, logged_in_dashboard, driver):
        logged_in_dashboard.click_assign_leave()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/leave/assignLeave")
        )
        assert "/leave/assignLeave" in driver.current_url

    def test_quick_launch_leave_list(self, logged_in_dashboard, driver):
        logged_in_dashboard.click_leave_list()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/leave/viewLeaveList")
        )
        assert "/leave/viewLeaveList" in driver.current_url

    def test_quick_launch_apply_leave(self, logged_in_dashboard, driver):
        logged_in_dashboard.click_apply_leave()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/leave/applyLeave")
        )
        assert "/leave/applyLeave" in driver.current_url

    # ---------- MY ACTIONS ----------
    def test_pending_self_review(self, logged_in_dashboard, driver):
        logged_in_dashboard.click_pending_review()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/performance/myPerformanceReview")
        )
        assert "/performance/myPerformanceReview" in driver.current_url

    def test_candidate_interview(self, logged_in_dashboard, driver):
        logged_in_dashboard.click_candidate_interview()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/recruitment/viewCandidates")
        )
        assert "/recruitment/viewCandidates" in driver.current_url

    # ---------- BUZZ ----------
    def test_buzz_post_exists(self, logged_in_dashboard):
        assert logged_in_dashboard.has_buzz_post()

    # ---------- ON LEAVE CONFIG ----------
    def test_on_leave_configuration_modal(self, logged_in_dashboard, driver):
        logged_in_dashboard.open_on_leave_settings()

        modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(normalize-space(),'Configurations')]")
            )
        )
        assert modal.is_displayed()

    # ---------- PUNCH IN ----------
    def test_punch_in(self, logged_in_dashboard, driver):
        logged_in_dashboard.punch_in()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/attendance/punchIn")
        )
        assert "/attendance/punchIn" in driver.current_url
