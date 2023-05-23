from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    input_title_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/input")
    btn_cancel_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[3]/div[1]/button")
    btn_create_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[3]/div[2]/button")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_title = None
        self.btn_cancel = None
        self.btn_create = None
        self.present_locator = self.btn_create_locator

    def init_elements(self):
        super().init_elements()
        self.input_title = super().get_element(self.input_title_locator)
        self.btn_cancel = super().get_element(self.btn_cancel_locator)
        self.btn_create = super().get_element(self.btn_create_locator)
