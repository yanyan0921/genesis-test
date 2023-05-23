from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    btn_post_now_locator = (By.CSS_SELECTOR, ".post_3zXA0Q8b")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_post_now= None
        self.present_locator = self.btn_post_now_locator

    def init_elements(self):
        super().init_elements()
        self.btn_post_now = super().get_element(self.btn_post_now_locator)
