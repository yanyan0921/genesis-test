from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    add_to_cart_main_locator = (By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[7]/div/div/button')
    add_to_cart_anonymous_locator = (By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[6]/div/div[2]/button')
    request_add_to_cart_main_locator = (By.CLASS_NAME, '_3vg37')
    btn_add_to_cart_locator = (By.XPATH,
                               "//*[@id='main-layout-scroller']/div/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div[2]/div[5]/div/div/div[3]/button")
    add_to_cart_btn_locator = (By.CSS_SELECTOR, "[class= '_3UE3J ZQFsR auto _2kZZa']")
    btn_request_for_approval_locator = (By.CSS_SELECTOR, "[class= '_3UE3J ZQFsR auto _2kZZa']")
    input_request_text_locator = (
        By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div[2]/div[3]/div/div[1]")
    request_approval_btn_locator = (By.CSS_SELECTOR, "[class= '_3UE3J _3zD70 auto -XHn3']")
    btn_view_cart_locator = (By.CSS_SELECTOR, "[class='_3UE3J ZQFsR auto vtzyy']")
    request_btn_view_cart_locator = (By.CSS_SELECTOR, "[class = '_3UE3J ZQFsR auto vtzyy']")
    btn_view_cart_Not_logged_in_locator = (By.CLASS_NAME, "_3UE3J ZQFsR auto _24sbO")
    arrow_open_in_unity_locator = (By.CSS_SELECTOR, '[class="_3l4rA"]')
    href_terms_of_services_locator = (By.CLASS_NAME, "EJ5it")
    add_tag_btn_locator = (By.CSS_SELECTOR, "[class='_3UE3J pDJt- auto _31f1z _3dfMi']")
    btn_report_locator = (By.CLASS_NAME, "_4Ln7f")
    btn_express_text_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[6]/div/div/button')
    Accept_btn_locator = (By.LINK_TEXT, "Accept")
    asset_name_locator = (By.CSS_SELECTOR, "[class='cfm2v']")
    add_to_list_btn_locator = (By.CSS_SELECTOR, "[class = '_3UE3J MtRkn auto Cdm9P']")
    btn_new_list_locator = (By.CLASS_NAME, "EaoU7")
    input_list_name_locator = (By.CLASS_NAME, "_1gSGR")
    btn_save_for_list_locator = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div/div[1]/div/div/div[4]/button[2]')
    btn_save_for_item_locator = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div[2]/button')
    icon_Visibility_Private_locator = (By.CLASS_NAME, "ubwet _2OWZd")
    icon_Visibility_Public_locator = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div[1]/div/div/div[3]/div[3]/div[2]/div[2]/div')
    btn_save_locator = (By.CLASS_NAME, "_3UE3J pDJt- auto IaiTq")
    Input_box_locator = (By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/textarea")
    Submit_btn_locator = (By.CLASS_NAME, "_3UE3J _3zD70 auto _3er3j")
    lable_fedback_locator = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div/div[1]/div/div/div[2]/div[1]')
    read_more_review_btn_locator = (By.CLASS_NAME, "D_-Sy")

    arrow_support_the_creator_locator = (By.CSS_SELECTOR, "[class = '_2NQ0d ifont ifont-icon-arrow-up _2NQ0d']")
    btn_fixedtips_3_locator = (By.CLASS_NAME, '_2RZxq')
    btn_fixedtips_5_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div/div[2]')
    custom_support_price_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div/div[3]')
    label_price_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]')

    Qty_box_locator = (By.CSS_SELECTOR, "[class = '_1cSsg']")
    Qty_1_locator = (By.XPATH,'//*[@id="Product/ProductDetailController"]/div/div/div/div[1]/div/div[2]/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[1]')
    Qty_10_locator = (By.XPATH,'//*[@id="Product/ProductDetailController"]/div/div/div/div[1]/div/div[2]/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[10]')
    Qty_input_box_locator = (By.XPATH,'//*[@id="Product/ProductDetailController"]/div/div/div/div[1]/div/div[2]/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/input')
    btn_proceed_to_checkout_locator = (By.XPATH,'/html/body/div[1]/div/div/div/di/div/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div/button[2]')
    label_price_minicart_locator = (By.CSS_SELECTOR, "[class = 'row TmM8_']")
    icon_save_for_later_locator = (By.XPATH,'//*[@id="Product/ProductDetailController"]/div/div/div/div[1]/div/div[2]/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/button[2]')
    icon_remove_locator = (By.CSS_SELECTOR, "[class = '_3UE3J _3vV3- auto']")
    icon_close_locator = (By.CSS_SELECTOR, "[class = 'ifont ifont-close _3MYHt']")
    tips_empty_locator = (By.CSS_SELECTOR, "[class = '_3Kg2p']")
    Input_Qty_box_locator = (By.XPATH,'/html/body/div[1]/div/div/div/di/div/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/input')
    btn_buy_now_locator = (By.CSS_SELECTOR, "[class = '_3UE3J _3zD70 auto _1wYRX _5-uB5']")
    input_password_locator = (By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div[1]/div/div/div[2]/div[2]/input")
    btn_express_purchase_locator = (By.CSS_SELECTOR, "[class='_3UE3J _3zD70 auto qsCb9']")
    accept_terms_locator = (By.CLASS_NAME, "_2V-G7")

    single_multi_choice_locator = (By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[5]/div[1]/i')
    multi_locator = (By.XPATH,
                     '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[5]/div[2]/div/div[1]/div[2]/button')
    single_locator = (By.CLASS_NAME, '_3_GB5')
    asset_common_price_locator = (By.XPATH,
                                  '/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div')

    btn_post_reviews_locator = (By.CSS_SELECTOR, "[class = '_3UE3J pDJt- auto']")
    icon_rating_locator = (
    By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div[3]")
    input_reviews_title_locator = (By.CSS_SELECTOR, "[class='_1gSGR']")
    input_reviews_content_locator = (By.CSS_SELECTOR, "[class='_22V1a _1kyS6']")
    btn_reviews_post_locator = (By.CSS_SELECTOR, "[class='_3UE3J pDJt- auto tIoLl']")
    label_reviews_title_locator = (By.CSS_SELECTOR,"[class='_2GKDi _3VcrN']")
    label_reviews_content_locator = (By.CSS_SELECTOR,"[class ='Gbs5z']")
    icon_edit_reviews_locator = (By.CLASS_NAME, '_3V1lU')
    icon_delete_review_locator = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[3]/div/div/div[4]/div[2]/div/button[2]')
    icon_rating_edit_locator = (
    By.XPATH, '/html/body/div[5]/div/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div[2]')
    btn_delete_review_locator = (By.CSS_SELECTOR, "[class='_3UE3J pDJt- auto _2YXi8']")
    btn_delete_reply_locator = (By.XPATH,
                                '//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div/div[3]/div/div[2]/div/div[3]/button[2]')
    btn_delete_reply_OK_locator = (By.CSS_SELECTOR, "[class='_3UE3J pDJt- auto _2YXi8']")
    label_count_reviews_locator = (By.CSS_SELECTOR, "[class='_2rWAE']")
    accept_cookies_locator = (By.CSS_SELECTOR, "[class='_2fq1-']")
    label_publisher_reply_locator = (By.CSS_SELECTOR, "[class='_3xC-c']")
    label_1_star_locator = (By.XPATH,
                            '/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/div/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div[6]')
    filter_stars_locator = (By.XPATH,
                            '/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/div/div[1]/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]/button/div/div[1]')
    btn_reviews_locator = (By.ID,'reviews')
    input_search_locator = (By.CSS_SELECTOR,"[class = '_3_gZI']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_add_to_cart = None
        self.add_to_cart_btn = None
        self.add_to_cart_main = None
        self.add_to_cart_anonymous = None
        self.btn_request_for_approval = None
        self.href_terms_of_services = None
        self.btn_view_cart = None
        self.btn_view_cart_Not_logged_in = None
        self.arrow_open_in_unity = None
        self.add_tag_btn = None
        self.btn_report = None
        self.btn_express_text = None
        self.Accept_btn = None
        self.asset_name = None
        self.input_request_text = None
        self.request_approval_btn = None
        self.add_to_list_btn = self.add_to_list_btn_locator
        self.btn_new_list = None
        self.input_list_name = None
        self.btn_save_for_list = None
        self.btn_save_for_item = None
        self.icon_Visibility_Private = None
        self.icon_Visibility_Public = None
        self.btn_save = None
        self.Input_box = None
        self.Submit_btn = None
        self.lable_fedback = None

        self.read_more_review_btn = None
        self.request_btn_view_cart = None
        self.request_add_to_cart_main = None
        self.arrow_support_the_creator = None
        self.btn_fixedtips_3 = None
        self.btn_fixedtips_5 = None
        self.custom_support_price = None
        self.label_price = None

        self.Qty_box = None
        self.Qty_1 = None
        self.Qty_10 = None
        self.Qty_input_box = None
        self.Input_Qty_box = None
        self.btn_proceed_to_checkout = None
        self.label_price_minicart = None
        self.icon_save_for_later = None
        self.icon_remove = None
        self.icon_close = None
        self.tips_empty = None
        self.btn_buy_now = None
        self.cart = None
        self.input_password = None
        self.btn_express_purchase = None
        self.accept_terms = None
        self.single_multi_choice = None
        self.multi = None
        self.single = None
        self.asset_common_price = None

        self.btn_post_reviews = None
        self.icon_rating = None
        self.input_reviews_title = None
        self.input_reviews_content = None
        self.btn_reviews_post = None
        self.label_reviews_title = None
        self.label_reviews_content = None
        self.icon_edit_reviews = None
        self.icon_delete_review = None
        self.icon_rating_edit = None
        self.btn_delete_review = None
        self.btn_delete_reply_OK = None
        self.btn_delete_reply = None
        self.label_count_reviews = None
        self.accept_cookies = None
        self.label_publisher_reply = None
        self.label_1_star = None
        self.filter_stars = None
        self.btn_reviews = None
        self.input_search = None

        self.present_locator = self.btn_report_locator

    def init_elements(self):
        super().init_elements()
        self.btn_add_to_cart = super().get_element(self.btn_add_to_cart_locator)
        self.add_to_cart_btn = super().get_element(self.add_to_cart_btn_locator)
        self.btn_view_cart = super().get_element(self.btn_view_cart_locator)
        self.btn_view_cart_Not_logged_in = super().get_element(self.btn_view_cart_Not_logged_in_locator)
        self.arrow_open_in_unity = super().get_element(self.arrow_open_in_unity_locator)
        self.href_terms_of_services = super().get_element(self.href_terms_of_services_locator)
        self.add_tag_btn = super().get_element(self.add_tag_btn_locator)
        self.btn_report = super().get_element(self.btn_report_locator)
        self.btn_express_text = super().get_element(self.btn_express_text_locator)
        self.add_to_cart_main = super().get_element(self.add_to_cart_main_locator)
        self.add_to_cart_anonymous = super().get_element(self.add_to_cart_anonymous_locator)
        self.Accept_btn = super().get_element(self.Accept_btn_locator)
        self.asset_name = super().get_element(self.asset_name_locator)
        self.btn_request_for_approval = super().get_element(self.btn_request_for_approval_locator)
        self.input_request_text = super().get_element(self.input_request_text_locator)
        self.request_approval_btn = super().get_element(self.request_approval_btn_locator)
        self.add_to_list_btn = super().get_element(self.add_to_list_btn_locator)
        self.btn_new_list = super().get_element(self.btn_new_list_locator)
        self.input_list_name = super().get_element(self.input_list_name_locator)
        self.btn_save_for_list = super().get_element(self.btn_save_for_list_locator)
        self.btn_save_for_item = super().get_element(self.btn_save_for_item_locator)
        self.icon_Visibility_Private = super().get_element(self.icon_Visibility_Private_locator)
        self.icon_Visibility_Public = super().get_element(self.icon_Visibility_Public_locator)
        self.btn_save = super().get_element(self.btn_save_locator)
        self.Input_box = super().get_element(self.Input_box_locator)
        self.Submit_btn = super().get_element(self.Submit_btn_locator)
        self.lable_fedback = super().get_element(self.lable_fedback_locator)

        self.read_more_review_btn = super().get_element(self.read_more_review_btn_locator)
        self.request_btn_view_cart = super().get_element(self.request_btn_view_cart_locator)
        self.request_add_to_cart_main = super().get_element(self.request_add_to_cart_main_locator)
        self.btn_fixedtips_3 = super().get_element(self.btn_fixedtips_3_locator)
        self.btn_fixedtips_5 = super().get_element(self.btn_fixedtips_5_locator)
        self.custom_support_price = super().get_element(self.custom_support_price_locator)
        self.label_price = super().get_element(self.label_price_locator)
        self.arrow_support_the_creator = super().get_element(self.arrow_support_the_creator_locator)

        self.Qty_box = super().get_element(self.Qty_box_locator)
        self.Qty_1 = super().get_element(self.Qty_1_locator)
        self.Qty_10 = super().get_element(self.Qty_10_locator)
        self.Qty_input_box = super().get_element(self.Qty_input_box_locator)
        self.Input_Qty_box = super().get_element(self.Input_Qty_box_locator)
        self.label_price_minicart = super().get_element(self.label_price_minicart_locator)
        self.icon_close = super().get_element(self.icon_close_locator)
        self.icon_save_for_later = super().get_element(self.icon_save_for_later_locator)
        self.icon_remove = super().get_element(self.icon_remove_locator)
        self.tips_empty = super().get_element(self.tips_empty_locator)
        self.btn_buy_now = super().get_element(self.btn_buy_now_locator)

        self.input_password = super().get_element(self.input_password_locator)
        self.btn_express_purchase = super().get_element(self.btn_express_purchase_locator)
        self.accept_terms = super().get_element(self.accept_terms_locator)
        self.single_multi_choice = super().get_element(self.single_multi_choice_locator)
        self.multi = super().get_element(self.multi_locator)
        self.single = super().get_element(self.single_locator)
        self.asset_common_price = super().get_element(self.asset_common_price_locator)

        self.btn_post_reviews = super().get_element(self.btn_post_reviews_locator)
        self.icon_rating = super().get_element(self.icon_rating_locator)
        self.input_reviews_title = super().get_element(self.input_reviews_title_locator)
        self.input_reviews_content = super().get_element(self.input_reviews_content_locator)
        self.btn_reviews_post = super().get_element(self.btn_reviews_post_locator)
        self.label_reviews_title = super().get_element(self.label_reviews_title_locator)
        self.label_reviews_content = super().get_element(self.label_reviews_content_locator)
        self.icon_edit_reviews = super().get_element(self.icon_edit_reviews_locator)
        self.icon_delete_review = super().get_element(self.icon_delete_review_locator)
        self.icon_rating_edit = super().get_element(self.icon_rating_edit_locator)
        self.btn_delete_review = super().get_element(self.btn_delete_review_locator)
        self.btn_delete_reply = super().get_element(self.btn_delete_reply_locator)
        self.btn_delete_reply_OK = super().get_element(self.btn_delete_reply_OK_locator)
        self.label_count_reviews = super().get_element(self.label_count_reviews_locator)
        self.accept_cookies = super().get_element(self.accept_cookies_locator)
        self.label_publisher_reply = super().get_element(self.label_publisher_reply_locator)
        self.label_1_star = super().get_element(self.label_1_star_locator)
        self.filter_stars = super().get_element(self.filter_stars_locator)
        self.btn_reviews = super().get_element(self.btn_reviews_locator)
        self.input_search = super().get_element(self.input_search_locator)



