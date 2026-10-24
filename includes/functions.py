
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
import requests
import time

driver = webdriver.Chrome()

last_error = ""
last_actual = ""


def test_click_item(test_url, target_url, itemname):
    global last_error, last_actual

    last_error = ""
    last_actual = ""

    try:
        driver.get(test_url)
        driver.maximize_window()

        link_element = WebDriverWait(driver, 15).until(
            lambda d: d.find_element(By.LINK_TEXT, itemname)
        )

        link_element.click()

        WebDriverWait(driver, 15).until(
            lambda d: d.current_url == target_url
        )

        expected_url = target_url
        last_actual = driver.current_url

        assert driver.current_url == expected_url, (
            f"Expected {expected_url} but got {driver.current_url}"
        )

        print(
            f"Link test for {itemname} at URL "
            f"{target_url} passed successfully!"
        )
        print(
            "Attempting the next test for the next item in the array..."
        )

        test_results = "PASS"

    except Exception as err:
        last_actual = driver.current_url
        last_error = str(err)

        print(
            f"An error occurred trying to perform the test: {err}"
        )
        test_results = "FAIL"

    return test_results


def test_undefined_url(url):
    global last_error, last_actual

    last_error = ""
    last_actual = ""

    try:
        driver.get(url)
        driver.maximize_window()

        WebDriverWait(driver, 15).until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        # Save screenshots inside the project directory
        BASE_DIR = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        SCREENSHOT_DIR = os.path.join(
            BASE_DIR, "screenshots"
        )
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)

        screenshot_path = os.path.join(
            SCREENSHOT_DIR, "undefined_page.png"
        )

        screenshot_saved = driver.save_screenshot(
            screenshot_path
        )

        if screenshot_saved:
            print(
                f"Screenshot saved: {os.path.abspath(screenshot_path)}"
            )
        else:
            print("WARNING: Screenshot could not be saved")

        response = requests.get(url, timeout=15)
        last_actual = f"HTTP {response.status_code}"

        if response.status_code == 404:
            print("PASS: Undefined URL returned HTTP 404")
            return "PASS"
        else:
            last_error = (
                f"Expected HTTP 404, got HTTP {response.status_code}"
            )
            print(f"FAIL: {last_error}")
            return "FAIL"

    except Exception as err:
        last_error = str(err)
        last_actual = last_actual or "Test could not complete"

        print(f"An error occurred: {err}")
        return "FAIL"


def close_browser():
    driver.quit()
