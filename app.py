
from includes import functions
from includes import constants
from datetime import datetime
import logging
import platform
import time
import os

# Create the logs directory inside the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S_%f")

log_filename = os.path.join(
    LOG_DIR,
    f"LOG_FILE_{timestamp}.txt"
)

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True
)

text_url_array = {
    constants.HOME_TEXT: constants.HOME_URL,
    constants.ABOUT_TEXT: constants.ABOUT_URL,
    constants.SERVICES_TEXT: constants.SERVICES_URL,
    constants.PORTFOLIO_TEXT: constants.PORTFOLIO_URL,
    constants.CONTACT_TEXT: constants.CONTACT_URL
}

total_tests = 0
passed_tests = 0
failed_tests = 0

run_start = time.perf_counter()

try:
    browser_info = functions.driver.capabilities
    browser_name = browser_info.get("browserName", "Unknown")
    browser_version = browser_info.get("browserVersion", "Unknown")

    logging.info(
        f"RUN START | Website: {constants.TEST_URL} | "
        f"Browser: {browser_name} {browser_version} | "
        f"OS: {platform.system()} {platform.release()}"
    )

    for index, (test_name, test_url) in enumerate(
        text_url_array.items(), start=1
    ):
        test_id = f"TC-{index:02d}"
        start_time = time.perf_counter()

        test_results = functions.test_click_item(
            constants.TEST_URL, test_url, test_name
        )

        duration = time.perf_counter() - start_time
        total_tests += 1

        if test_results == "PASS":
            passed_tests += 1
            log_level = logging.INFO
        else:
            failed_tests += 1
            log_level = logging.ERROR

        logging.log(
            log_level,
            f"{test_id} | Click {test_name} | "
            f"Expected: {test_url} | "
            f"Actual: {functions.last_actual} | "
            f"Status: {test_results} | "
            f"Duration: {duration:.2f} s | "
            f"Page URL: {functions.driver.current_url} | "
            f"Error: {functions.last_error or 'None'}"
        )

        if duration > 10:
            logging.warning(
                f"{test_id} | Slow test execution | "
                f"Duration: {duration:.2f} s"
            )

        print(f"TC-{index:02d}: {test_name} - {test_results}")

    # Undefined URL test runs only once
    print("\nStarting undefined URL test...")

    start_time = time.perf_counter()

    undefined_result = functions.test_undefined_url(
        constants.UNDEFINED_URL
    )

    duration = time.perf_counter() - start_time
    total_tests += 1

    if undefined_result == "PASS":
        passed_tests += 1
        log_level = logging.INFO
    else:
        failed_tests += 1
        log_level = logging.ERROR

    screenshot_path = os.path.abspath(
        "screenshots/undefined_page.png"
    )

    logging.log(
        log_level,
        f"TC-06 | Undefined URL Test | "
        f"Expected: HTTP 404 | "
        f"Actual: {functions.last_actual} | "
        f"Status: {undefined_result} | "
        f"Duration: {duration:.2f} s | "
        f"Page URL: {functions.driver.current_url} | "
        f"Screenshot: {screenshot_path if os.path.isfile(screenshot_path) else 'Not available'} | "
        f"Error: {functions.last_error or 'None'}"
    )

    if duration > 10:
        logging.warning(
            f"TC-06 | Slow test execution | "
            f"Duration: {duration:.2f} s"
        )

    print(f"TC-06: Undefined URL - {undefined_result}")

finally:
    total_duration = time.perf_counter() - run_start

    logging.info(
        f"RUN END | Total: {total_tests} | "
        f"Passed: {passed_tests} | "
        f"Failed: {failed_tests} | "
        f"Duration: {total_duration:.2f} s"
    )

    print("\nTEST EXECUTION SUMMARY")
    print(f"Total tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"Duration: {total_duration:.2f} seconds")
    print(f"Log file: {log_filename}")

    functions.close_browser()
