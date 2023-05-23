from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    div_2_seat_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div[2]")
    div_prepaidPlus_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]")
    div_monthlyPlus_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/span[1]")
    div_monthlyPro_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[3]/div")
    div_1year_prepaid_Pro_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[1]")
    div_2year_prepaid_Pro_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/p[5]")
    div_1year_monthly_Pro_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[3]/div")
    btn_purchase_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[3]/div[2]/a")
    btn_change_currency_locator = (By.XPATH, "//*[@id=\"master-wrapper\"]/div/footer/div[1]/div/div/div[2]/div[1]/div")
    div_currency_CNY_locator = (By.XPATH, "//*[@id=\"master-wrapper\"]/div/footer/div[1]/div/div/div[2]/div[1]/ul/li[2]/a")
    div_currency_JPY_locator = (By.XPATH, "//*[@id=\"master-wrapper\"]/div/footer/div[1]/div/div/div[2]/div[1]/ul/li[3]/a")
    div_currency_KRW_locator = (By.XPATH, "//*[@id=\"master-wrapper\"]/div/footer/div[1]/div/div/div[2]/div[1]/ul/li[4]/a")
    div_productReminder_continue_locator = (By.XPATH, "//*[@id=\"produt_reminder\"]/div/section/div[2]/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.div_2_seat = None
        self.div_prepaidPlus = None
        self.div_monthlyPlus = None
        self.div_monthlyPro = None
        self.div_1year_prepaid_Pro = None
        self.div_2year_prepaid_Pro = None
        self.div_1year_monthly_Pro = None
        self.btn_purchase = None
        self.present_locator = self.div_2_seat_locator
        self.btn_change_currency = self.btn_change_currency_locator
        self.div_currency_CNY = None
        self.div_currency_JPY = None
        self.div_currency_KRW = None
        self.div_productReminder_continue = None

    def init_elements(self):
        super().init_elements()
        self.div_2_seat = super().get_element(self.div_2_seat_locator)
        self.div_prepaidPlus = super().get_element(self.div_prepaidPlus_locator)
        self.div_monthlyPlus = super().get_element(self.div_monthlyPlus_locator)
        self.div_monthlyPro = super().get_element(self.div_monthlyPro_locator)
        self.div_1year_prepaid_Pro = super().get_element(self.div_1year_prepaid_Pro_locator)
        self.div_2year_prepaid_Pro = super().get_element(self.div_2year_prepaid_Pro_locator)
        self.div_1year_monthly_Pro = super().get_element(self.div_1year_monthly_Pro_locator)
        self.btn_purchase = super().get_element(self.btn_purchase_locator)
        self.btn_change_currency = super().get_element(self.btn_change_currency_locator)
        self.div_currency_CNY = super().get_element(self.div_currency_CNY_locator)
        self.div_currency_JPY = super().get_element(self.div_currency_JPY_locator)
        self.div_currency_KRW = super().get_element(self.div_currency_KRW_locator)
        self.div_productReminder_continue = super().get_element(self.div_productReminder_continue_locator)
