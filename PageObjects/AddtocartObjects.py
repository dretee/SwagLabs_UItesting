from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddcartObject:
    addBackpack_xpath = "//button[@id='add-to-cart-sauce-labs-backpack']"
    removeBackpack_xpath = "//button[@id='remove-sauce-labs-backpack']"
    addBike_Light_xpath = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    removeBike_Light_xpath = "//button[@id='remove-sauce-labs-bike-light']"
    addBolt_TShirt_xpath = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    removeBolt_TShirt_xpath = "//button[@id='remove-sauce-labs-bolt-t-shirt']"
    addFleece_Jacket_xpath = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    removeFleece_Jacket_xpath = "//button[@id='remove-sauce-labs-fleece-jacket']"
    addOnesie_xpath = "//button[@id='add-to-cart-sauce-labs-onesie']"
    removeOnesie_xpath = "//button[@id='remove-sauce-labs-onesie']"
    addT_Shirt_Red_xpath = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    removeT_Shirt_Red_xpath = "//button[@id='remove-test.allthethings()-t-shirt-(red)']"
    cart_xpath = "//a[@class='shopping_cart_link']"
    continueShopping_xpath = "//button[@id='continue-shopping']"
    checkout_button_xpath = "//button[@id='checkout']"
    cancel_button_xpath = "//button[@id='cancel']"
    txt_firstname_id = "first-name"
    txt_lastname_id = "last-name"
    txt_zipcode_id = "postal-code"
    checkout_continue_xpath = "//input[@id='continue']"
    checkout_cancel_xpath = "//button[@id='cancel']"
    autoreset_xpath = "//a[@id='reset_sidebar_link']"
    menu_button_xpath = "//button[@id='react-burger-menu-btn']"
    finish_button_xpath = "//button[@id='finish']"
    back_home_xpath = "//button[@id='back-to-products']"

    def __init__(self, driver):
        self.driver = driver

    def addBackpack(self):
        self.driver.find_element(By.XPATH, self.addBackpack_xpath).click()

    def removeBackpack(self):
        self.driver.find_element(By.XPATH, self.removeBackpack_xpath).click()

    def addBike_Light(self):
        self.driver.find_element(By.XPATH, self.addBike_Light_xpath).click()

    def removeBike_Light(self):
        self.driver.find_element(By.XPATH, self.removeBike_Light_xpath).click()

    def addBolt_TShirt(self):
        self.driver.find_element(By.XPATH, self.addBolt_TShirt_xpath).click()

    def removeBolt_TShirt(self):
        self.driver.find_element(By.XPATH, self.removeBolt_TShirt_xpath).click()

    def addFleece_Jacket(self):
        self.driver.find_element(By.XPATH, self.addFleece_Jacket_xpath).click()

    def removeFleece_Jacket(self):
        self.driver.find_element(By.XPATH, self.removeFleece_Jacket_xpath).click()

    def addOnesie(self):
        self.driver.find_element(By.XPATH, self.addOnesie_xpath).click()

    def removeOnesie(self):
        self.driver.find_element(By.XPATH, self.removeOnesie_xpath).click()

    def addT_Shirt_Red(self):
        self.driver.find_element(By.XPATH, self.addT_Shirt_Red_xpath).click()

    def removeT_Shirt_Red(self):
        self.driver.find_element(By.XPATH, self.removeT_Shirt_Red_xpath).click()

    def OpenCart(self):
        self.driver.find_element(By.XPATH, self.cart_xpath).click()

    def ContinueShopping(self):
        self.driver.find_element(By.XPATH, self.continueShopping_xpath).click()

    def Checkout_button(self):
        self.driver.find_element(By.XPATH, self.checkout_button_xpath).click()

    def cancel_button(self):
        self.driver.find_element(By.XPATH, self.cancel_button_xpath).click()

    def inputTxtFirstname(self,firstname):
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(firstname)

    def inputTxtLastname(self,lastname):
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lastname)

    def inputTxtZipcode(self,nos):
        self.driver.find_element(By.ID, self.txt_zipcode_id).send_keys(nos)

    def CheckoutContinue(self):
        self.driver.find_element(By.XPATH, self.checkout_continue_xpath).click()

    def Checkoutcancel(self):
        self.driver.find_element(By.XPATH, self.checkout_button_xpath).click()

    def LogoutSequence(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.menu_button_xpath))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.autoreset_xpath))).click()

    def Cart_click(self):
        self.driver.find_element(By.XPATH, self.cart_xpath).click()

    def Finishbutton_click(self):
        self.driver.find_element(By.XPATH, self.finish_button_xpath).click()

    def Back_home_click(self):
        self.driver.find_element(By.XPATH, self.back_home_xpath).click()


