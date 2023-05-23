from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-staging.unity.com/en/subscriptions"
    btn_upgrade_plan_locator = (By.LINK_TEXT, "Upgrade plan")
    btn_upgrade_plan2_locator = (By.XPATH, "/html/body/div[1]/div/section/div[1]/section[2]/div/div/div[1]/div/div/div[2]/a[1]")
    btn_upgrade_plan3_locator = (By.XPATH, "//*[@id=\"seat-assignment-vue-app\"]/div[2]/div[2]/div[3]/div/div[2]/a")
    btn_pay_for_remaining_locator = (By.XPATH, "//*[@id=\"content-wrapper\"]/div[1]/div[2]/div[2]/div[3]/div/div[2]/a")
    #btn_pay_for_remaining_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div[1]/div[3]/div[2]/div[3]/div/div[2]/a")
    #btn_confirm_purchase_locator = (By.XPATH, "//*[@id=\"new_prepay_subscription_form\"]/div/div[3]/div/input")
    btn_confirm_purchase_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div/form/div/div[3]/div/input")
    div_transaction_history_locator = (By.LINK_TEXT, "Transaction History")
    div_pay_now_locator = (By.LINK_TEXT, "Pay now")
    href_payment_methods_locator = (By.LINK_TEXT, "Payment Methods")
    label_last_payment_status_locator = (By.XPATH, "//*[@id=\"content-wrapper\"]/div/div[3]/div[4]/table/tbody/tr[1]/td[4]")
    # div_pay_remaining_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div[1]/div[3]/div[2]/div[3]/div/div[2]/a")
    div_pay_remaining_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/a")

    # btn_add_seat_locator = (By.XPATH, "/html/body/div/section/div[3]/div/div[1]/div[4]/div/ul/li[2]/a")
    btn_add_seat_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div[1]/div[3]/div/ul/li[2]/a")
    # btn_pay_add_seat_locator = (By.XPATH, "/html/body/div/section/div[3]/div/div/div[4]/div/form/div/div/div[2]/div/div[3]/input")
    btn_pay_add_seat_locator = (By.XPATH, "//*[@id=\"page-bottom\"]/input")
    # btn_purchase_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div/div[2]/div[3]/div/form/input[7]")
    btn_purchase_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div/div[2]/div[3]/div/form/input[7]")

    btn_remaining_pay_locator = (By.XPATH, "/html/body/div/section/div[3]/div/div/div[2]/div[2]/div[3]/div/div[2]/a")

    # btn_mgr_subs_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div[1]/div[4]/div/ul/li[5]/a")
    btn_mgr_subs_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div[1]/div[4]/div/ul/li[5]/a")
    # btn_renewal_options_locator = (By.XPATH, "/html/body/div/section/div[3]/div/div/div[4]/div/form/div/div/div[4]/div[2]/div/div[3]/div[2]/div[2]/div")
    btn_renewal_options_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div/div[3]/div/form/div/div/div[3]/div[2]/div/label")
    # btn_renewal_next_locator = (By.XPATH, "/html/body/div/section/div[3]/div/div/div[4]/div/form/div/div/div[6]/div/input")
    btn_renewal_next_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div/div[3]/div/form/div/div/div[10]/div/input")
    btn_renewal_purchase_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div/form/div/div[3]/div/input")
    btn_renewal_cancel_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div/div[3]/div/div/div/div/div/p/a[2]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_upgrade_plan = self.btn_upgrade_plan_locator
        self.btn_upgrade_plan2 = None
        self.btn_upgrade_plan3 = None
        self.btn_pay_for_remaining = None
        self.btn_confirm_purchase = None
        self.present_locator = self.div_transaction_history_locator
        self.div_transaction_history = self.div_transaction_history_locator
        self.div_pay_now = None
        self.href_payment_methods = self.href_payment_methods_locator
        self.label_last_payment_status = None
        self.div_pay_remaining = None
        self.btn_add_seat = None
        self.btn_pay_add_seat = None
        self.btn_purchase = None

        self.btn_mgr_subs = None
        self.btn_renewal_options = None
        self.btn_renewal_next = None
        self.btn_renewal_purchase = None
        self.btn_renewal_cancel = None

    def init_elements(self):
        super().init_elements()
        self.btn_upgrade_plan = super().get_element(self.btn_upgrade_plan_locator)
        self.btn_upgrade_plan2 = super().get_element(self.btn_upgrade_plan2_locator)
        self.btn_upgrade_plan3 = super().get_element(self.btn_upgrade_plan3_locator)
        self.btn_pay_for_remaining = super().get_element(self.btn_pay_for_remaining_locator)
        self.btn_confirm_purchase = super().get_element(self.btn_confirm_purchase_locator)
        self.div_transaction_history = super().get_element(self.div_transaction_history_locator)
        self.div_pay_now = super().get_element(self.div_pay_now_locator)
        self.href_payment_methods = super().get_element(self.href_payment_methods_locator)
        self.label_last_payment_status = super().get_element(self.label_last_payment_status_locator)
        self.div_pay_remaining = super().get_element(self.div_pay_remaining_locator)
        self.btn_add_seat = super().get_element(self.btn_add_seat_locator)
        self.btn_pay_add_seat = super().get_element(self.btn_pay_add_seat_locator)
        self.btn_purchase = super().get_element(self.btn_purchase_locator)

        self.btn_mgr_subs = super().get_element(self.btn_mgr_subs_locator)
        self.btn_renewal_options = super().get_element(self.btn_renewal_options_locator)
        self.btn_renewal_next = super().get_element(self.btn_renewal_next_locator)
        self.btn_renewal_purchase = super().get_element(self.btn_renewal_purchase_locator)
        self.btn_renewal_cancel = super().get_element(self.btn_renewal_cancel_locator)