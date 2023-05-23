from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_read_locator = (By.XPATH, "//*[@id=\"notification_div\"]/div/div[1]/a[2]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_read = None
        self.present_locator = self.btn_read_locator

    def init_elements(self):
        super().init_elements()
        self.btn_read = super().get_element(self.btn_read_locator)
