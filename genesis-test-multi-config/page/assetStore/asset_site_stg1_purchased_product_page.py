from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    plus_pro_price_locator = (By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div/div/div')
    original_price_locator = (By.CSS_SELECTOR, "[class = 'mErEH _223RA']")

    asset_name_locator = (By.CSS_SELECTOR, "[class='cfm2v']")
    single_multi_choice_locator = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[4]/div[1]/div[2]/strong')
    multi_locator = (By.XPATH,
                     "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[2]/div/div[1]")
    asset_common_price_locator = (By.CSS_SELECTOR, "[class = 'mErEH _223RA']")
    add_to_cart_main_locator = (By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[6]/div/button[1]")
    btn_view_cart_locator = (By.CSS_SELECTOR, "[class='_3UE3J ZQFsR auto _24sbO']")
    arrow_add_to_cart_locator = (By.CSS_SELECTOR, "[class = 'ifont ifont-icon-arrow-down h2TMq']")
    request_for_approval_locator = (By.CSS_SELECTOR, "[class = '_3UE3J ZQFsR auto _2kZZa']")
    request_approval_btn_locator = (By.CSS_SELECTOR, "[class= '_3UE3J _3zD70 auto -XHn3']")
    input_request_text_locator = (
        By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div[2]/div[3]/div/div[1]")
    site_stg_3_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div/a/div[1]/div')
    site_stg_2_locator = (By.XPATH,"//*[@id=\"main-layout-scroller\"]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/a/div[1]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.plus_pro_price = None
        self.original_price = None
        self.asset_name = None
        self.single_multi_choice = None
        self.multi = None
        self.asset_common_price = None
        self.add_to_cart_main = None
        self.btn_view_cart = None
        self.arrow_add_to_cart = None
        self.request_for_approval = None
        self.request_approval_btn = None
        self.input_request_text = None
        self.site_stg_2 = None
        self.site_stg_3 = None
        self.present_locator = self.asset_name_locator

    def init_elements(self):
        super().init_elements()
        self.plus_pro_price = super().get_element(self.plus_pro_price_locator)
        self.original_price = super().get_element(self.original_price_locator)
        self.asset_name = super().get_element(self.asset_name_locator)
        self.single_multi_choice = super().get_element(self.single_multi_choice_locator)
        self.multi = super().get_element(self.multi_locator)
        self.asset_common_price = super().get_element(self.asset_common_price_locator)
        self.add_to_cart_main = super().get_element(self.add_to_cart_main_locator)
        self.btn_view_cart = super().get_element(self.btn_view_cart_locator)
        self.arrow_add_to_cart = super().get_element(self.arrow_add_to_cart_locator)
        self.request_for_approval = super().get_element(self.request_for_approval_locator)
        self.request_approval_btn = super().get_element(self.request_approval_btn_locator)
        self.input_request_text = super().get_element(self.input_request_text_locator)
        self.site_stg_2 = super().get_element(self.site_stg_2_locator)
        self.site_stg_3 = super().get_element(self.site_stg_3_locator)