from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    input_seat_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[1]/div[2]/div[4]/div[1]/div/input")
    div_monthly_pay_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[1]/div[2]/div[4]/div[3]/div/div[2]")
    btn_purchase_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[1]/div[2]/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.input_seat_locator
        self.input_seat = None
        self.div_monthly_pay = None
        self.btn_purchase = None


    def init_elements(self):
        super().init_elements()
        self.input_seat = super().get_element(self.input_seat_locator)
        self.div_monthly_pay = super().get_element(self.div_monthly_pay_locator)
        self.btn_purchase = super().get_element(self.btn_purchase_locator)
