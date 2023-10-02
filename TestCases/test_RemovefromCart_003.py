from selenium.webdriver.common.by import By
from Utilities.ReadProperties import Readcongftest
from PageObjects.loginObjects import loginObjects
from Utilities.customerlogger import logen
from PageObjects.AddtocartObjects import AddcartObject


class TestAddRemoveToCart:
    url = Readcongftest.Getapplicationurl()
    username = Readcongftest.GetUsername()
    password = Readcongftest.GetPassword()
    logger = logen.logging_info()

    def test_removefromcart(self, setup):

        # Initialize driver and navigate to the application URL
        self.logger.info("******* TEST TO REMOVE ITEMS FROM THE CART (test_removefromcart) ***********")
        self.logger.info("******* INITIALIZING THE DRIVER AND OPENING THE WEBPAGE***********")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        # Login sequence
        self.logger.info("******* LOGIN SEQUENCE INITIATED, GETTING THE USERNAME AND THE PASSWORD***********")
        self.li = loginObjects(self.driver)
        self.li.GetUserName(self.username)
        self.li.GetUserPassword(self.password)
        self.li.ClickSubmit()

        # Adding items to the cart
        self.ac = AddcartObject(self.driver)
        items_to_add = [self.ac.addFleece_Jacket, self.ac.addT_Shirt_Red, self.ac.addOnesie,
                        self.ac.addBackpack, self.ac.addBike_Light, self.ac.addBolt_TShirt]
        counts = 0

        for index in range(0, len(items_to_add), 2):
            item_function = items_to_add[index]
            item_function()  # Call the function at the even index
            counts += 1
            self.logger.info(F"******* ADDITION OF THE ITEM {counts}***********")

        self.ac.Cart_click()  # go to cart

        # Remove all items from the cart
        item_to_remove = [self.ac.removeFleece_Jacket, self.ac.removeT_Shirt_Red, self.ac.removeOnesie,
                          self.ac.removeBackpack, self.ac.removeBike_Light, self.ac.removeBolt_TShirt]
        count = 0
        for items in range(0, len(item_to_remove), 2):
            item_removal = item_to_remove[items]
            item_removal()  # Call the function at the even item
            count += 1
            self.logger.info(F"******* REMOVAL OF THE ITEM {count}***********")
        body_text = self.driver.find_element(By.TAG_NAME, "body").text

        # Proceed to check the item removed via the number displayed on the cart icon
        item_list = ["Sauce Labs Fleece Jacket",
                     "Test.allTheThings() T-Shirt (Red)",
                     "Sauce Labs Onesie",
                     "Sauce Labs Backpack",
                     "Sauce Labs Bike Light",
                     "Sauce Labs Bolt T-Shirt"]
        if all(items not in body_text for items in item_list):
            self.logger.info("Items were removed from the cart successfully.")
            self.driver.quit()
            assert True
        else:
            self.logger.error("Items were not removed from the cart correctly.")
            self.driver.quit()
            assert False
