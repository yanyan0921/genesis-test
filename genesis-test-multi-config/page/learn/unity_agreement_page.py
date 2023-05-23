from page.base_page import BasePage
from selenium.webdriver.common.by import By

class Page(BasePage):
    base_url = "https://id-int.unity.com/en/conversations/"
    accept_btn1_locator = (By.XPATH, "//form[@id='new_conversations_accept_updated_tos_form']/div[2]/button[1]")
    accept_btn2_locator = (By.XPATH, "//form[@id='new_conversations_accept_updated_tos_form']/div[2]/button[2]")

    def __init__(self, driver, wait):
        super().__int__(driver,wait)
        self.url = self.base_url
        self.accept_btn1 = None
        self.accept_btn2 = None
        self.present_locator = self.accept_btn2_locator

    def init_elements(self):
        super().init_elements()
        self.accept_btn1 =super().get_element(self.accept_btn1_locator)
        self.accept_btn2 = super().get_element(self.accept_btn2_locator)