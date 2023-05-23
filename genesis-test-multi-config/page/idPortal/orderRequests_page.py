from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-staging.unity.com/en/organizations/order-request/order_requests"
    decline_btn_locator = (By.XPATH, '//*[@id="content-wrapper"]/div/div[3]/div[2]/table/tbody/tr[1]/td[7]/a[2]')
    view_btn_locator = (By.XPATH, '//*[@id="content-wrapper"]/div/div[3]/div[2]/table/tbody/tr[1]/td[7]/a[1]')
    declinedByName_locator = (By.XPATH, '//*[@id="content-wrapper"]/div/div[3]/div[2]/table/tbody/tr[1]/td[7]/span')
    errorTip_locator = (By.CSS_SELECTOR,"[class='error']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.decline_btn = self.decline_btn_locator
        self.view_btn = self.view_btn_locator
        self.declinedByName = None
        self.errorTip = None
        self.present_locator = self.decline_btn_locator

    def init_elements(self):
        super().init_elements()
        self.decline_btn = super().get_element(self.decline_btn_locator)
        self.view_btn = super().get_element(self.view_btn_locator)
        self.declinedByName = super().get_element(self.declinedByName_locator)
        self.errorTip = super().get_element(self.errorTip_locator)







