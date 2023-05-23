from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    asset_name_locator = (By.CSS_SELECTOR, "[class='cfm2v']")
    single_multi_choice_locator = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[5]/div[1]/i')
    normal_upgrade_promotion_price_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]')
    multi_locator = (By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[5]/div[2]/div/div[1]/div[2]/button')
    asset_common_price_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div')
    plus_pro_price_locator = (By.XPATH,
                              "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div[2]/div[1]/div/div/div")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.asset_name = None
        self.normal_upgrade_promotion_price = None
        self.single_multi_choice = None
        self.multi = None
        self.asset_common_price = None
        self.plus_pro_price = None
        self.present_locator = self.asset_name_locator

    def init_elements(self):
        super().init_elements()
        self.asset_name = super().get_element(self.asset_name_locator)
        self.single_multi_choice = super().get_element(self.single_multi_choice_locator)
        self.normal_upgrade_promotion_price = super().get_element(self.normal_upgrade_promotion_price_locator)
        self.multi = super().get_element(self.multi_locator)
        self.asset_common_price = super().get_element(self.asset_common_price_locator)
        self.plus_pro_price = super().get_element(self.plus_pro_price_locator)