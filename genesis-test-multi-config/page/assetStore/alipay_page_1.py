from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    input_account_locator = (By.NAME, "loginId")
    input_password_locator = (By.NAME, "payPasswd_rsainput")
    next_step_locator = (By.XPATH,"//*[@id=\"J_newBtn\"]/span")
    checkcode_locator = (By.NAME,"checkCode")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.input_account = None
        self.input_password = None
        self.next_step = None
        self.checkcode = None
        self.present_locator = self.next_step_locator

    def init_elements(self):
        super().init_elements()
        self.input_account = super().get_element(self.input_account_locator)
        self.input_password = super().get_element(self.input_password_locator)
        self.next_step = super().get_element(self.next_step_locator)
        self.checkcode = super().get_element(self.checkcode_locator)
