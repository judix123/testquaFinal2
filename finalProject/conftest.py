# conftest.py
import os
from datetime import datetime

import pytest
# import pytest_html
from selenium import webdriver


#global fixture configuration for testing
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    if not getattr(config.option, "htmlpath", None):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        config.option.htmlpath = f"reports/orangehrm_report_{timestamp}.html"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            screenshot = driver.get_screenshot_as_png()
            report.extra = getattr(report, "extra", [])
            # report.extra.append(pytest_html.extras.png(screenshot))
