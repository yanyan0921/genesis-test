from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    div_2_seat_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[2]")
    div_monthly_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]")
    div_unite_trial_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[3]")
    div_1year_prepaid_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]")
    btn_purchase_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[2]/div[2]/a")
    btn_change_currency_locator = (By.XPATH, "//*[@id=\"master-wrapper\"]/div/footer/div[1]/div/div[1]/div[2]")
    div_currency_CNY_locator = (By.XPATH, "//*[@id=\"master-wrapper\"]/div/footer/div[1]/div/div[1]/div[2]/ul/li[2]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.div_2_seat = None
        self.div_monthly = None
        self.div_unite_trial = None
        self.div_1year_prepaid = None
        self.btn_purchase = None
        self.present_locator = self.div_2_seat_locator
        self.btn_change_currency = self.btn_change_currency_locator
        self.div_currency_CNY = None

    def init_elements(self):
        super().init_elements()
        self.div_2_seat = super().get_element(self.div_2_seat_locator)
        self.div_monthly = super().get_element(self.div_monthly_locator)
        self.div_unite_trial = super().get_element(self.div_unite_trial_locator)
        self.div_1year_prepaid = super().get_element(self.div_1year_prepaid_locator)
        self.btn_purchase = super().get_element(self.btn_purchase_locator)
        self.btn_change_currency = super().get_element(self.btn_change_currency_locator)
        self.div_currency_CNY = super().get_element(self.div_currency_CNY_locator)