from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://urdp.unity.cn/host-list"
    voucherstext_locator = (By.XPATH, '/html/body/app-component/balance-component/admin-layout-component/mat-sidenav-container/mat-sidenav-content/mat-card/div[1]/balance-item-component[2]/div[2]/span')



    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.voucherstext=self.voucherstext_locator


        self.present_locator = self.voucherstext_locator

    def init_elements(self):
        super().init_elements()
        self.voucherstext = super().get_element(self.voucherstext_locator)
