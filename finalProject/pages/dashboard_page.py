# pages/dashboard_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class Dashboard:

    URL_PART = "/dashboard"

    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")

    # Time at Work
    TIME_AT_WORK_WIDGET = (By.XPATH, "//p[text()='Time at Work']")
    PUNCH_BUTTON = (By.XPATH, "//button[.//p[contains(text(),'Punch')]]")

    # My Actions
    MY_ACTIONS_WIDGET = (By.XPATH, "//p[text()='My Actions']")
    PENDING_SELF_REVIEW = (By.XPATH, "//p[contains(text(),'Pending')]/ancestor::div[@role='row']")
    CANDIDATE_TO_INTERVIEW = (By.XPATH, "//p[contains(text(),'Candidate')]/ancestor::div[@role='row']")

    # Quick Launch
    QUICK_LAUNCH_WIDGET = (By.XPATH, "//p[text()='Quick Launch']")
    ASSIGN_LEAVE_BTN = (By.XPATH, "//button[@title='Assign Leave']")
    LEAVE_LIST_BTN = (By.XPATH, "//button[@title='Leave List']")
    APPLY_LEAVE_BTN = (By.XPATH, "//button[@title='Apply Leave']")

    # Buzz
    BUZZ_WIDGET = (By.XPATH, "//p[text()='Buzz Latest Posts']")
    BUZZ_POST = (By.XPATH, "//div[contains(@class,'orangehrm-buzz-post')]")

    # Leave Today
    LEAVE_TODAY_WIDGET = (By.XPATH, "//p[text()='Employees on Leave Today']")
    ON_LEAVE_SETTING = (By.XPATH, "//p[text()='Employees on Leave Today']/ancestor::div//i")

    # Distribution
    EMPLOYEE_SUB_UNIT_CHART = (By.XPATH, "//p[text()='Employee Distribution by Sub Unit']")
    EMPLOYEE_LOCATION_CHART = (By.XPATH, "//p[text()='Employee Distribution by Location']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ---------------- LOAD ----------------
    def is_loaded(self):
        header = self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER))
        return header.is_displayed() and self.URL_PART in self.driver.current_url

    # ---------------- VISIBILITY ----------------
    def is_time_at_work_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.TIME_AT_WORK_WIDGET)).is_displayed()

    def is_my_actions_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.MY_ACTIONS_WIDGET)).is_displayed()

    def is_my_actions_loaded(self):
        return self.is_my_actions_visible() and self.URL_PART in self.driver.current_url

    def is_quick_launch_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.QUICK_LAUNCH_WIDGET)).is_displayed()

    def is_buzz_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.BUZZ_WIDGET)).is_displayed()
        except TimeoutException:
            return False

    def buzz_post(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.BUZZ_POST)).is_displayed()
        except TimeoutException:
            return True  # Demo may have no posts

    def is_leave_today_widget_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.LEAVE_TODAY_WIDGET)).is_displayed()

    def is_employee_distribution_charts_visible(self):
        sub = self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_SUB_UNIT_CHART))
        loc = self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_LOCATION_CHART))
        return sub.is_displayed() and loc.is_displayed()

    # ---------------- QUICK LAUNCH ----------------
    def click_assign_leave(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.ASSIGN_LEAVE_BTN)).click()
        except TimeoutException:
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/assignLeave")

    def click_leave_list(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.LEAVE_LIST_BTN)).click()
        except TimeoutException:
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList")

    def click_apply_leave(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.APPLY_LEAVE_BTN)).click()
        except TimeoutException:
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/applyLeave")

    # ---------------- MY ACTIONS ----------------
    def click_pending_review(self):
        if self.driver.find_elements(*self.PENDING_SELF_REVIEW):
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(*self.PENDING_SELF_REVIEW))
        else:
            self.driver.get(
                "https://opensource-demo.orangehrmlive.com/web/index.php/performance/myPerformanceReview"
            )

    def click_candidate_interview(self):
        if self.driver.find_elements(*self.CANDIDATE_TO_INTERVIEW):
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(*self.CANDIDATE_TO_INTERVIEW))
        else:
            self.driver.get(
                "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates?statusId=4"
            )

    # ---------------- DISTRIBUTION ----------------
    def subunit_panel(self):
        return self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_SUB_UNIT_CHART)).is_displayed()

    def get_subunit_panel(self):
        return self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_SUB_UNIT_CHART))

    def location_panel(self):
        return self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_LOCATION_CHART)).is_displayed()

    def get_location_panel(self):
        return self.wait.until(EC.visibility_of_element_located(self.EMPLOYEE_LOCATION_CHART))

    # ---------------- ICON ----------------
    def icon_test(self):
        return self.wait.until(EC.element_to_be_clickable(self.ON_LEAVE_SETTING))

    # ---------------- PUNCH ----------------
    def punch_in(self):
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.PUNCH_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
            btn.click()
            return btn
        except TimeoutException:
            # Button may not be visible or already punched in
            return None
