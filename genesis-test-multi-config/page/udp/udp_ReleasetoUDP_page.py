from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    input_releasenote_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[5]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/textarea")
    btn_cancelrelease_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[5]/div[2]/div/div/div/div[3]/div[1]/button")
    btn_createrelease_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[5]/div[2]/div/div/div/div[3]/div[2]/button")
    icon_closereleaseifont_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[5]/div[2]/div/div/div/div[1]/button/div")
    icon_language_dropdown_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[3]/div/button/div/div[2]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_releasenote = None
        self.btn_cancelrelease = None
        self.icon_closereleaseifont = None
        self.present_locator = self.btn_createrelease_locator

    def init_elements(self):
        super().init_elements()
        self.input_releasenote = super().get_element(self.input_releasenote_locator)
        self.btn_cancelrelease = super().get_element(self.btn_cancelrelease_locator)
        self.btn_createrelease = super().get_element(self.btn_createrelease_locator)
        self.icon_closereleaseifont = super().get_element(self.icon_closereleaseifont_locator)


