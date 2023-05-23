from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):

    original_price_locator = (By.CSS_SELECTOR,"[class = 'mErEH _223RA']")

    asset_name_locator = (By.CSS_SELECTOR, "[class='cfm2v']")
    single_multi_choice_locator = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[5]/div[1]/i')
    multi_locator = (By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[5]/div[2]/div/div[1]/div[2]/button')
    asset_common_price_locator = ( By.CLASS_NAME, 'mErEH')
    add_to_cart_main_locator = (By.CSS_SELECTOR, "[class ='_3UE3J _3zD70 auto _6dtXD _1CXMR']")
    btn_view_cart_locator = (By.CSS_SELECTOR, "[class='_3UE3J ZQFsR auto _24sbO']")
    arrow_add_to_cart_locator = (By.CSS_SELECTOR,"[class = 'ifont ifont-icon-arrow-down h2TMq']")
    upgrade_promtion_price_locator = (By.XPATH,"/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]")
    normal_promotion_price_locator = (By.CLASS_NAME,'mErEH')
    label_price_minicart_locator = (By.CSS_SELECTOR, "[class = 'row TmM8_']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.original_price = None
        self.asset_name = None
        self.single_multi_choice = None
        self.multi = None
        self.asset_common_price = None
        self.add_to_cart_main = None
        self.btn_view_cart = None
        self.arrow_add_to_cart = None
        self.upgrade_promtion_price = None
        self.normal_promotion_price = None
        self.label_price_minicart = None
        self.present_locator = self.asset_name_locator

    def init_elements(self):
        super().init_elements()
        self.original_price = super().get_element(self.original_price_locator)
        self.asset_name = super().get_element(self.asset_name_locator)
        self.single_multi_choice = super().get_element(self.single_multi_choice_locator)
        self.multi = super().get_element(self.multi_locator)
        self.asset_common_price = super().get_element(self.asset_common_price_locator)
        self.add_to_cart_main = super().get_element(self.add_to_cart_main_locator)
        self.btn_view_cart = super().get_element(self.btn_view_cart_locator)
        self.arrow_add_to_cart = super().get_element(self.arrow_add_to_cart_locator)
        self.upgrade_promtion_price = super().get_element(self.upgrade_promtion_price_locator)
        self.normal_promotion_price = super().get_element(self.normal_promotion_price_locator)
        self.label_price_minicart = super().get_element(self.label_price_minicart_locator)