from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    input_useremail_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[7]/div/div[3]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div/textarea")
    btn_closeBetauser_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[7]/div/div[3]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div/div[1]/button/div")
    btn_usercancel_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[7]/div/div[3]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div/div[3]/div[1]/button")
    btn_usercreate_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[7]/div/div[3]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div/div[3]/div[2]/button")
    icon_language_dropdown_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[4]/div[3]/div/button/div/div[2]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_useremail = None
        self.btn_closeBetauser = None
        self.btn_usercancel = None
        self.btn_usercreate = None
        self.present_locator = self.icon_language_dropdown_locator

    def init_elements(self):
        super().init_elements()
        self.input_useremail = super().get_element(self.input_useremail_locator)
        self.btn_closeBetauser = super().get_element(self.btn_closeBetauser_locator)
        self.btn_usercancel = super().get_element(self.btn_usercancel_locator)
        self.btn_usercreate = super().get_element(self.btn_usercreate_locator)
        self.icon_language_dropdown = super().get_element(self.icon_language_dropdown_locator)
