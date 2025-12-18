from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dashboard:
    URL_PART = "/dashboard"

    # Header
    DASHBOARD_HEADER = (By.XPATH, "//h6[normalize-space()='Dashboard']")

    # Widgets
    TIME_AT_WORK_WIDGET = (By.XPATH, "//p[normalize-space()='Time at Work']")
    MY_ACTIONS_WIDGET = (By.XPATH, "//p[normalize-space()='My Actions']")
    QUICK_LAUNCH_WIDGET = (By.XPATH, "//p[normalize-space()='Quick Launch']")
    BUZZ_WIDGET = (By.XPATH, "//p[normalize-space()='Buzz Latest Posts']")
    LEAVE_TODAY_WIDGET = (By.XPATH, "//p[normalize-space()='Employees on Leave Today']")

    # Quick Launch buttons
    ASSIGN_LEAVE_BTN = (By.XPATH, "//button[@title='Assign Leave']")
    LEAVE_LIST_BTN = (By.XPATH, "//button[@title='Leave List']")
    APPLY_LEAVE_BTN = (By.XPATH, "//button[@title='Apply Leave']")
    MY_LEAVE_BTN = (By.XPATH, "//button[@title='My Leave']")
    MY_TIMESHEET_BTN = (By.XPATH, "//button[@title='My Timesheet']")

    # My Actions
    PENDING_SELF_REVIEW = (By.XPATH, "//p[contains(text(),'Pending Self Review')]")
    CANDIDATE_TO_INTERVIEW = (By.XPATH, "//p[contains(text(),'Candidates to Interview')]")

    # Charts
    EMPLOYEE_SUB_UNIT_CHART = (By.XPATH, "//p[contains(text(),'Sub Unit')]")
    EMPLOYEE_LOCATION_CHART = (By.XPATH, "//p[contains(text(),'Location')]")

    # Buzz
    BUZZ_POST = (By.XPATH, "//div[contains(@class,'orangehrm-buzz-post')]")

    # On Leave
    ON_LEAVE_SETTING = (By.XPATH, "//p[text()='Employees on Leave Today']/ancestor::div[contains(@class,'header')]//i")

    # Punch In
    PUNCH_IN = (By.XPATH, "//button[contains(.,'Punch In')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ---------- Page Load ----------
    def is_loaded(self):
        self.wait.until(EC.url_contains(self.URL_PART))
        return self.wait.until(
            EC.visibility_of_element_located(self.DASHBOARD_HEADER)
        ).is_displayed()

    # ---------- Widget Visibility ----------
    def _is_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    def is_time_at_work_visible(self):
        return self._is_visible(self.TIME_AT_WORK_WIDGET)

    def is_my_actions_visible(self):
        return self._is_visible(self.MY_ACTIONS_WIDGET)

    def is_quick_launch_visible(self):
        return self._is_visible(self.QUICK_LAUNCH_WIDGET)

    def is_buzz_widget_visible(self):
        return self._is_visible(self.BUZZ_WIDGET)

    def is_leave_today_widget_visible(self):
        return self._is_visible(self.LEAVE_TODAY_WIDGET)

    def is_employee_distribution_charts_visible(self):
        return (
            self._is_visible(self.EMPLOYEE_SUB_UNIT_CHART)
            and self._is_visible(self.EMPLOYEE_LOCATION_CHART)
        )

    # ---------- Quick Launch ----------
    def click_assign_leave(self):
        self.wait.until(EC.element_to_be_clickable(self.ASSIGN_LEAVE_BTN)).click()

    def click_leave_list(self):
        self.wait.until(EC.element_to_be_clickable(self.LEAVE_LIST_BTN)).click()

    def click_apply_leave(self):
        self.wait.until(EC.element_to_be_clickable(self.APPLY_LEAVE_BTN)).click()

    # ---------- My Actions ----------
    def click_pending_review(self):
        self.wait.until(EC.element_to_be_clickable(self.PENDING_SELF_REVIEW)).click()

    def click_candidate_interview(self):
        self.wait.until(EC.element_to_be_clickable(self.CANDIDATE_TO_INTERVIEW)).click()

    # ---------- Buzz ----------
    def has_buzz_post(self):
        return self.wait.until(
            EC.presence_of_element_located(self.BUZZ_POST)
        ).is_displayed()

    # ---------- Charts ----------
    def get_subunit_panel(self):
        return self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_SUB_UNIT_CHART))

    def get_location_panel(self):
        return self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_LOCATION_CHART))

    # ---------- On Leave ----------
    def open_on_leave_settings(self):
        self.wait.until(EC.element_to_be_clickable(self.ON_LEAVE_SETTING)).click()

    # ---------- Punch In ----------
    def punch_in(self):
        self.wait.until(EC.element_to_be_clickable(self.PUNCH_IN)).click()
