from page.base_page import BasePage
from selenium.webdriver.common.by import By

class Page(BasePage):
    btn_plus_locator = (By.ID, "cta-cd21c916")
    btn_pro_locator = (By.ID, "cta-b118ce00")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_plus = None
        self.btn_pro = None

    def init_elements(self):
        super().init_elements()
        self.btn_plus = super().get_element(self.btn_plus_locator)
        self.btn_pro = super().get_element(self.btn_pro_locator)
