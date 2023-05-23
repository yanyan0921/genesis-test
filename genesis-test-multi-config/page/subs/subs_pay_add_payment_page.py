from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_select_cc_locator = (By.XPATH, "/html/body/div[3]/section/div[3]/div/div[1]/div[2]/div/form/div/div/section/div[2]/div[2]/div[1]/dl[2]/dt/div/label")
    input_cc_number_locator = (By.ID, "cardnr")
    input_cc_name_locator = (By.ID, "name")
    btn_cc_month_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[2]/dl[1]/dd[1]/div[1]/span/span[1]/span/span[2]")
    div_cc_month_4_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[5]")
    btn_add_payment_method_locator = (By.XPATH, "//*[@id=\"pay-button-area\"]/button")
    btn_cc_year_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[2]/dl[1]/dd[1]/div[2]/span/span[1]/span/span[2]")
    div_cc_year_2022_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[4]")
    input_cc_cvc_locator = (By.ID, "cvc")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.btn_add_payment_method_locator
        self.btn_add_payment_method = self.btn_add_payment_method_locator
        self.btn_select_cc = None
        self.btn_cc_month = self.btn_cc_month_locator
        self.div_cc_month_4 = None
        self.btn_cc_year = self.btn_cc_year_locator
        self.div_cc_year_2022 = None
        self.input_cc_number = self.input_cc_number_locator
        self.input_cc_name = self.input_cc_name_locator
        self.input_cc_cvc = self.input_cc_cvc_locator


    def init_elements(self):
        super().init_elements()
        self.btn_add_payment_method = super().get_element(self.btn_add_payment_method_locator)
        self.btn_select_cc = super().get_element(self.btn_select_cc_locator)
        self.btn_cc_month = super().get_element(self.btn_cc_month_locator)
        self.div_cc_month_4 = super().get_element(self.div_cc_month_4_locator)
        self.btn_cc_year = super().get_element(self.btn_cc_year_locator)
        self.div_cc_year_2022 = super().get_element(self.div_cc_year_2022_locator)
        self.input_cc_number = super().get_element(self.input_cc_number_locator)
        self.input_cc_name = super().get_element(self.input_cc_name_locator)
        self.input_cc_cvc = super().get_element(self.input_cc_cvc_locator)
