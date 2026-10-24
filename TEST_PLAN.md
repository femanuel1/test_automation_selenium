# Test Plan

## 1. Objective
This project validates the core navigation behavior of the portfolio website and checks that an undefined URL returns the expected HTTP 404 response.

## 2. Scope
The automated test covers:
- Home page navigation
- About page navigation
- Services page navigation
- Portfolio page navigation
- Contact page navigation
- Undefined URL handling

## 3. Test Environment
- Operating System: macOS
- Browser: Google Chrome
- Automation Tool: Selenium WebDriver
- Programming Language: Python 3
- Libraries: selenium, requests
- Portifolio Under Test: https://femanuel1.github.io/emmanuelmfitumukiza/

## 4. Test Data
The following navigation targets are validated:

| Test ID | Page Label | Expected URL |
| --- | --- | --- |
| TC-01 | HOME | https://femanuel1.github.io/emmanuelmfitumukiza/index.html |
| TC-02 | ABOUT ME | https://femanuel1.github.io/emmanuelmfitumukiza/about.html |
| TC-03 | SERVICES | https://femanuel1.github.io/emmanuelmfitumukiza/services.html |
| TC-04 | PROJECTS | https://femanuel1.github.io/emmanuelmfitumukiza/portfolio.html |
| TC-05 | CONTACT | https://femanuel1.github.io/emmanuelmfitumukiza/contact.html |
| TC-06 | Undefined URL | HTTP 404 |

## 5. Test Cases

### TC-01: Verify HOME navigation
- Open the website
- Click the HOME link
- Confirm the browser reaches the home page URL
- Expected Result: PASS

### TC-02: Verify ABOUT ME navigation
- Open the website
- Click the ABOUT ME link
- Confirm the browser reaches the about page URL
- Expected Result: PASS

### TC-03: Verify SERVICES navigation
- Open the website
- Click the SERVICES link
- Confirm the browser reaches the services page URL
- Expected Result: PASS

### TC-04: Verify PROJECTS navigation
- Open the website
- Click the PROJECTS link
- Confirm the browser reaches the portfolio page URL
- Expected Result: PASS

### TC-05: Verify CONTACT navigation
- Open the website
- Click the CONTACT link
- Confirm the browser reaches the contact page URL
- Expected Result: PASS

### TC-06: Verify undefined URL returns HTTP 404
- Request a non-existing page URL
- Confirm the page responds with HTTP status 404
- Save a screenshot of the result page
- Expected Result: PASS

## 6. Entry Criteria
- The website is reachable online
- Chrome is installed and available on the machine
- Python dependencies are installed
- The project files are available in the repository

## 7. Exit Criteria
- All six tests complete without failure
- Logs are generated successfully
- Screenshot is saved for the undefined page test
- Execution summary shows 0 failed tests

## 8. Pass/Fail Rules
A test passes when:
- the expected page URL is reached for link navigation tests
- the undefined page returns HTTP 404
- no unexpected exception occurs during execution

A test fails when:
- the page URL does not match the expected target
- the undefined page does not return HTTP 404
- the browser or request raises an exception during the test

## 9. Evidence
The project stores execution evidence in the log files under the logs directory and the screenshot under the screenshots directory.

Examples:
- logs/LOG_FILE_20261024_171201_795326.txt
- screenshots/undefined_page.png

## 10. Summary
The current implementation validates the navigation flow and negative test case successfully. The final execution summary recorded 6 total tests, 6 passed, and 0 failed.
