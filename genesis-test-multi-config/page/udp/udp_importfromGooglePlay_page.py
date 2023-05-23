from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    input_GooglePlaylink_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[5]/div[2]/div/div/div/div[2]/div[2]/div/div/div/input")
    icon_closeGoogleifont_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[5]/div[2]/div/div/div/div[1]/button/div")
    btn_import_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[5]/div[2]/div/div/div/div[3]/div/button")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_GooglePlaylink = None
        self.icon_closeGoogleifont= None
        self.present_locator = self.btn_import_locator

    def init_elements(self):
        super().init_elements()
        self.input_GooglePlaylink = super().get_element(self.input_GooglePlaylink_locator)
        self.icon_closeGoogleifont = super().get_element(self.icon_closeGoogleifont_locator)
        self.btn_import = super().get_element(self.btn_import_locator)
