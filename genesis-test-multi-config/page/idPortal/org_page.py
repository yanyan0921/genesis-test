from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-staging.unity.com/en/organizations/subsuitest"
    div_transaction_history_locator = (By.LINK_TEXT, "Transaction History")
    href_payment_methods_locator = (By.LINK_TEXT, "Payment Methods")
    btn_add_payment_method_locator = (By.XPATH, "//*[@id=\"content-wrapper\"]/div/div[2]/div[1]/div/a")
    btn_continue_locator = (By.CSS_SELECTOR, "#new_shipping_address > div.block-footer > input")
    label_new_card_info_locator = (By.XPATH, "//*[@id=\"content-wrapper\"]/div/div[2]/div[2]/div[1]/div[2]")
    href_delete_first_pi_locator = (By.XPATH, "//*[@id=\"content-wrapper\"]/div/div[2]/div[2]/div[1]/div[3]/a[1]")
    href_remove_pi_locator = (By.XPATH, "//*[@id=\"alert-remove-pi\"]/a[1]")
    btn_country_locator = (By.XPATH, "//*[@id=\"billing-address\"]/div[13]/div/button")
    div_country_brazil_locator = (By.XPATH, "//*[@id=\"billing-address\"]/div[13]/div/div/ul/li[2]/a")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.present_locator = self.div_transaction_history_locator
        self.div_transaction_history = self.div_transaction_history_locator
        self.href_payment_methods = self.href_payment_methods_locator
        self.btn_add_payment_method = None
        self.btn_continue = None
        self.label_new_card_info = None
        self.href_delete_first_pi = None
        self.href_remove_pi = None
        self.btn_country = None
        self.div_country_brazil = None

    def init_elements(self):
        super().init_elements()
        self.div_transaction_history = super().get_element(self.div_transaction_history_locator)
        self.href_payment_methods = super().get_element(self.href_payment_methods_locator)
        self.btn_add_payment_method = super().get_element(self.btn_add_payment_method_locator)
        self.btn_continue = super().get_element(self.btn_continue_locator)
        self.label_new_card_info = super().get_element(self.label_new_card_info_locator)
        self.href_delete_first_pi = super().get_element(self.href_delete_first_pi_locator)
        self.href_remove_pi = super().get_element(self.href_remove_pi_locator)
        self.btn_country = super().get_element(self.btn_country_locator)
        self.div_country_brazil = super().get_element(self.div_country_brazil_locator)
