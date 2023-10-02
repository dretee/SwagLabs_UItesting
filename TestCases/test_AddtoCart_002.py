import time
from selenium.webdriver.common.by import By
from Utilities.ReadProperties import Readcongftest
from PageObjects.loginObjects import loginObjects
from Utilities.customerlogger import logen
from PageObjects.AddtocartObjects import AddcartObject
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddRemoveToCart:
    url = Readcongftest.Getapplicationurl()
    username = Readcongftest.GetUsername()
    password = Readcongftest.GetPassword()
    logger = logen.logging_info()

    def test_addtocart(self, setup):
        # Initialize driver and navigate to the application URL
        self.logger.info("******* TEST TO ADD ITEMS TO THE CART (test_addtocart) ***********")
        self.logger.info("******* INITIALIZING THE DRIVER AND OPENING THE WEBPAGE***********")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        # Login sequence
        self.logger.info("******* LOGIN SEQUENCE, GETTING THE USERNAME AND THE PASSWORD***********")
        self.li = loginObjects(self.driver)
        self.li.GetUserName(self.username)
        self.li.GetUserPassword(self.password)
        self.li.ClickSubmit()

        # Initialize AddcartObject and add items to the cart
        self.ac = AddcartObject(self.driver)
        list_of_items = []
        items_to_add = {
            "Sauce Labs Fleece Jacket": self.ac.addFleece_Jacket,
            "Test.allTheThings() T-Shirt (Red)": self.ac.addT_Shirt_Red,
            "Sauce Labs Onesie": self.ac.addOnesie,
            "Sauce Labs Backpack": self.ac.addBackpack,
            "Sauce Labs Bike Light": self.ac.addBike_Light,
            "Sauce Labs Bolt T-Shirt": self.ac.addBolt_TShirt
        }
        count = 0
        self.logger.info("******* CALLING THE FUNCTIONS FOR THE DICTIONARY ***********")
        self.logger.info("******* USING THE FOR LOOP TO CALL THEM "
                         "AND STORING THE NAMES OF THOSE CALLED IN A DICTIONARY ***********")
        for name, item_function in items_to_add.items():
            item_function()
            list_of_items.append(name)
            count += 1
            self.logger.info(F"******* ADDITION OF THE ITEM {count}***********")

        # Verify if the items were added to the cart
        self.logger.info("******* OPENING THE CART TO VERIFY IF THE ITEMS WERE ADDED VISUALLY ***********")
        time.sleep(2)
        self.ac.Cart_click()
        time.sleep(2)
        nos_on_cartIcon = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
        expected_item_count = count
        body_text = self.driver.find_element(By.TAG_NAME, "body").text

        if nos_on_cartIcon == str(expected_item_count) and all(item in body_text for item in list_of_items):
            print(f"the number of items added is {count} ")
            self.logger.info("Items were added to the cart successfully.")
            self.driver.quit()
            assert True
        else:
            print(f"the number of items added is {count} ")
            self.logger.error("Items were not added to the cart correctly.")
            self.driver.quit()
            assert False


