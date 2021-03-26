import time

from selenium.webdriver.common.by import By
from configurations.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    LogIn = (By.LINK_TEXT, 'Log in')
    Email = (By.ID, 'user')
    Password = (By.ID, 'password')
    LoginWithAltassianBtn = (By.ID, 'login')
    LoginBtn = (By.ID, 'login-submit')



    def __init__(self, driver):
        super().__init__(driver)


    def loginToApplication(self):
        self.do_click(self.LogIn)
        self.do_send_keys(self.Email, TestData.Email)
        time.sleep(5)
        self.do_click(self.LoginWithAltassianBtn)
        time.sleep(5)
        self.do_send_keys(self.Password, TestData.Password)
        self.do_click(self.LoginBtn)
        time.sleep(5)



