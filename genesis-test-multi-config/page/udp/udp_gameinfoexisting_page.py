from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    btn_mygames_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[1]/div/div/span")
    btn_reporting_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[2]/div/div/span")
    btn_partnerstores_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[3]/div/div/span")
    btn_documentation_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[4]/div/div/span")
    btn_gamecancel_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[1]/div[2]/div[1]/button")
    btn_gamesave_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[1]/div[2]/div[2]/button")
    btn_editinfo_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[1]/div[2]/div[1]")
    btn_release_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[1]/div[2]/div[2]/button")
    icon_language_dropdown_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[4]/div[3]/div/button/div/div[2]")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_mygames = None
        self.btn_reporting = None
        self.btn_partnerstores = None
        self.btn_documentation = None
        self.btn_gamecancel = None
        self.btn_gamesave = None
        self.btn_editinfo = None
        self.btn_release = None
        self.present_locator = self.icon_language_dropdown_locator

    def init_elements(self):
        super().init_elements()
        self.btn_mygames = super().get_element(self.btn_mygames_locator)
        self.btn_reporting = super().get_element(self.btn_reporting_locator)
        self.btn_partnerstores = super().get_element(self.btn_partnerstores_locator)
        self.btn_documentation = super().get_element(self.btn_documentation_locator)
        self.btn_gamecancel = super().get_element(self.btn_gamecancel_locator)
        self.btn_gamesave = super().get_element(self.btn_gamesave_locator)
        self.btn_editinfo = super().get_element(self.btn_editinfo_locator)
        self.icon_language_dropdown = super().get_element(self.icon_language_dropdown_locator)

