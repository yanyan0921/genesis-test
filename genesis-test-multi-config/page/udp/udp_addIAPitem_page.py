from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    input_productid_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[3]/div/div[4]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div/input")
    input_productname_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[3]/div/div[4]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/div/input")
    btn_checkbox_consumble_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[3]/div/div[4]/div[2]/div/div/div/div[2]/div[1]/div/div[3]/div[2]/div/button")
    input_iapdescription_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[3]/div/div[4]/div[2]/div/div/div/div[2]/div[1]/div/div[4]/div/div/textarea")
    icon_closeiapifont_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[3]/div/div[4]/div[2]/div/div/div/div[1]/button/div")
    btn_iapcancel_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[3]/div/div[4]/div[2]/div/div/div/div[3]/div[1]/button")
    btn_iapsave_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[3]/div/div[4]/div[2]/div/div/div/div[3]/div[2]/button")
    icon_language_dropdown_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[4]/div[3]/div/button/div/div[2]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_productid = None
        self.input_productname = None
        self.btn_checkbox_consumble = None
        self.input_iapdescription = None
        self.icon_closeiapifont = None
        self.btn_iapcancel = None
        self.btn_iapsave = None
        self.present_locator = self.icon_language_dropdown_locator

    def init_elements(self):
        super().init_elements()
        self.input_productid = super().get_element(self.input_productid_locator)
        self.input_productname = super().get_element(self.input_productname_locator)
        self.btn_checkbox_consumble = super().get_element(self.btn_checkbox_consumble_locator)
        self.input_iapdescription = super().get_element(self.input_iapdescription_locator)
        self.icon_closeiapifont = super().get_element(self.icon_closeiapifont_locator)
        self.btn_iapcancel = super().get_element(self.btn_iapcancel_locator)
        self.btn_iapsave = super().get_element(self.btn_iapsave_locator)
        self.icon_language_dropdown = super().get_element(self.icon_language_dropdown_locator)
