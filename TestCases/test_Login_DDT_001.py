from Utilities import ReadXyFile
from Utilities.customerlogger import logen
from selenium.webdriver.common.by import By
from PageObjects.loginObjects import loginObjects
from Utilities.ReadProperties import Readcongftest


class TestLoginDDT001:
    base_url = Readcongftest.Getapplicationurl()
    logger = logen.logging_info()
    Path = ".\\TestData\\DDT_webpage1.xlsx"

    def test_homepage(self, setup):
        # Initialize the test and log the start
        self.logger.info("***** STARTING THE TEST ******")
        self.logger.info("***** STARTING THE LOGIN HOMEPAGE TEST ******")

        # Set up the WebDriver and navigate to the base URL
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("***** NAVIGATING TO THE TEST PAGE ******")

        # Get the actual title of the page
        actual_title = self.driver.title

        if actual_title == "Swag Labs":
            # Check if the actual title matches the expected title
            self.logger.info("***** TEST PASSED ******")
            self.logger.info("***** TEST PASSED ******")
            self.driver.quit()
            assert True
        else:
            # Handle the case where the actual title does not match the expected title
            self.logger.info("***** TEST FAILED ******")
            self.logger.info("***** TEST FAILED ******")
            self.driver.quit()
            assert False

    def test_Login_DDT_001(self, setup):
        # Initialize the test and log the start
        self.logger.info("***** STARTING THE TEST ******")

        # Set up the WebDriver and navigate to the base URL
        self.logger.info("***** STARTING THE LOGIN PROCESS TEST ******")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("***** NAVIGATING TO THE TEST PAGE ******")

        # Initialize loginObjects and a result list
        self.li = loginObjects(self.driver)
        result = []

        # Get the number of rows in the data file (assuming ReadXyFile is a module for reading data)
        self.rowcount = ReadXyFile.getRowCount(self.Path, "swag labs")
        self.logger.info(f"Total rows to process: {self.rowcount}")

        # Loop through the rows starting from row 3 (assuming data starts from row 3)
        for r in range(3, self.rowcount + 1):
            # Read data from the file for username, password, and expected title
            self.username = ReadXyFile.readData(self.Path, "swag labs", r, 1)
            self.password = ReadXyFile.readData(self.Path, "swag labs", r, 2)
            self.expected_title = ReadXyFile.readData(self.Path, "swag labs", r, 3)
            self.logger.info(f"Processing row {r}: username='{self.username}', password='{self.password}', "
                             f"expected_title='{self.expected_title}'")

            # Input username and password, then click submit
            self.li.GetUserName(self.username)
            self.li.GetUserPassword(self.password)
            self.li.ClickSubmit()

            # Get the actual title from the page
            actual_title = self.driver.find_element(By.TAG_NAME, "body").text
            if "Add to cart" in actual_title:

                # Check if the expected title is "Pass" or "Fail"
                if self.expected_title == "Pass":
                    self.li.LogoutSequence()  # Logout if expected to pass
                    result.append("Pass")
                    self.logger.info("***** Test passed. Logging out. *****")
                elif self.expected_title == "Fail":
                    self.li.LogoutSequence()  # Logout if expected to fail
                    result.append("Fail")
                    self.logger.info("***** Test failed. Logging out. *****")
            elif "Add to cart" not in actual_title:
                # Handle cases where the "Add to cart" text is not found
                if self.expected_title == "Pass":
                    result.append("Fail")  # If expected to pass, it's a failure
                    self.logger.info("***** Test failed. *****")
                elif self.expected_title == "Fail":
                    result.append("Pass")  # If expected to fail, it's a pass
                    self.logger.info("***** Test passed. *****")

        # Check the overall result
        if "Fail" not in result:
            print(result)
            self.driver.quit()
            self.logger.info("***** Overall test result: Pass *****")
            assert True
        else:
            print(result)
            self.driver.quit()
            self.logger.info("***** Overall test result: Fail *****")
            assert False








