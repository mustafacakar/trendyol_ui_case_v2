import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.ButiquePage import ButiquePage
from Pages.ProductPage import ProductPage
from Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_home_page_load(self):
        self.homePage = HomePage(self.driver)
        self.homePage.get_home_page()



    def test_login_page_load(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click_login_button()

    def test_valid_user_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)

    def test_butique_images(self):
        self.homePage = HomePage(self.driver)
        self.homePage.check_butique_images()


    def test_images_in_selected_store(self):
        self.butiquePage = ButiquePage(self.driver)
        self.butiquePage.select_store()
        self.butiquePage.check_product_images_in_store()

    def test_select_product(self):
        self.butiquePage = ButiquePage(self.driver)
        self.butiquePage.select_product()

    def test_add_to_basket(self):
        self.productPage = ProductPage(self)