from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    input_accountemail_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[5]/div/div[2]/div/div[1]/div/div/input")
    input_accountpassword_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[5]/div/div[2]/div/div[2]/div/div/input")
    btn_accountcancel_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[5]/div/div[2]/div/div[3]/div/div[1]/button")
    btn_accountsave_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[5]/div/div[2]/div/div[3]/div/div[2]/button")
    icon_language_dropdown_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[4]/div[3]/div/button/div/div[2]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_accountemail = None
        self.input_accountpassword = None
        self.btn_accountcancel = None
        self.btn_accountsave = None
        self.present_locator = self.icon_language_dropdown_locator

    def init_elements(self):
        super().init_elements()
        self.input_accountemail = super().get_element(self.input_accountemail_locator)
        self.input_accountpassword = super().get_element(self.input_accountpassword_locator)
        self.btn_accountcancel = super().get_element(self.btn_accountcancel_locator)
        self.btn_accountsave = super().get_element(self.btn_accountsave_locator)
        self.icon_language_dropdown = super().get_element(self.icon_language_dropdown_locator)
