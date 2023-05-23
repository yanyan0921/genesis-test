from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    label_total_amount_locator = (By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div[2]')
    label_tax_locator = (By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[4]/div[2]")
    label_tax_without_discount_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[3]/div[2]')
    href_terms_of_services_locator = (By.CLASS_NAME, "EJ5it")
    user_icon_locator = (By.CSS_SELECTOR, "class= '_1KJpK _1tK4F']")
    icon_logout_locator = (By.CSS_SELECTOR, "[class = '_2hXqt _1GsCa']")
    seat_management_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div[1]/div[2]/a')
    site_stg_1_amount_locator = (By.XPATH, "//*[@id=\"main-layout-scroller\"]/div/div[1]/div/div/div/div[3]/div/div[2]/div[2]/div/div[2]")
    label_tips_locator = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div/div[2]/div[3]/div[1]/div[4]')
    label_tips2_locator = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div[4]')
    item_name_locator = (By.CSS_SELECTOR, "[class = '_2pZAA']")
    icon_menu_locator = (By.CSS_SELECTOR, "[class = 'icon ifont ifont-more-vert _3RMvx']")
    label_request_refund_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div[5]/div[2]/div[2]/div[1]/a[1]/div')
    icon_menu_second_locator = (By.CSS_SELECTOR, "[class = 'icon ifont ifont-more-vert _3RMvx']")
    label_request_refund_second_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div[2]/div[3]/div[1]/div[5]/div[2]/div[2]/div[1]/a[1]/div')
    label_refund_history_second_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div[2]/div[3]/div[1]/div[5]/div[2]/div[2]/div[1]/a[1]/div')
    icon_menu_third_locator = (By.CSS_SELECTOR, "[class = 'icon ifont ifont-more-vert _3RMvx']")
    label_request_refund_third_locator = (By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div[2]/div[4]/div[1]/div[5]/div[2]/div[2]/div[1]/a[1]/div')
    label_refund_history_third_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div[2]/div[4]/div[1]/div[5]/div[2]/div[2]/div[1]/a[1]/div')
    btn_continue_locator = (By.CSS_SELECTOR, "[class = '_3UE3J _3zD70 auto']")
    box_request_reason_locator = (By.CSS_SELECTOR,"[class = '_8WK5S _3S48S normal']")
    label_request_reason_locator = (By.CSS_SELECTOR,"[class = '_3BlIq _3RSfC']")
    btn_submit_locator = (By.CSS_SELECTOR, "[class = '_3UE3J _3zD70 auto _1nJoY']")
    label_submit_locator = (By.CSS_SELECTOR, "[class = '_2Xz8n']")
    label_refund_history_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div[5]/div[2]/div[2]/div[1]/a[1]/div')
    label_result_locator = (By.CSS_SELECTOR,"[class = '_16HVS']")
    icon_close_locator = (By.CSS_SELECTOR,"[class = 'ifont ifont-close _2qFWx']")
    label_order_detail_locator = (By.CSS_SELECTOR,"[class = 'order-details-link']")
    input_search_box_locator = (By.CLASS_NAME, "_3_gZI")
    input_message_locator = (By.TAG_NAME,'textarea')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.label_total_amount = None
        self.href_terms_of_services = None
        self.label_tax = None
        self.label_tax_without_discount = None
        self.user_icon = self.user_icon_locator
        self.icon_logout = None
        self.seat_management = None
        self.site_stg_1_amount = None
        self.label_tips = None
        self.label_tips2 = None
        self.item_name = None
        self.icon_menu = None
        self.box_request_reason = None
        self.icon_menu_second = None
        self.label_request_refund_second = None
        self.label_refund_history_second = None
        self.icon_menu_third = None
        self.label_request_refund_third = None
        self.label_refund_history_third = None
        self.label_request_refund = None
        self.btn_continue = None
        self.label_request_reason = self.label_request_reason_locator
        self.btn_submit = None
        self.label_submit = None
        self.label_refund_history = None
        self.label_result = None
        self.icon_close = None
        self.label_order_detail = None
        self.input_search_box = None
        self.input_message = None
        self.present_locator = self.href_terms_of_services_locator

    def init_elements(self):
        super().init_elements()
        self.label_total_amount = super().get_element(self.label_total_amount_locator)
        self.label_tax = super().get_element(self.label_tax_locator)
        self.label_tax_without_discount = super().get_element(self.label_tax_without_discount_locator)
        self.href_terms_of_services = super().get_element(self.href_terms_of_services_locator)
        self.user_icon = super().get_element(self.user_icon_locator)
        self.icon_logout = super().get_element(self.icon_logout_locator)
        self.seat_management = super().get_element(self.seat_management_locator)
        self.site_stg_1_amount = super().get_element(self.site_stg_1_amount_locator)
        self.label_tips = super().get_element(self.label_tips_locator)
        self.label_tips2 = super().get_element(self.label_tips2_locator)
        self.item_name = super().get_element(self.item_name_locator)
        self.icon_menu = super().get_element(self.icon_menu_locator)
        self.label_request_refund = super().get_element(self.label_request_refund_locator)
        self.icon_menu_second = super().get_element(self.icon_menu_second_locator)
        self.label_request_refund_second = super().get_element(self.label_request_refund_second_locator)
        self.label_refund_history_second = super().get_element(self.label_refund_history_second_locator)
        self.icon_menu_third = super().get_element(self.icon_menu_third_locator)
        self.label_request_refund_third = super().get_element(self.label_request_refund_third_locator)
        self.label_refund_history_third = super().get_element(self.label_refund_history_third_locator)
        self.btn_continue = super().get_element(self.btn_continue_locator)
        self.box_request_reason = super().get_element(self.box_request_reason_locator)
        self.label_request_reason = super().get_element(self.label_request_reason_locator)
        self.btn_submit = super().get_element(self.btn_submit_locator)
        self.label_submit = super().get_element(self.label_submit_locator)
        self.label_refund_history = super().get_element(self.label_refund_history_locator)
        self.label_result = super().get_element(self.label_result_locator)
        self.icon_close = super().get_element(self.icon_close_locator)
        self.label_order_detail = super().get_element(self.label_order_detail_locator)
        self.input_search_box = super().get_element(self.input_search_box_locator)
        self.input_message = super().get_element(self.input_message_locator)