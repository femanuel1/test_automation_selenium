
from includes import functions
from includes import constants
from datetime import datetime

#Create an array of the texts and URLs as well so that they are looped through in the test.
text_url_array = {
    constants.HOME_TEXT: constants.HOME_URL,
    constants.ABOUT_TEXT: constants.ABOUT_URL,
    constants.SERVICES_TEXT: constants.SERVICES_URL,
    constants.PORTFOLIO_TEXT: constants.PORTFOLIO_URL,
    constants.CONTACT_TEXT: constants.CONTACT_URL
}

#Try and loop through an array
for test_name, test_url in text_url_array.items():
    #Call the function that it to perform the actual test
    test_results = functions.test_click_item(constants.TEST_URL,test_url, test_name)
    print(f"All tests have been completed. Please check the log file for details. {test_results}")

    #Create a log file to hold the test results. The log file will be created in the logs directory with a timestamp in the filename.
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S_%f")

    lines_of_text = [
        f"Test Title:{test_name}\n",
        f"Test URL:{test_url}\n",
        f"Target URL:{text_url_array}\n",
        f"Result:{test_results}\n"
        f"Time of test:{now}\n",
        f"----------------------------------------\n"
    ]

    #Write the lines of text to a log file
    with open(f"logs/LOG_FILE_{timestamp}.txt", "w", encoding="utf-8") as file:
        file.writelines(lines_of_text)


# STEP 2: NEW - Test unavailable URL
# OUTSIDE THE LOOP - Runs only once
print("\nStarting undefined URL test...")

undefined_result = functions.test_undefined_url(
    constants.UNDEFINED_URL
)

print(f"Undefined URL test: {undefined_result}")

# STEP 3: NEW - Log undefined URL test
now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S_%f")

lines_of_text = [
    "Test Title: Undefined URL Test\n",
    f"Test URL: {constants.UNDEFINED_URL}\n",
    "Expected HTTP Status: 404\n",
    f"Result: {undefined_result}\n",
    f"Time of test: {now}\n",
    "----------------------------------------\n"
]

with open(
    f"logs/LOG_FILE_{timestamp}.txt",
    "w",
    encoding="utf-8"
) as file:
    file.writelines(lines_of_text)


#Close the test activities after the test
print(f"End of test for all items. Closing the browser now...")
functions.close_browser()
