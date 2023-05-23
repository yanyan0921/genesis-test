from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Page(BasePage):
    view_detail_btn_locator = (By.CLASS_NAME, "_1BWkF")
    status_text_locator = (By.CSS_SELECTOR,"[class = '_2pcIL _1jtXf']")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.view_detail_btn = self.view_detail_btn_locator
        self.status_text = None
        self.present_locator = self.view_detail_btn

    def init_elements(self):
        super().init_elements()
        self.view_detail_btn = super().get_element(self.view_detail_btn_locator)
        self.status_text = super().get_element(self.status_text_locator)