from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-staging.unity.com/en/account"
    icon_chevron_down_locator = (By.CLASS_NAME, "ico-chevron-down")
    icon_sign_out_locator = (By.XPATH, "//*[@id=\"user-panel\"]/div/a[4]/i")
    href_account_management_locator = (By.CLASS_NAME, "ico-remove-user")
    organizations_locator = (By.XPATH,"/html/body/div/section/div[2]/nav/ul/li[5]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.icon_chevron_down = None
        self.icon_sign_out = None
        self.href_organization = None
        self.organizations = None
        self.present_locator = self.href_account_management_locator

    def init_elements(self):
        super().init_elements()
        self.icon_chevron_down = super().get_element(self.icon_chevron_down_locator)
        self.icon_sign_out = super().get_element(self.icon_sign_out_locator)
        self.href_account_management_locator = super().get_element(self.href_account_management_locator)
        self.organizations = super().get_element(self.organizations_locator)
