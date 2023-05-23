from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    list_name_locator = (By.CSS_SELECTOR, "[class='_1gSGR']")
    save_btn_locator = (By.CSS_SELECTOR, "[class = '_3UE3J pDJt- auto IaiTq']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.list_name = None
        self.save_btn = None
        self.present_locator = self.list_name_locator

    def init_elements(self):
        super().init_elements()
        self.list_name = super().get_element(self.list_name_locator)
        self.save_btn = super().get_element(self.save_btn_locator)
