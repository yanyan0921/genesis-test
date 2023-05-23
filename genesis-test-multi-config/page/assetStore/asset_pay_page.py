from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_country_locator = (By.CLASS_NAME, 'select2-selection__rendered')
    btn_province_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[2]/dd[1]/div/button")
    div_province_anhui_locator = (By.XPATH,"//*[@id=\"org_address_form\"]/div/div[1]/dl[2]/dd[1]/div/div/ul/li[2]/a")
    btn_state_locator = (By.XPATH, "//*[@id='org_address_form']/div/div[1]/dl[2]/dd[1]/span/span[1]/span/span[2]")
    btn_us_textbox_locator = (By.XPATH, "/html/body/div[3]/section/div[3]/div/div[1]/div[2]/div[2]/form/div/div/div[2]/div/div[1]/dl[1]/dd[1]/span/span[1]/span/span[1]")
    btn_utah_textbox_locator = (By.XPATH, "/html/body/div[3]/section/div[3]/div/div[1]/div[2]/div[2]/form/div/div/div[2]/div/div[1]/dl[2]/dd[1]/span/span[1]/span/span[1]")
    btn_return_to_cart_locator = (By.XPATH, "/html/body/div[3]/header/div/div/a")


    input_firstname_locator = (By.NAME, "sta[firstName]")
    input_lastname_locator = (By.NAME, "sta[lastName]")
    input_email_locator = (By.NAME, "sta[email]")
    input_phone_locator = (By.NAME, "sta[phoneNumber]")
    input_address_locator = (By.NAME, "sta[streetAddress]")
    input_postalCode_locator = (By.NAME, "sta[postalCode]")
    input_city_locator = (By.NAME, "sta[locality]")
    btn_taxno_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[7]/dl/dd[1]/div[2]/div[2]/label")
    FR_taxNumber_locator = (By.CSS_SELECTOR,"[class = 'vat req c720 c721']")
    arrow_coupon_code_locator = (By.XPATH, "//*[@id=\"summary-right\"]/div/div[1]/div[1]/div[3]")
    coupon_creditcode_input_locator = (By.XPATH,'//*[@id="summary-right"]/div/div[2]/dl/dd[1]/input')
    btn_apply_locator = (By.XPATH,'//*[@id="summary-right"]/div/div[2]/dl/dd[1]/button')

    btn_send_sms_code_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[4]/dl[1]/dd[1]/button")
    input_sms_code_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[4]/dl[2]/dd[1]/input")
    btn_verify_sms_code_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[4]/dl[2]/dd[1]/button")
    label_subtotal_locator = (By.XPATH, "/html/body/div[3]/section/div[3]/div/div[1]/div[2]/div[3]/div/div[1]/div[2]/dl[3]/dd")
    label_tax_locator = (By.XPATH, "/html/body/div[3]/section/div[3]/div/div[1]/div[2]/div[3]/div/div[1]/div[2]/dl[4]/dd")
    label_To_pay_now_locator = (By.XPATH, "//*[@id='summary-right']/div/div[1]/div[2]/dl[5]/dd")
    btn_paypal_locator = (By.XPATH, '//*[@id="payment_methods"]/div[2]/div[1]/dl/dd[2]/div/label/span')
    btn_Assetcredits_locator = (By.XPATH, '//*[@id="payment_methods"]/div[2]/div[1]/dl/dd[2]/div/label/span[1]')

    div_country_box_locator = (By.CSS_SELECTOR,"[class = 'select2-search__field']")
    div_country_brazil_locator = (By.XPATH, "/html/body/span/span/span[2]/ul/li[30]")
    div_country_us_locator = (By.XPATH, "/html/body/span/span/span[2]/ul/li[228]")
    div_state_utah_locator = (By.XPATH, "/html/body/span/span/span[2]/ul/li[53]")
    div_country_japan_locator = (By.XPATH, "/html/body/span/span/span[2]/ul/li[110]")
    div_country_china_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[1]/dd[1]/div/div/ul/li[6]")
    div_country_hongkong_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[1]/dd[1]/div/div/ul/li[60]")
    div_country_macao_locator = (By.XPATH, "//*[@id=\"org_address_form\"]/div/div[1]/dl[1]/dd[1]/div/div/ul/li[61]")
    div_country_southkorea_locator = (By.XPATH, " //*[@id=\"org_address_form\"]/div/div[1]/dl[1]/dd[1]/div/div/ul/li[14]")
    checkbox_terms_locator = (By.ID, "summary_terms")
    btn_pay_now_locator = (By.XPATH, "//*[@id=\"summary-right\"]/div/div[1]/div[1]/button")
    icon_unity_logo_locator = (By.CLASS_NAME, "unity-logo")
    add_new_hypertext_locator = (By.XPATH, '//*[@id="payment_methods"]/div[1]/a')

    select_paypal_locator = (By.ID, "new_PAYPAL")
    select_alipay_locator = (By.XPATH,"//*[@id=\"pi-editor\"]/div[1]/dl[1]/dt/div/label/span")
    select_creditcard_locator = (By.CSS_SELECTOR, '[class="card na"]')
    select_credit_locator = (By.CSS_SELECTOR,"[class = 'card as_wallet_credit']")
    future_purchase_checkbox_locator = (By.XPATH, "//*[@id=\"payment_methods\"]/div[3]/div/label")
    input_paypal_email_locator = (By.ID, 'paypal-email')
    input_creditcard_locator = (By.ID, "cardnr")
    input_creditcode_locator = (By.XPATH, '//*[@id="summary-right"]/div/div[2]/dl/dd[1]/input')
    btn_creditcode_locator = (By.XPATH, '//*[@id="summary-right"]/div/div[2]/dl/dd[1]/button')
    input_alipay_locator = (By.ID,"alipay-account")
    month_box_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[2]/dl[1]/dd[1]/div[1]/span/span[1]/span/span[2]")
    month_locator = (By.CSS_SELECTOR, "[class = 'select2-results__option']")
    year_box_locator = (By.XPATH, "//*[@id=\"pi-editor\"]/div[2]/div[2]/dl[1]/dd[1]/div[2]/span/span[1]/span/span[2]")
    year_locator = (By.XPATH, "/html/body/span/span/span[2]/ul/li[4]")
    cvc_cvv2_locator = (By.CSS_SELECTOR, "[class='cvc req c201 c202']")
    Cardholder_name_box_locator = (By.XPATH, "//*[@id=\"name\"]")
    same_as_checkbox_locator = (By.XPATH, "//*[@id=\"billing_addr_same_as\"]/label")
    firstname_checkbox_locator = (By.NAME, "firstName")
    error_code_msg_locator = (By.XPATH, "//*[@id=\"addressApp\"]/div[2]/div[2]/div/div/p[1]")
    login_btn_locator = (By.CSS_SELECTOR, "switch-tip-btn")
    Cardholder_name_Eorror_tip_locator = (By.XPATH,"//*[@id='pi-editor']/div[2]/div[3]/dl/dd[2]/span[2]")
    WorldPay_Ok_btn_locator = (By.XPATH,"//*[@id=\"challengeForm\"]/input[4]")

    error_tip_text_locator = (By.CSS_SELECTOR,"[class = 'server-error-warning']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.btn_pay_now_locator
        self.checkbox_terms = self.checkbox_terms_locator
        self.btn_pay_now = self.btn_pay_now_locator
        self.icon_unity_logo = self.icon_unity_logo_locator
        self.add_new_hypertext = self.add_new_hypertext_locator
        self.select_alipay = None
        self.input_alipay = None
        self.select_paypal = None
        self.input_paypal_email = None
        self.future_purchase_checkbox = None
        self.select_creditcard = None
        self.input_creditcode = None
        self.btn_creditcode = None
        self.select_credit = None
        self.month_box = None
        self.month = None
        self.year_box = None
        self.year = None
        self.cvc_cvv2 = None
        self.Cardholder_name_box = None
        self.same_as_checkbox = None
        self.firstname_checkbox = None
        self.error_code_msg = None
        self.login_btn = None
        self.Cardholder_name_Eorror_tip = None
        self.WorldPay_Ok_btn = None;

        self.btn_country = self.btn_country_locator
        self.btn_province = self.btn_province_locator
        self.div_province_anhui = self.div_province_anhui_locator
        self.input_firstname = self.input_firstname_locator
        self.input_lastname = self.input_lastname_locator
        self.input_email = self.input_email_locator
        self.input_phone = self.input_phone_locator
        self.input_address = self.input_address_locator
        self.input_postalCode = self.input_postalCode_locator
        self.input_city = self.input_city_locator
        self.btn_taxno = self.btn_taxno_locator
        self.FR_taxNumber = self.FR_taxNumber_locator
        self.arrow_coupon_code = self.arrow_coupon_code_locator
        self.coupon_creditcode_input = self.coupon_creditcode_input_locator
        self.btn_apply = self.btn_apply_locator

        self.btn_send_sms_code = self.btn_send_sms_code_locator
        self.input_sms_code = self.input_sms_code_locator
        self.btn_verify_sms_code = self.btn_verify_sms_code_locator
        self.label_subtotal = None
        self.label_tax = None
        self.label_To_pay_now = None
        self.btn_paypal = None
        self.btn_Assetcredits = None

        self.btn_country = None
        self.div_country_box = None
        self.div_country_brazil = None
        self.div_country_us = None
        self.div_state_utah = None
        self.div_country_japan = None
        self.div_country_china = None
        self.div_country_hongkong = None
        self.div_country_macao = None
        self.div_country_southkorea = None
        self.btn_state  = None
        self.btn_us_textbox  = None
        self.btn_utah_textbox = None
        self.btn_return_to_cart = None


        self.error_tip_text = None

    def init_elements(self):
        super().init_elements()
        self.btn_agree_continut = super().get_element(self.checkbox_terms_locator)
        self.btn_pay_now = super().get_element(self.btn_pay_now_locator)
        self.icon_unity_logo = super().get_element(self.icon_unity_logo_locator)
        self.add_new_hypertext = super().get_element(self.add_new_hypertext_locator)
        self.select_paypal = super().get_element(self.select_paypal_locator)
        self.input_paypal_email = super().get_element(self.input_paypal_email_locator)
        self.future_purchase_checkbox = super().get_element(self.future_purchase_checkbox_locator)
        self.select_CreditCard = super().get_element(self.select_creditcard_locator)
        self.input_creditcard = super().get_element(self.input_creditcard_locator)
        self.input_creditcode = super().get_element(self.input_creditcode_locator)
        self.btn_creditcode = super().get_element(self.btn_creditcode_locator)
        self.select_credit = super().get_element(self.select_credit_locator)
        self.month_box = super().get_element(self.month_box_locator)
        self.month = super().get_element(self.month_locator)
        self.year_box = super().get_element(self.year_box_locator)
        self.year = super().get_element(self.year_locator)
        self.cvc_cvv2 = super().get_element(self.cvc_cvv2_locator)
        self.Cardholder_name_box = super().get_element(self.Cardholder_name_box_locator)
        self.same_as_checkbox = super().get_element(self.same_as_checkbox_locator)
        self.firstname_checkbox = super().get_element(self.firstname_checkbox_locator)
        self.error_code_msg = super().get_element(self.error_code_msg_locator)
        self.select_alipay = super().get_element(self.select_alipay_locator)
        self.input_alipay = super().get_element(self.input_alipay_locator)
        self.login_btn = super().get_element(self.login_btn_locator)
        self.Cardholder_name_Eorror_tip = super().get_element(self.Cardholder_name_Eorror_tip_locator)
        self.WorldPay_Ok_btn = super().get_element(self.WorldPay_Ok_btn_locator)

        self.btn_country = super().get_element(self.btn_country_locator)
        self.btn_state = super().get_element(self.btn_state_locator)
        self.div_province_anhui = super().get_element(self.btn_province_locator)
        self.btn_province = super().get_element(self.btn_province_locator)
        self.input_firstname = super().get_element(self.input_firstname_locator)
        self.input_lastname = super().get_element(self.input_lastname_locator)
        self.input_email = super().get_element(self.input_email_locator)
        self.input_phone = super().get_element(self.input_phone_locator)
        self.input_address = super().get_element(self.input_address_locator)
        self.input_postalCode = super().get_element(self.input_postalCode_locator)
        self.input_city = super().get_element(self.input_city_locator)
        self.btn_taxno = super().get_element(self.btn_taxno_locator)
        self.FR_taxNumber = super().get_element(self.FR_taxNumber_locator)
        self.arrow_coupon_code = super().get_element(self.arrow_coupon_code_locator)
        self.coupon_creditcode_input = super().get_element(self.coupon_creditcode_input_locator)
        self.btn_apply = super().get_element(self.btn_apply_locator)

        self.btn_send_sms_code = super().get_element(self.btn_send_sms_code_locator)
        self.input_sms_code = super().get_element(self.input_sms_code_locator)
        self.btn_verify_sms_code = super().get_element(self.btn_verify_sms_code_locator)
        self.label_subtotal = super().get_element(self.label_subtotal_locator)
        self.label_tax = super().get_element(self.label_tax_locator)
        self.label_To_pay_now = super().get_element(self.label_To_pay_now_locator)
        self.btn_us_textbox = super().get_element(self.btn_us_textbox_locator)
        self.btn_utah_textbox = super().get_element(self.btn_utah_textbox_locator)

        self.div_country_box = super().get_element(self.div_country_box_locator)
        self.div_country_brazil = super().get_element(self.div_country_brazil_locator)
        self.div_country_us = super().get_element(self.div_country_us_locator)
        self.div_state_utah = super().get_element(self.div_state_utah_locator)
        self.div_country_japan = super().get_element(self.div_country_japan_locator)
        self.div_country_china = super().get_element(self.div_country_china_locator)
        self.div_country_hongkong = super().get_element(self.div_country_hongkong_locator)
        self.div_country_macao = super().get_element(self.div_country_macao_locator)
        self.div_country_southkorea = super().get_element(self.div_country_southkorea_locator)
        self.btn_return_to_cart = super().get_element(self.btn_return_to_cart_locator)
        self.btn_paypal = super().get_element(self.btn_paypal_locator)
        self.btn_Assetcredits = super().get_element(self.btn_Assetcredits_locator)

        self.error_tip_text = super().get_element(self.error_tip_text_locator)