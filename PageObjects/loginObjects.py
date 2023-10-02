from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class loginObjects:
    inputbox_Username_xpath = "//input[@id='user-name']"
    inputbox_Password_xpath = "//input[@id='password']"
    Searchbutton_xpath = "//input[@id='login-button']"
    menu_button_xpath = "//button[@id='react-burger-menu-btn']"
    logout_button_xpath = "//a[@id='logout_sidebar_link']"

    def __init__(self, driver):
        self.driver = driver

    def GetUserName(self, username):
        self.driver.find_element(By.XPATH, self.inputbox_Username_xpath).clear()
        self.driver.find_element(By.XPATH, self.inputbox_Username_xpath).send_keys(username)

    def GetUserPassword(self, Password):
        self.driver.find_element(By.XPATH, self.inputbox_Password_xpath).clear()
        self.driver.find_element(By.XPATH, self.inputbox_Password_xpath).send_keys(Password)

    def ClickSubmit(self):
        self.driver.find_element(By.XPATH, self.Searchbutton_xpath).click()

    def LogoutSequence(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.menu_button_xpath))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.logout_button_xpath))).click()

