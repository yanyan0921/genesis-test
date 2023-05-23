from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_portal_type_locator = (By.XPATH, "//*[@id=\"testPageApp\"]/form/div/div[2]/div/button")
    btn_go_locator = (By.XPATH, "//*[@id=\"testPageApp\"]/form/div/div[19]/input")
    div_cpq_locator = (By.XPATH, "//*[@id=\"testPageApp\"]/form/div/div[2]/div/div/ul/li[3]")
    btn_cpq_product_name_locator = (By.XPATH, "//*[@id=\"testPageApp\"]/form/div/div[16]/div/button")
    div_cpq_editor_only_locator = (By.XPATH, "//*[@id=\"testPageApp\"]/form/div/div[16]/div/div/ul/li[3]")
    div_cpq_renew_locator = (By.XPATH, "//*[@id=\"testPageApp\"]/form/div/div[16]/div/div/ul/li[11]")
    btn_cpq_payment_method_locator = (By.XPATH, "//*[@id=\"testPageApp\"]/form/div/div[11]/div/button")
    div_cpq_payment_method_CC_locator = (By.XPATH, "//*[@id=\"testPageApp\"]/form/div/div[11]/div/div/ul/li[2]")
    div_online_locator = (By.XPATH, "//*[@id=\"testPageApp\"]/form/div/div[2]/div/div/ul/li[2]/a/span[1]")
    btn_subscription_name_locator = (By.XPATH, "//*[@id=\"testPageApp\"]/form/div/div[14]/span/span[1]/span/span[2]")
    div_unity_reflect_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul/li[10]")
    div_learn_premium_prepaid_locator = (By.XPATH,"//*[@id=\"testPageApp\"]/form/div/div[14]/div/div/ul/li[20]/a/span[1]")
    input_amount_locator = (By.XPATH, "//*[@id=\"testPageApp\"]/form/div/div[5]/input")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_portal_type = self.btn_portal_type_locator
        self.btn_go = self.btn_go_locator
        self.present_locator = self.btn_go_locator
        self.div_cpq = None
        self.div_online = None
        self.input_amount = None
        self.btn_subscription_name = None
        self.btn_cpq_product_name = None
        self.div_cpq_editor_only = None
        self.div_unity_reflect = None
        self.div_learn_premium_prepaid = None
        self.div_cpq_renew = None
        self.btn_cpq_payment_method = None
        self.div_cpq_payment_method_CC = None

    def init_elements(self):
        super().init_elements()
        self.btn_portal_type = super().get_element(self.btn_portal_type_locator)
        self.btn_go = super().get_element(self.btn_go_locator)
        self.div_cpq = super().get_element(self.div_cpq_locator)
        self.div_online = super().get_element(self.div_online_locator)
        self.btn_subscription_name = super().get_element(self.btn_subscription_name_locator)
        self.btn_cpq_product_name = super().get_element(self.btn_cpq_product_name_locator)
        self.div_cpq_editor_only = super().get_element(self.div_cpq_editor_only_locator)
        self.div_unity_reflect = super().get_element(self.div_unity_reflect_locator)
        self.div_learn_premium_prepaid = super().get_element(self.div_learn_premium_prepaid_locator)
        self.div_cpq_renew = super().get_element(self.div_cpq_renew_locator)
        self.btn_cpq_payment_method = super().get_element(self.btn_cpq_payment_method_locator)
        self.div_cpq_payment_method_CC = super().get_element(self.div_cpq_payment_method_CC_locator)
        self.input_amount = super().get_element(self.input_amount_locator)

