
from binascii import Error

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
import requests
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

def test_click_item(test_url, target_url, itemname):
    try:
        # 1. Open the target webpage
        driver.get(test_url)
        driver.maximize_window()

        # 2. Locate the link (by its visible text or XPath)
        # Strategy A: Using the exact text displayed on the page
        link_element = driver.find_element(By.LINK_TEXT, itemname)
        
        # Strategy B: Alternative using XPath if the text is dynamic
        # link_element = driver.find_element(By.XPATH, "//a[@id='myLink']")

        # 3. Click the link
        link_element.click()
        time.sleep(2) # Brief pause to allow the page to load

        # 4. Verify navigation by checking the current URL
        expected_url = target_url  # Assuming itemname is the expected URL after clicking
        assert driver.current_url == expected_url, f"Expected {expected_url} but got {driver.current_url}"
        print(f"Link test for {itemname} at URL {target_url} passed successfully!")
        print(f"Attempting the next test for the next item in the array...")

        test_results = "PASS"

    except Error as err:
        print(f"An error occurred trying to perform the test:  {err}")
        test_results = "FAIL"
    return test_results


# NEW FUNCTION: Test unavailable page and take screenshot
def test_undefined_url(url):
    try:
        # Open the unavailable page
        driver.get(url)
        driver.maximize_window()

        # Wait until page loads
        WebDriverWait(driver, 15).until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

        # Create screenshots folder
        os.makedirs("screenshots", exist_ok=True)

        # Take screenshot after page loads
        screenshot_path = "screenshots/undefined_page.png"
        screenshot_saved = driver.save_screenshot(screenshot_path)

        if screenshot_saved:
            print(
                f"Screenshot saved: {os.path.abspath(screenshot_path)}"
            )
        else:
            print("FAIL: Screenshot could not be saved")

        # Check HTTP response status
        response = requests.get(url, timeout=15)

        if response.status_code == 404:
            print("PASS: Undefined URL returned HTTP 404")
            return "PASS"

        else:
            print(
                f"FAIL: Expected 404, got {response.status_code}"
            )
            return "FAIL"

    except Exception as err:
        print(f"An error occurred: {err}")
        return "FAIL"


def close_browser():
    driver.quit()
