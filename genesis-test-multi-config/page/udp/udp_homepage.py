from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    icon_console_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[1]/div/div/span")
    icon_about_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[2]/div/div/span")
    icon_getstart_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[3]/div/div/span")
    btn_Login_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[2]/div[3]/button")
    icon_login_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[2]/div[2]/div/div/div/div/div")
    icon_language_dropdown_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[3]/div/button/div/div[2]")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.icon_console = None
        self.icon_about = None
        self.icon_getstart = None
        self.btn_Login = None
        self.icon_login = None
        self.present_locator = self.icon_language_dropdown_locator

    def init_elements(self):
        super().init_elements()
        self.icon_console = super().get_element(self.icon_console_locator)
        self.icon_about = super().get_element(self.icon_about_locator)
        self.icon_getstart = super().get_element(self.icon_getstart_locator)
        self.btn_Login = super().get_element(self.btn_Login_locator)
        self.icon_login = super().get_element(self.icon_login_locator)
        self.icon_language_dropdown = super().get_element(self.icon_language_dropdown_locator)
