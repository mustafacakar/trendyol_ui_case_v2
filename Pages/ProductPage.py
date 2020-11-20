from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class ProductPage(BasePage):

    addToBasketButton = (By.CSS_SELECTOR, ".add-to-bs")

    """contructor of the page class"""
    def __init__(self,driver):
        super().__init__(driver)

    """this is used to click add to basket button in product page"""
    def add_to_basket(self):
        self.do_click(self.addToBasketButton)