
import os
import re
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# ==========================================
# SCREENSHOT DIRECTORY
# ==========================================

ARTIFACTS_DIR = Path(__file__).resolve().parent / "artifacts"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


# ==========================================
# SELENIUM DRIVER FIXTURE
# ==========================================

@pytest.fixture
def driver(request):

    options = Options()

    # Headless mode
    if os.getenv("HEADLESS") == "1":
        options.add_argument("--headless=new")

    # Browser configuration
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    # Disable Chrome password warning
    options.add_argument("--disable-features=PasswordLeakDetection")

    options.add_experimental_option(
        "prefs",
        {
            "profile.password_manager_leak_detection": False,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    # Initialize Chrome
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(0)

    browser.get("https://www.saucedemo.com/")

    yield browser

    # ======================================
    # AUTOMATIC SCREENSHOT AFTER TEST
    # ======================================

    report = getattr(request.node, "rep_call", None)

    if report is not None:

        # Determine test status
        if report.passed:
            status = "PASSED"
        else:
            status = "FAILED"

        # Generate safe filename
        test_name = re.sub(
            r"[^a-zA-Z0-9_-]",
            "_",
            request.node.name
        )

        # Screenshot filename
        screenshot_path = (
            ARTIFACTS_DIR /
            f"{test_name}_{status}.png"
        )

        # Save screenshot before closing browser
        try:
            browser.save_screenshot(str(screenshot_path))

            print(
                f"\n[{status}] Screenshot saved: "
                f"{screenshot_path}"
            )

        except Exception as e:
            print(f"\nScreenshot failed: {e}")

    # Close browser
    browser.quit()


# ==========================================
# PYTEST HOOK
# ==========================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)
