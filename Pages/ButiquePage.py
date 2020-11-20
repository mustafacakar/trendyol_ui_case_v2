from selenium.webdriver.common.by import By
import logging
from Pages.BasePage import BasePage
import time


class ButiquePage(BasePage):
    firstButique = (By.CSS_SELECTOR, "#navigation-wrapper > nav > ul > li:nth-child(1)")
    choosedStore = (By.CSS_SELECTOR, "#browsing-gw-homepage > div > div:nth-child(2) > div.sticky-wrapper > div.component-list.component-big-list > article:nth-child(1)")
    chooseProduct = (By.CSS_SELECTOR, "#boutique-detail-app > div > div:nth-child(2) > div > div:nth-child(1)")
    addToBasketButton = (By.CSS_SELECTOR, ".add-to-bs")

    """contructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """this is used to select one butique"""
    def select_store(self):
        self.do_click(self.choosedStore)


    """this is used to check images loaded succesfully in store """
    def check_product_images_in_store(self):
        driver = self.driver
        time.sleep(1)
        productCount = len(driver.find_elements_by_class_name("boutique-product"))
        print("Bu sayfada" + str(productCount) + "ürün bulunmaktadır.")

        for x in range(1, productCount):
            try:
                elementPath = "div.boutique-product:nth-child(" + str(
                    x) + ") > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)"
                mainElem = driver.find_element_by_css_selector(elementPath)
                mainElemSrc = driver.find_element_by_css_selector(elementPath).get_attribute("src")
                driver.execute_script("arguments[0].scrollIntoView();", mainElem)
                print(elementPath)
                print(mainElemSrc)

                ###Get Element attributes
                productPath = "div.boutique - product: nth - child(" + str(x) + ")"
                productTitle = driver.find_element_by_css_selector(productPath).get_attribute("title")
                productID = driver.find_element_by_css_selector(productPath).get_attribute("id")

                if (mainElemSrc == "/Content/images/defaultThumb.jpg"):
                    logging.error("Fotoğraf yüklenemedi. ProductID : " + productID + "Product Title : " + productTitle)
                else:
                    logging.info(
                        "Fotoğraf başarıyla görüntülendi. Product ID : " + productID + "Product Title : " + productTitle)

            except Exception:
                pass

    """this is used to select one product in all products"""
    def select_product(self):
        self.do_click(self.chooseProduct)
