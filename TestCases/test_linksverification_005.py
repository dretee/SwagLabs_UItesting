import requests
from selenium.webdriver.common.by import By
from PageObjects.loginObjects import loginObjects
from Utilities.ReadProperties import Readcongftest
from Utilities.customerlogger import logen


class Test_linkVerification:
    # Initialize class variables
    url = Readcongftest.Getapplicationurl()
    username = Readcongftest.GetUsername()
    password = Readcongftest.GetPassword()
    logger = logen.logging_info()

    def test_linkchecker_01(self, setup):
        # Initialize driver and navigate to the application URL
        self.logger.info("******* TEST TO CHECK LINKS FUNCTIONALITY (test_linkchecker_01) ***********")
        self.logger.info("******* INITIALIZING THE DRIVER AND OPENING THE WEBPAGE ***********")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        # Login to the application
        self.logger.info("******* LOGIN SEQUENCE INITIATED, GETTING THE USERNAME AND THE PASSWORD ***********")
        self.li = loginObjects(self.driver)
        self.li.GetUserName(self.username)
        self.li.GetUserPassword(self.password)
        self.li.ClickSubmit()

        # Get all links on the page
        all_links = self.driver.find_elements(By.TAG_NAME, "a")
        self.logger.info(f"The total number of links on this page is {len(all_links)}")

        # Initialize counters for broken and functional links
        count_broken = 0

        # Iterate through all links and check their status
        for link in all_links:
            url = link.get_attribute("href")
            try:
                response = requests.head(url)
            except:
                response = None

            if response is not None and response.status_code >= 400:
                count_broken += 1
                self.logger.info(f"THIS LINK {link} IS BROKEN")
            else:
                self.logger.info(f"THIS LINK {link} IS FUNCTIONAL")

        # Log the total number of broken and functional links
        self.logger.info(f"TOTAL BROKEN LINKS: {count_broken}")
        self.logger.info(f"TOTAL FUNCTIONAL LINKS: {len(all_links) - count_broken}")

        # Assert that there are no broken links
        assert count_broken == 0, "TEST FAILED: THERE ARE BROKEN LINKS ON THE PAGE"
        self.logger.info("TEST PASSED: ALL LINKS ARE FUNCTIONAL")
        self.driver.quit()
