from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    input_password_locator = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div/div[1]/div/div/div[2]/div[2]/input")
    btn_express_purchase_locator = (By.CSS_SELECTOR,"[class='_3UE3J _3zD70 auto qsCb9']")
    btn_cancel_locator = (By.XPATH,"/html/body/div[3]/div/div[2]/div/div/div[1]/div/div/div[2]/div[5]/button[1]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.input_password = None
        self.btn_express_purchase = None
        self.present_locator = self.btn_cancel_locator

    def init_elements(self):
        super().init_elements()
        self.input_password = super().get_element(self.input_password_locator)
        self.btn_express_purchase = super().get_element(self.btn_express_purchase_locator)
        self.btn_cancel_locator = super().get_element(self.btn_express_purchase_locator)


