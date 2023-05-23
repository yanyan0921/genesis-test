from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://genesis-staging.hq.unity3d.com/organizations/18966698513222/"
    href_unity_plus_locator = (By.LINK_TEXT, "Unity Plus")
    href_unity_pro_locator = (By.LINK_TEXT, "Unity Pro")
    href_user_locator = (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/u-audit/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.href_unity_plus = None
        self.href_unity_pro = None
        self.href_user = self.href_user_locator
        self.present_locator = self.href_user_locator

    def init_elements(self):
        super().init_elements()
        self.href_unity_plus = super().get_element(self.href_unity_plus_locator)
        self.href_unity_pro = super().get_element(self.href_unity_pro_locator)
        self.href_user = super().get_element(self.href_user_locator)
