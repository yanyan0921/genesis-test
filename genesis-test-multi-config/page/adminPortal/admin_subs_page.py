from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://genesis-staging.hq.unity3d.com/subscriptions/"
    btn_immediate_cancel_locator = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div/a[1]")
    div_choose_cancel_reason_locator = (By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/u-select/div/div[1]/div[1]")
    div_choose_cancel_reason_1_locator = (By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/u-select/div/div[2]/div[3]/div[1]")
    btn_confirm_locator = (By.XPATH, "/html/body/div[5]/div/div[3]/button[1]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.div_choose_cancel_reason = None
        self.div_choose_cancel_reason_1 = None
        self.btn_immediate_cancel = self.btn_immediate_cancel_locator
        self.btn_confirm = None
        self.present_locator = self.btn_immediate_cancel_locator


    def init_elements(self):
        super().init_elements()
        self.div_choose_cancel_reason = super().get_element(self.div_choose_cancel_reason_locator)
        self.div_choose_cancel_reason_1 = super().get_element(self.div_choose_cancel_reason_1_locator)
        self.btn_immediate_cancel = super().get_element(self.btn_immediate_cancel_locator)
        self.btn_confirm = super().get_element(self.btn_confirm_locator)
