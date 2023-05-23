from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://store-staging.unity.com/"
    checkbox_terms_locator = (By.ID, "order_terms")
    btn_pay_now_locator = (By.XPATH, "//*[@id=\"pay-button-area\"]/button")
    div_copy_from_org_address_locator = (By.XPATH, "//*[@id=\"billing-address\"]/div/div[1]/span")
    btn_pay_now_from_id_locator = (By.XPATH, "//*[@id=\"submit\"]")
    btn_select_org_locator = (By.XPATH, "//*[@id=\"org-18966698513222\"]/a")
    input_cc_number_locator = (By.ID, "cardnr")
    div_cc_month_locator = (By.XPATH, "//*[@id=\"method-creditcard\"]/div/div[2]/dl[1]/dd[1]/div[1]/span/span[1]/span/span[2]")
    div_cc_month_1_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[2]")
    div_cc_year_locator = (By.XPATH, "//*[@id=\"method-creditcard\"]/div/div[2]/dl[1]/dd[1]/div[2]/span/span[1]/span/span[2]")
    div_cc_year_2022_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[4]")
    input_cc_cvc_locator = (By.ID, "cvc")
    input_cc_name_locator = (By.ID, "name")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.present_locator = self.btn_pay_now_from_id_locator
        self.checkbox_terms = self.checkbox_terms_locator
        self.btn_pay_now = self.btn_pay_now_locator
        self.div_copy_from_org_address = self.div_copy_from_org_address_locator
        self.btn_pay_now_from_id = None
        self.btn_select_org = None
        self.input_cc_number = None
        self.div_cc_month = self.div_cc_month_locator
        self.div_cc_month_1 = None
        self.div_cc_year = self.div_cc_year_locator
        self.div_cc_year_2022 = None
        self.input_cc_cvc = self.input_cc_cvc_locator
        self.input_cc_name = self.input_cc_name_locator


    def init_elements(self):
        super().init_elements()
        self.btn_agree_continue = super().get_element(self.checkbox_terms_locator)
        self.btn_pay_now = super().get_element(self.btn_pay_now_locator)
        self.div_copy_from_org_address = super().get_element(self.div_copy_from_org_address_locator)
        self.btn_pay_now_from_id = super().get_element(self.btn_pay_now_from_id_locator)
        self.btn_select_org = super().get_element(self.btn_select_org_locator)
        self.input_cc_number = super().get_element(self.input_cc_number_locator)
        self.div_cc_month = super().get_element(self.div_cc_month_locator)
        self.div_cc_month_1 = super().get_element(self.div_cc_month_1_locator)
        self.div_cc_year = super().get_element(self.div_cc_year_locator)
        self.div_cc_year_2022 = super().get_element(self.div_cc_year_2022_locator)
        self.input_cc_cvc = super().get_element(self.input_cc_cvc_locator)
        self.input_cc_name = super().get_element(self.input_cc_name_locator)