from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    remove_btn_locator=(By.CSS_SELECTOR,"[class='_3UE3J _3vV3- auto']")
    site_stg1_price_locator = (By.CSS_SELECTOR,"[class = '_3Z7ge']")
    move_to_cart_locator = (By.CSS_SELECTOR,"[class = '_3UE3J _3vV3- auto _1EJPn add-to-cart-wrap']")
    cart_view_locator = (By.CSS_SELECTOR,"[class = '_17YTr']")

    def __init__(self , driver, wait):
        super().__int__(driver, wait)
        self.remove_btn = self.remove_btn_locator
        self.site_stg1_price = self.site_stg1_price_locator
        self.move_to_cart = self.move_to_cart_locator
        self.cart_view = self.cart_view_locator
        self.present_locator = self.remove_btn_locator


    def init_elements(self):
        super().init_elements()
        self.remove_btn = super().get_element(self.remove_btn_locator)
        self.site_stg1_price = super().get_element(self.site_stg1_price_locator)
        self.move_to_cart = super().get_element(self.move_to_cart_locator)
        self.cart_view = super().get_element(self.cart_view_locator)
