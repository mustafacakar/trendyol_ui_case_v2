from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
import time


class LoginPage(BasePage):

    EMAIL = (By.ID, "login-email")
    PASSWORD = (By.ID, "login-password-input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".q-primary")

    """contructor of the page class"""
    def __init__(self,driver):
        super().__init__(driver)



    """Page Actions for Login Page"""

    """this is used to get the page title"""
    def get_login_page_title(self,title):
        return self.get_title(title)



    """this is used to login to Trendyol"""
    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)
        time.sleep(3)