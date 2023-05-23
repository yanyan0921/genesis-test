from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    checkbox_terms_locator = (By.ID, "order_terms")
    btn_pay_now_locator = (By.XPATH, "//*[@id=\"pay-button-area\"]/button")
    div_copy_from_org_address_locator = (By.XPATH, "//*[@id=\"billing-address\"]/div/div[1]/span")
    btn_pay_now_from_id_locator = (By.XPATH, "//*[@id=\"submit\"]")
    btn_select_org_locator = (By.XPATH, "//*[@id=\"org-18966698513222\"]/a")
    btn_select_cc_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[2]/dt/div/label")
    btn_select_cc2_locator = (By.XPATH, "/html/body/div[3]/section/div[3]/div/div[1]/div[2]/div[2]/form/div/div/section/div[2]/div[2]/div[1]/dl[2]/dt/div/label")
    input_cc_number_locator = (By.ID, "cardnr")
    div_cc_month_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[2]/dl[1]/dd[1]/div[1]/div/button")
    div_expiry_month_locator = (By.XPATH, "/html/body/div[3]/section/div[3]/div/div[1]/div[2]/div[2]/form/div/div/section/div[2]/div[2]/div[2]/div[2]/dl[1]/dd[1]/div[1]/span/span[1]/span/span[1]")
    div_expiry_month_1_locator = (By.XPATH, "/html/body/span/span/span[2]/ul/li[2]")
    div_expiry_year_locator = (By.XPATH, "/html/body/div[3]/section/div[3]/div/div[1]/div[2]/div[2]/form/div/div/section/div[2]/div[2]/div[2]/div[2]/dl[1]/dd[1]/div[2]/span/span[1]/span/span[1]")
    div_expiry_year_1_locator = (By.XPATH, "/html/body/span/span/span[2]/ul/li[4]")

    btn_to_change_org_locator = (By.XPATH, "//*[@id=\"step1\"]/div[1]/div[2]/p/a")

    div_cc_month_1_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[2]/dl[1]/dd[1]/div[1]/div/div/ul/li[2]")
    div_cc_year_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[2]/dl[1]/dd[1]/div[2]/div/button")
    div_cc_year_2022_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[2]/dl[1]/dd[1]/div[2]/div/div/ul/li[5]")
    input_cc_cvc_locator = (By.ID, "cvc")
    input_cc_name_locator = (By.ID, "name")
    radio_no_po_number_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[1]/dl/dd/div[2]/label")
    radio_yes_po_number_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[1]/dl/dd/div[1]/label")
    input_po_number_locator = (By.XPATH, "//*[@id=\"poNumber\"]")
    btn_country_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[1]/dd[1]/div/button")
    div_country_germany_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[1]/dd[1]/div/div/ul/li[8]")
    div_country_brazil_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[1]/dd[1]/div/div/ul/li[3]")
    div_country_japan_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[1]/dd[1]/div/div/ul/li[10]")
    div_country_china_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[1]/dd[1]/div/div/ul/li[6]")

    btn_province_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[2]/dd[1]/div/button")
    div_province_hongkong_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[2]/dd[1]/div/div/ul/li[14]")
    input_vatNumber_locator = (By.CSS_SELECTOR,"[class='vat req c720 c721']")
    input_firstname_locator = (By.NAME, "sta[firstName]")
    input_lastname_locator = (By.NAME, "sta[lastName]")
    input_email_locator = (By.NAME, "sta[email]")
    input_phone_locator = (By.NAME, "sta[phoneNumber]")
    input_address_locator = (By.NAME, "sta[streetAddress]")
    input_postalCode_locator = (By.NAME, "sta[postalCode]")
    input_city_locator = (By.NAME, "sta[locality]")
    radio_no_vat_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[7]/dl/dd[1]/div[2]/div[2]")
    radio_yes_vat_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[7]/dl/dd[1]/div[2]/div[1]")
    btn_currency_locator = (By.CSS_SELECTOR, "#master-wrapper > footer > div.store-footer.bg-lg > div > div.g3.right > div.currency_div > div > button")
    div_currency_EUR_locator = (By.XPATH, "//*[@id=\"master-wrapper\"]/footer/div[1]/div/div[1]/div[2]/div/div/ul/li[5]")
    div_currency_CNY_locator = (By.XPATH, "//*[@id=\"master-wrapper\"]/footer/div[1]/div/div[1]/div[2]/div/div/ul/li[2]")
    input_couponCode_locator = (By.XPATH, "//*[@id=\"summary-right\"]/div/div[2]/dl/dd[1]/input")
    btn_couponCode_locator = (By.XPATH, "//*[@id=\"summary-right\"]/div/div[2]/dl/dd[1]/button")
    radio_alipay_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[1]/dt/div/label")
    input_alipay_account_locator = (By.XPATH, "//*[@id=\"alipay-account\"]")
    radio_unionPay_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[4]/dt/div/label")
    radio_collectFapiao_locator = (By.XPATH, "//*[@id=\"payment_methods\"]/div[4]/div/label")
    input_fapiao_title_locator = (By.NAME, "fapiao[title]")
    input_fapiao_receiver_locator = (By.NAME, "fapiao[receiver]")
    input_fapiao_phone_locator = (By.NAME, "fapiao[phoneNumber]")
    input_fapiao_address_locator = (By.NAME, "fapiao[shippingAddress]")
    href_add_new_pi_locator = (By.XPATH, "//*[@id=\"payment_methods\"]/div[1]/a")
    div_shadow_locator = (By.CSS_SELECTOR, "#addressApp > div.shadow")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.btn_pay_now_locator
        self.checkbox_terms = self.checkbox_terms_locator
        self.btn_pay_now = self.btn_pay_now_locator
        self.div_copy_from_org_address = self.div_copy_from_org_address_locator
        self.btn_pay_now_from_id = None
        self.btn_select_org = None
        self.btn_to_change_org = None
        self.btn_select_cc = None
        self.btn_select_cc2 = None
        self.input_cc_number = None
        self.div_cc_month = self.div_cc_month_locator
        self.div_cc_month_1 = None
        self.div_expiry_month = self.div_cc_month_locator
        self.div_expiry_1 = None
        self.div_expiry_year = self.div_expiry_year_locator
        self.div_expiry_year_1 = None
        self.div_cc_year = self.div_cc_year_locator
        self.div_cc_year_2022 = None
        self.input_cc_cvc = self.input_cc_cvc_locator
        self.input_cc_name = self.input_cc_name_locator
        self.radio_no_po_number = None
        self.radio_yes_po_number = None
        self.btn_country = self.btn_country_locator
        self.div_country_germany = None
        self.div_country_brazil = None
        self.div_country_japan = None
        self.div_country_china = None
        self.btn_province = None
        self.div_province_hongkong = None
        self.input_vatNumber = None
        self.input_po_number = None
        self.input_firstname = self.input_firstname_locator
        self.input_lastname = self.input_lastname_locator
        self.input_email = self.input_email_locator
        self.input_address = self.input_address_locator
        self.input_phone = self.input_phone_locator
        self.input_postalCode = self.input_postalCode_locator
        self.input_city = self.input_city_locator

        self.radio_no_vat = None
        self.radio_yes_vat = None
        self.btn_currency = self.btn_currency_locator
        self.div_currency_EUR = self.div_currency_EUR_locator
        self.div_currency_CNY = None
        self.input_couponCode = self.input_couponCode_locator
        self.btn_couponCode = self.btn_couponCode_locator

        self.radio_alipay = None
        self.input_alipay_account = None
        self.radio_unionPay = None
        self.radio_collectFapiao = None
        self.input_fapiao_title = None
        self.input_fapiao_receiver = None
        self.input_fapiao_phone = None
        self.input_fapiao_address = None
        self.href_add_new_pi = None

    def init_elements(self):
        super().init_elements()
        super().wait_for_element_hidden(self.div_shadow_locator)
        self.btn_agree_continue = super().get_element(self.checkbox_terms_locator)
        self.btn_pay_now = super().get_element(self.btn_pay_now_locator)
        self.div_copy_from_org_address = super().get_element(self.div_copy_from_org_address_locator)
        self.btn_pay_now_from_id = super().get_element(self.btn_pay_now_from_id_locator)
        self.btn_select_org = super().get_element(self.btn_select_org_locator)
        self.btn_to_change_org = super().get_element(self.btn_to_change_org_locator)
        self.btn_select_cc = super().get_element(self.btn_select_cc_locator)
        self.btn_select_cc2 = super().get_element(self.btn_select_cc2_locator)
        self.input_cc_number = super().get_element(self.input_cc_number_locator)
        self.div_cc_month = super().get_element(self.div_cc_month_locator)
        self.div_cc_month_1 = super().get_element(self.div_cc_month_1_locator)
        self.div_cc_year = super().get_element(self.div_cc_year_locator)
        self.div_cc_year_2022 = super().get_element(self.div_cc_year_2022_locator)
        self.div_expiry_month = super().get_element(self.div_expiry_month_locator)
        self.div_expiry_month_1 = super().get_element(self.div_expiry_month_1_locator)
        self.div_expiry_year = super().get_element(self.div_expiry_year_locator)
        self.div_expiry_year_1 = super().get_element(self.div_expiry_year_1_locator)
        self.input_cc_cvc = super().get_element(self.input_cc_cvc_locator)
        self.input_cc_name = super().get_element(self.input_cc_name_locator)
        self.radio_no_po_number = super().get_element(self.radio_no_po_number_locator)
        self.radio_yes_po_number = super().get_element(self.radio_yes_po_number_locator)
        self.btn_country = super().get_element(self.btn_country_locator)
        self.div_country_germany = super().get_element(self.div_country_germany_locator)
        self.div_country_brazil = super().get_element(self.div_country_brazil_locator)
        self.div_country_japan = super().get_element(self.div_country_japan_locator)
        self.div_country_china = super().get_element(self.div_country_china_locator)
        self.btn_province = super().get_element(self.btn_province_locator)
        self.div_province_hongkong = super().get_element(self.div_province_hongkong_locator)
        self.input_vatNumber = super().get_element(self.input_vatNumber_locator)
        self.input_po_number = super().get_element(self.input_po_number_locator)
        self.input_firstname = super().get_element(self.input_firstname_locator)
        self.input_lastname = super().get_element(self.input_lastname_locator)
        self.input_phone = super().get_element(self.input_phone_locator)
        self.input_address = super().get_element(self.input_address_locator)
        self.input_email = super().get_element(self.input_email_locator)
        self.input_postalCode = super().get_element(self.input_postalCode_locator)
        self.input_city = super().get_element(self.input_city_locator)
        self.radio_no_vat = super().get_element(self.radio_no_vat_locator)
        self.radio_yes_vat = super().get_element(self.radio_yes_vat_locator)
        self.btn_currency = super().get_element(self.btn_currency_locator)
        self.div_currency_EUR = super().get_element(self.div_currency_EUR_locator)
        self.div_currency_CNY = super().get_element(self.div_currency_CNY_locator)
        self.input_couponCode = super().get_element(self.input_couponCode_locator)
        self.btn_couponCode = super().get_element(self.btn_couponCode_locator)
        self.radio_alipay = super().get_element(self.radio_alipay_locator)
        self.input_alipay_account = super().get_element(self.input_alipay_account_locator)
        self.radio_unionPay = super().get_element(self.radio_unionPay_locator)
        self.radio_collectFapiao = super().get_element(self.radio_collectFapiao_locator)
        self.input_fapiao_title = super().get_element(self.input_fapiao_title_locator)
        self.input_fapiao_receiver = super().get_element(self.input_fapiao_receiver_locator)
        self.input_fapiao_phone = super().get_element(self.input_fapiao_phone_locator)
        self.input_fapiao_address = super().get_element(self.input_fapiao_address_locator)
        self.href_add_new_pi = super().get_element(self.href_add_new_pi_locator)

