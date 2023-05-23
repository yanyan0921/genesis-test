from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://plastichub-int.unity.cn/"
    icon_sign_in_locator = (By.XPATH, "//*[@id=\"navbar\"]/div[2]/a")
    btn_login_by_account_locator = (By.XPATH, "//*[@id=\"content-wrapper\"]/div/div/div/div[1]/ul/li[2]/a")
    icon_email_login_locator = (By.XPATH, "//*[@id=\"content-wrapper\"]/div/div/div/div/ul/li[2]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.icon_sign_in = None
        self.btn_login_by_account = None
        self.icon_email_login = None
        self.present_locator = self.icon_sign_in_locator

    def init_elements(self):
        super().init_elements()
        self.icon_sign_in = super().get_element(self.icon_sign_in_locator)
        self.btn_login_by_account = super().get_element(self.btn_login_by_account_locator)
        self.icon_email_login = super().get_element(self.icon_email_login_locator)
