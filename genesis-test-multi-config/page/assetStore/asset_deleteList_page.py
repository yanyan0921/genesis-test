from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    Yes_btn_locator = (By.CSS_SELECTOR, "[class='_3UE3J _3zD70 auto _27Drk']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.Yes_btn = None
        self.present_locator = self.Yes_btn_locator

    def init_elements(self):
        super().init_elements()
        self.Yes_btn = super().get_element(self.Yes_btn_locator)
