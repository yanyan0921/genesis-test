from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Page(BasePage):
    cancel_btn_locator = (By.CSS_SELECTOR, "[class='view-invoice-link']")
    Yes_sure_btn_locator = (By.CSS_SELECTOR,"[class='_3UE3J _3zD70 auto _27Drk']")
    price_text_locator = (By.XPATH,"//*[@id=\"main-layout-scroller\"]/div/div[1]/div/div/div/div[2]/div[2]/div[1]/div[4]")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.cancel_btn = self.cancel_btn_locator
        self.Yes_sure_btn = None
        self.price_text = None
        self.present_locator = self.cancel_btn

    def init_elements(self):
        super().init_elements()
        self.cancel_btn= super().get_element(self.cancel_btn_locator)
        self.Yes_sure_btn = super().get_element(self.Yes_sure_btn_locator)
        self.price_text = super().get_element(self.price_text_locator)
