from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/groups/discover"
    btn_create_group_locator = (By.CSS_SELECTOR,".button-create_2xvTJu93")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_create_group = None
        self.present_locator = self. btn_create_group_locator

    def init_elements(self):
        super().init_elements()
        self.btn_create_group = super().get_element(self.btn_create_group_locator)
