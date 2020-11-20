from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
import time
import logging


class HomePage(BasePage):

    EMAIL = (By.ID, "login-email")
    ACCOUNT_BTN = (By.ID,"accountBtn")
    POPUP_CLOSE = (By.CSS_SELECTOR,"html.fancybox-margin.fancybox-lock body div.fancybox-overlay.fancybox-overlay-fixed div.fancybox-wrap.fancybox-desktop.fancybox-type-html.fancybox-opened div.fancybox-skin a.fancybox-item.fancybox-close")
    ACC_LOGIN_BTN = (By.CSS_SELECTOR, "div.account-button:nth-child(1)")
    firstButique = (By.CSS_SELECTOR,"#navigation-wrapper > nav > ul > li:nth-child(1)")



    """contructor of the page class"""
    def __init__(self,driver):
        super().__init__(driver)



    """this is used to get home page = trendyol"""
    def get_home_page(self):
        self.driver.get(TestData.BASE_URL)
        self.do_click(self.POPUP_CLOSE)

    """this is used to hover account button + click Login button"""
    def click_login_button(self):
        self.hover(self.ACCOUNT_BTN)
        self.do_click(self.ACC_LOGIN_BTN)

    """this is used to check butique images in all categories"""
    def check_butique_images(self):
        driver = self.driver
        driver.find_element(*self.firstButique).click()

        ## turn all categories
        for x in range(1, 9):
            butiqueElement = "#navigation-wrapper > nav > ul > li:nth-child(" + str(x) + ")"
            driver.find_element_by_css_selector(butiqueElement).click()
            butiqueCount = len(driver.find_elements_by_class_name("component-item"))

            # ## turn images in one butique
            for y in range(1, butiqueCount):
                time.sleep(0.25)
                imgPath = "article.component-item:nth-child(" + str(
                    y) + ") > a:nth-child(1) > span:nth-child(1) > img:nth-child(1)"

                imgElement = driver.find_element_by_css_selector(imgPath)
                imgSrc = driver.find_element_by_css_selector(imgPath).get_attribute("src")
                driver.execute_script("arguments[0].scrollIntoView();", imgElement)

                ## If image is not load -> https://cdn.dsmcdn.com//web/production/large_boutique_placeholder.png
                ## setting placeholoder url for image src.
                if (imgSrc != "https://cdn.dsmcdn.com//web/production/large_boutique_placeholder.png"):
                    logging.info("Image Başarıyla yüklendi. Başarılı URL : " + imgSrc)
                else:
                    logging.warning("Image Başarısız Yüklendi. Başarısız URL : " + imgSrc)


