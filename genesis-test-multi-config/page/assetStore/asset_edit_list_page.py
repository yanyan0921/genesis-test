from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    create_newList_btn_locator = (By.CSS_SELECTOR, "[class='_3UE3J ZQFsR auto EaoU7']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.create_newList_btn = None
        self.present_locator = self.create_newList_btn_locator

    def init_elements(self):
        super().init_elements()
        self.create_newList_btn = super().get_element(self.create_newList_btn_locator)
