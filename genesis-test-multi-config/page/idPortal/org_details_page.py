from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-staging.unity.com/en/organizations/order-request"
    assetStoreCredit_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div[2]/nav/ul/li[5]/ul/li[6]/a")
    orderRequest_locator = (By.XPATH,"//*[@id=\"main-wrapper\"]/div[2]/nav/ul/li[5]/ul/li[8]/a")
    assetManagement_locator = (By.XPATH,"//*[@id=\"main-wrapper\"]/div[2]/nav/ul/li[5]/ul/li[7]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.assetStoreCredit = self.assetStoreCredit_locator
        self.orderRequest = self.orderRequest_locator
        self.assetManagement = self.assetManagement_locator
        self.present_locator = self.orderRequest_locator

    def init_elements(self):
        super().init_elements()
        self.assetStoreCredit = super().get_element(self.assetStoreCredit_locator)
        self.orderRequest = super().get_element(self.orderRequest_locator)
        self.assetManagement = super().get_element(self.assetManagement_locator)







