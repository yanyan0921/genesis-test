from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_accept_locator = (By.XPATH, "//*[@id=\"onetrust-accept-btn-handler\"]")
    btn_cookie_locator = (By.XPATH, "//*[@id=\"produt_reminder\"]/div/section/div[2]/button")
    checkbox_terms_locator = (By.ID, "order_terms")
    checkbox_terms_paypal_locator = (By.XPATH, "/html/body/div[3]/section/div[3]/div/div[1]/div[2]/div[2]/form/div/div/div[4]/div[1]/div/label")
    checkbox_learn_premium_locator = (By.ID, "learnSubscribed")
    btn_pay_now_locator = (By.XPATH, "//*[@id=\"pay-button-area\"]/button")
    btn_pay_now_paypal_locator = (By.XPATH, "/html/body/div[3]/section/div[3]/div/div[1]/div[2]/div[2]/form/div/div/div[4]/div[3]/button")
    div_copy_from_org_address_locator = (By.XPATH, "//*[@id=\"billing-address\"]/div/div[1]/span")
    btn_pay_now_from_id_locator = (By.XPATH, "//*[@id=\"submit\"]")
    btn_select_org_locator = (By.XPATH, "//*[@id=\"org-18966698513222\"]/a")
    btn_select_cc_locator = (By.XPATH,"/html/body/div[3]/section/div[3]/div/div[1]/div[4]/div[2]/form/div/div/section/div[2]/div[2]/div[1]/dl[3]/dt/div/label")
    btn_select_cc2_locator = (By.XPATH,"/html/body/div[3]/section/div[3]/div/div[1]/div[4]/div[2]/form/div/div/section/div[2]/div[2]/div[1]/dl[2]/dt/div/label")
    btn_select_paypal_locator = (By.XPATH,"")
    input_cc_number_locator = (By.ID, "cardnr")
    input_paypal_email_locator = (By.ID, "paypal-email")
    input_purchase_order_number_locator = (By.ID, "poNumber")
    div_cc_month_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[2]/dl[1]/dd[1]/div[1]/span/span[1]/span/span[2]")

    div_cc_month_1_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[2]")
    div_cc_year_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[2]/dl[1]/dd[1]/div[2]/span/span[1]/span/span[2]")
    div_cc_year_2022_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[4]")
    input_cc_cvc_locator = (By.ID, "cvc")
    input_cc_name_locator = (By.ID, "name")
    radio_no_po_number_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[1]/dl/dd/div[2]/label")
    radio_yes_po_number_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[1]/dl/dd/div[1]/label")
    btn_country_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[1]/dd[1]/span/span[1]/span/span[2]")
    div_country_germany_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[85]")
    div_country_mexico_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[140]")
    div_country_brazil_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[30]")
    div_country_japan_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[111]")
    div_country_china_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[49]")
    div_country_hongkong_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[47]")
    div_country_macao_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[48]")
    div_country_southkorea_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[202]")
    div_country_india_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[103]")
    div_cc_year_2023_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[5]")
    div_country_usa_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[232]")
    div_states_California_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[10]")
    btn_province_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[2]/dd[1]/span/span[1]/span/span[2]")
    div_province_anhui_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[13]")
    div_province_india_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[23]")
    input_vatNumber_locator = (By.CSS_SELECTOR, "[class='vat req c720 c721']")
    input_firstname_locator = (By.NAME, "sta[firstName]")
    input_lastname_locator = (By.NAME, "sta[lastName]")
    input_email_locator = (By.NAME, "sta[email]")
    input_phone_locator = (By.NAME, "sta[phoneNumber]")

    btn_send_sms_code_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[4]/dl[1]/dd[1]/button")
    input_sms_code_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[4]/dl[2]/dd[1]/input")
    btn_verify_sms_code_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[4]/dl[2]/dd[1]/button")

    input_address_locator = (By.NAME, "sta[streetAddress]")
    input_postalCode_locator = (By.NAME, "sta[postalCode]")
    input_city_locator = (By.NAME, "sta[locality]")
    btn_taxno_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[7]/dl/dd[1]/div[2]/div[2]/label")
    radio_no_vat_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[7]/dl/dd[1]/div[2]/div[2]")
    radio_yes_vat_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[7]/dl/dd[1]/div[2]/div[1]")
    btn_currency_locator = (By.XPATH, "//*[@id=\"currency_switcher\"]/span/span[1]/span/span[2]")
    div_currency_EUR_locator = (By.XPATH, "//div/footer[1]/div[1]/div[1]/div[1]/div[2]/span[2]/span[1]/span[2]/ul//li[5]")
    div_currency_CNY_locator = (By.XPATH, "//div/footer[1]/div[1]/div[1]/div[1]/div[2]/span[2]/span[1]/span[2]/ul//li[2]")
    div_currency_USD_locator = (By.XPATH, "//div/footer[1]/div[1]/div[1]/div[1]/div[2]/span[2]/span[1]/span[2]/ul//li[6]")
    input_couponCode_locator = (By.XPATH, "//*[@id=\"summary-right\"]/div/div[2]/dl/dd[1]/input")
    btn_couponCode_locator = (By.XPATH, "//*[@id=\"summary-right\"]/div/div[2]/dl/dd[1]/button")
    radio_alipay_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[1]/dt/div/label")
    input_alipay_account_locator = (By.XPATH, "//*[@id=\"alipay-account\"]")
    radio_unionPay_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[5]/dt/div/label")
    radio_btbTransfer_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[2]/dt/div/label")
    radio_btcreditTransfer_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[1]/dt/div/label")
    radio_btbTransfer_KRW_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[3]/dt/div/label")
    radio_China_btbTransfer_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[4]/dt/div[1]/label/span")
    radio_invoicePayment_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[2]/dt/div[1]/label")
    radio_haveQuote_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[3]/dt/div[2]/div[2]/label")
    radio_weChat_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[1]/dl[2]/dt/div/label")
    radio_collectFapiao_locator = (By.XPATH, "//*[@id=\"payment_methods\"]/div[4]/div/label")

    div_fapiaoType_locator = (By.XPATH, "//*[@id=\"fapiao_form\"]/div[2]/dl/dd/span/span[1]/span/span[2]")
    div_companyGeneralVATFapiao_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[2]")
    div_companySpecialVATFapiao_locator = (By.XPATH, "//span[1]/span[1]/span[2]/ul[1]/li[3]")

    input_fapiao_receiver_locator = (By.NAME, "fapiao[receiver]")
    input_fapiao_phone_locator = (By.NAME, "fapiao[phoneNumber]")
    input_fapiao_address_locator = (By.NAME, "fapiao[shippingAddress]")
    input_fapiao_firstName_locator = (By.NAME, "fapiao[firstName]")
    input_fapiao_lastName_locator = (By.NAME, "fapiao[lastName]")

    input_fapiao_receive_email_locator = (By.NAME, "fapiao[email]")
    input_fapiao_companyName_locator = (By.NAME, "fapiao[title]")
    input_fapiao_registrationNo_locator = (By.NAME, "fapiao[taxIdentifier]")
    input_fapiao_bankName_locator = (By.NAME, "fapiao[bankName]")
    input_fapiao_accountNo_locator = (By.NAME, "fapiao[bankNumber]")
    input_fapiao_telephone_locator = (By.NAME, "fapiao[companyPhoneNumber]")
    input_fapiao_companyAddress_locator = (By.NAME, "fapiao[companyAddress]")

    href_add_new_pi_locator = (By.XPATH, "//*[@id=\"payment_methods\"]/div[1]/a")
    div_shadow_locator = (By.CSS_SELECTOR, "#addressApp > div.shadow")
    div_add_payment_locator = (By.XPATH, "//*[@id=\"step1\"]/div[3]/div/label")

    radio_cc_pay_locator = (By.XPATH, "/html/body/div[3]/section/div[3]/div/div[1]/div[2]/div[2]/form/div/div/section/div[2]/div[2]/div[1]/dl[2]/dt/div/label")
    input_country_locator = (By.XPATH, "/html/body/span/span/span[1]/input")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_accept = self.btn_accept_locator
        self.btn_cookie = self.btn_cookie_locator
        self.present_locator = self.btn_pay_now_locator
        self.checkbox_terms = self.checkbox_terms_locator
        self.checkbox_terms_paypal = None
        self.checkbox_learn_premium = None
        self.btn_pay_now = self.btn_pay_now_locator
        self.btn_pay_now_paypal = None
        self.div_copy_from_org_address = self.div_copy_from_org_address_locator
        self.btn_pay_now_from_id = None
        self.btn_select_org = None
        self.btn_select_cc = None
        self.btn_select_cc2 = None
        self.input_cc_number = None
        self.input_purchase_order_number = None
        self.div_cc_month = self.div_cc_month_locator
        self.div_cc_month_1 = None
        self.div_cc_year = self.div_cc_year_locator
        self.div_cc_year_2022 = None
        self.input_cc_cvc = self.input_cc_cvc_locator
        self.input_cc_name = self.input_cc_name_locator
        self.radio_no_po_number = None
        self.radio_yes_po_number = None
        self.btn_country = self.btn_country_locator
        self.div_country_germany = None
        self.div_country_mexico = None
        self.div_country_brazil = None
        self.div_country_japan = None
        self.div_country_china = None
        self.div_country_hongkong = None
        self.div_country_macao = None
        self.div_country_southkorea = None
        self.div_country_india = None
        self.btn_province = None
        self.div_province_anhui = None
        self.div_province_india = None
        self.input_vatNumber = None
        self.input_firstname = self.input_firstname_locator
        self.input_lastname = self.input_lastname_locator
        self.input_email = self.input_email_locator
        self.input_address = self.input_address_locator
        self.input_phone = self.input_phone_locator
        self.input_sms_code = self.input_sms_code_locator
        self.input_postalCode = self.input_postalCode_locator
        self.input_city = self.input_city_locator
        self.input_paypal_email = None
        self.btn_taxno = self.btn_taxno_locator
        self.btn_send_sms_code = self.btn_send_sms_code_locator
        self.btn_verify_sms_code = self.btn_verify_sms_code_locator

        self.radio_no_vat = None
        self.radio_yes_vat = None
        self.btn_currency = self.btn_currency_locator
        self.div_currency_EUR = self.div_currency_EUR_locator
        self.div_currency_CNY = None
        self.div_currency_USD = None
        self.input_couponCode = self.input_couponCode_locator
        self.btn_couponCode = self.btn_couponCode_locator

        self.radio_alipay = None
        self.input_alipay_account = None
        self.radio_unionPay = None
        self.radio_btbTransfer = None
        self.radio_btbTransfer_KRW = None
        self.radio_btcreditTransfer = None
        self.radio_China_btbTransfer = None
        self.radio_invoicePayment = None
        self.radio_haveQuote = None
        self.radio_weChat = None
        self.radio_collectFapiao = None
        self.div_fapiaoType = None
        self.div_companyGeneralVATFapiao = None
        self.div_companySpecialVATFapiao = None
        self.input_fapiao_receiver = None
        self.input_fapiao_phone = None
        self.input_fapiao_address = None
        self.input_fapiao_firstName = None
        self.input_fapiao_lastName = None
        self.input_fapiao_receive_email = None
        self.input_fapiao_companyName = None
        self.input_fapiao_registrationNo = None
        self.input_fapiao_bankName = None
        self.input_fapiao_accountNo = None
        self.input_fapiao_telephone = None
        self.input_fapiao_companyAddress = None
        self.div_add_payment = None
        self.href_add_new_pi = None
        self.div_cc_year_2023 = None
        self.div_country_usa = None
        self.div_states_California = None

        self.radio_cc_pay = None
        self.input_country = None

    def init_elements(self):
        super().init_elements()
        super().wait_for_element_hidden(self.div_shadow_locator)
        self.btn_accept = super().get_element(self.btn_accept_locator)
        self.btn_cookie = super().get_element(self.btn_cookie_locator)
        self.btn_agree_continue = super().get_element(self.checkbox_terms_locator)
        self.checkbox_learn_premium = super().get_element(self.checkbox_learn_premium_locator)
        self.checkbox_terms_paypal = super().get_element(self.checkbox_terms_paypal_locator)
        self.btn_pay_now = super().get_element(self.btn_pay_now_locator)
        self.btn_pay_now_paypal = super().get_element(self.btn_pay_now_paypal_locator)
        self.div_copy_from_org_address = super().get_element(self.div_copy_from_org_address_locator)
        self.btn_pay_now_from_id = super().get_element(self.btn_pay_now_from_id_locator)
        self.btn_select_org = super().get_element(self.btn_select_org_locator)
        self.btn_select_cc = super().get_element(self.btn_select_cc_locator)
        self.btn_select_cc2 = super().get_element(self.btn_select_cc2_locator)
        self.input_cc_number = super().get_element(self.input_cc_number_locator)
        self.input_purchase_order_number = super().get_element(self.input_purchase_order_number_locator)
        self.div_cc_month = super().get_element(self.div_cc_month_locator)
        self.div_cc_month_1 = super().get_element(self.div_cc_month_1_locator)
        self.div_cc_year = super().get_element(self.div_cc_year_locator)
        self.div_cc_year_2022 = super().get_element(self.div_cc_year_2022_locator)
        self.input_cc_cvc = super().get_element(self.input_cc_cvc_locator)
        self.input_cc_name = super().get_element(self.input_cc_name_locator)
        self.input_paypal_email = super().get_element(self.input_paypal_email_locator)
        self.radio_no_po_number = super().get_element(self.radio_no_po_number_locator)
        self.radio_yes_po_number = super().get_element(self.radio_yes_po_number_locator)
        self.btn_country = super().get_element(self.btn_country_locator)
        self.div_country_germany = super().get_element(self.div_country_germany_locator)
        self.div_country_mexico = super().get_element(self.div_country_mexico_locator)
        self.div_country_brazil = super().get_element(self.div_country_brazil_locator)
        self.div_country_japan = super().get_element(self.div_country_japan_locator)
        self.div_country_china = super().get_element(self.div_country_china_locator)
        self.div_country_hongkong = super().get_element(self.div_country_hongkong_locator)
        self.div_country_macao = super().get_element(self.div_country_macao_locator)
        self.div_country_southkorea = super().get_element(self.div_country_southkorea_locator)
        self.div_country_india = super().get_element(self.div_country_india_locator)
        self.btn_province = super().get_element(self.btn_province_locator)
        self.div_province_anhui = super().get_element(self.div_province_anhui_locator)
        self.div_province_india = super().get_element(self.div_province_india_locator)
        self.input_vatNumber = super().get_element(self.input_vatNumber_locator)
        self.input_firstname = super().get_element(self.input_firstname_locator)
        self.input_lastname = super().get_element(self.input_lastname_locator)
        self.input_phone = super().get_element(self.input_phone_locator)
        self.input_sms_code = super().get_element(self.input_sms_code_locator)
        self.input_address = super().get_element(self.input_address_locator)
        self.input_email = super().get_element(self.input_email_locator)
        self.input_postalCode = super().get_element(self.input_postalCode_locator)
        self.input_city = super().get_element(self.input_city_locator)
        self.btn_taxno = super().get_element(self.btn_taxno_locator)
        self.btn_send_sms_code = super().get_element(self.btn_send_sms_code_locator)
        self.btn_verify_sms_code = super().get_element(self.btn_verify_sms_code_locator)
        self.radio_no_vat = super().get_element(self.radio_no_vat_locator)
        self.radio_yes_vat = super().get_element(self.radio_yes_vat_locator)
        self.btn_currency = super().get_element(self.btn_currency_locator)
        self.div_currency_EUR = super().get_element(self.div_currency_EUR_locator)
        self.div_currency_CNY = super().get_element(self.div_currency_CNY_locator)
        self.div_currency_USD = super().get_element(self.div_currency_USD_locator)
        self.input_couponCode = super().get_element(self.input_couponCode_locator)
        self.btn_couponCode = super().get_element(self.btn_couponCode_locator)
        self.radio_alipay = super().get_element(self.radio_alipay_locator)
        self.input_alipay_account = super().get_element(self.input_alipay_account_locator)
        self.radio_unionPay = super().get_element(self.radio_unionPay_locator)
        self.radio_btbTransfer = super().get_element(self.radio_btbTransfer_locator)
        self.radio_btbTransfer_KRW = super().get_element(self.radio_btbTransfer_KRW_locator)
        self.radio_btcreditTransfer = super().get_element(self.radio_btcreditTransfer_locator)
        self.radio_China_btbTransfer = super().get_element(self.radio_China_btbTransfer_locator)
        self.radio_invoicePayment = super().get_element(self.radio_invoicePayment_locator)
        self.radio_haveQuote = super().get_element(self.radio_haveQuote_locator)
        self.radio_weChat = super().get_element(self.radio_weChat_locator)
        self.radio_collectFapiao = super().get_element(self.radio_collectFapiao_locator)
        self.div_fapiaoType = super().get_element(self.div_fapiaoType_locator)
        self.div_companyGeneralVATFapiao = super().get_element(self.div_companyGeneralVATFapiao_locator)
        self.div_companySpecialVATFapiao = super().get_element(self.div_companySpecialVATFapiao_locator)
        self.input_fapiao_receiver = super().get_element(self.input_fapiao_receiver_locator)
        self.input_fapiao_phone = super().get_element(self.input_fapiao_phone_locator)
        self.input_fapiao_address = super().get_element(self.input_fapiao_address_locator)
        self.input_fapiao_firstName = super().get_element(self.input_fapiao_firstName_locator)
        self.input_fapiao_lastName = super().get_element(self.input_fapiao_lastName_locator)
        self.input_fapiao_receive_email = super().get_element(self.input_fapiao_receive_email_locator)
        self.input_fapiao_companyName = super().get_element(self.input_fapiao_companyName_locator)
        self.input_fapiao_registrationNo = super().get_element(self.input_fapiao_registrationNo_locator)
        self.input_fapiao_bankName = super().get_element(self.input_fapiao_bankName_locator)
        self.input_fapiao_accountNo = super().get_element(self.input_fapiao_accountNo_locator)
        self.input_fapiao_telephone = super().get_element(self.input_fapiao_telephone_locator)
        self.input_fapiao_companyAddress = super().get_element(self.input_fapiao_companyAddress_locator)
        self.div_cc_year_2023 = super().get_element(self.div_cc_year_2023_locator)
        self.div_country_usa = super().get_element(self.div_country_usa_locator)
        self.div_states_California = super().get_element(self.div_states_California_locator)
        self.href_add_new_pi = super().get_element(self.href_add_new_pi_locator)
        self.div_add_payment = super().get_element(self.div_add_payment_locator)
        self.radio_cc_pay = super().get_element(self.radio_cc_pay_locator)
        self.input_country = super().get_element(self.input_country_locator)
