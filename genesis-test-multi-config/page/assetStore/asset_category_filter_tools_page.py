from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    site_stg_1_item_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/div[1]/div/div/div/div/a/div[1]')
    game_flow_item_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div[1]/div[4]/div[3]/div/div[1]/div/div/div/div/a/div[1]/div')
    filter_refine_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/span')
    btn_best_match_locator = (By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div[10]')
    filter_all_category_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div[7]/div[1]/div[1]/strong')
    price_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div[2]/div/div[5]/div[1]/div[1]/strong')
    free_assets_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div[10]/div[2]/div/div[2]/div[2]/span[1]')
    free_price_locator = (By.CSS_SELECTOR,"[class ='mErEH _223RA']")
    label_quantity_results_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/strong[1]')
    label_3D_locator = (By.CLASS_NAME, "_4wnBF")
    filter_publisher_locator = (By.CLASS_NAME, "_4wnBF")
    filter_3D_locator = (By.CLASS_NAME, "_2byuL")
    filter_Tools_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div[7]/div[2]/div/div[7]/div[2]/div[1]/div')
    input_publisher_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div[13]/div[2]/div/div[1]/div/div/input')
    label_item_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div[3]/div/div[2]/div/div/div/div/a/div[1]/div')
    checkbox_hide_purchase_locator = (By.CLASS_NAME, "_4wnBF")
    input_search_box_locator = (By.CLASS_NAME, "_3_gZI")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.site_stg_1_item = None
        self.game_flow_item = None
        self.filter_all_category = None
        self.btn_best_match = None
        self.free_assets = None
        self.price = None
        self.free_price = None
        self.label_quantity_results = None
        self.label_3D = None
        self.filter_publisher = None
        self.filter_3D = None
        self.filter_Tools = None
        self.input_publisher = None
        self.label_item = None
        self.checkbox_hide_purchase = None
        self.input_search_box = None
        self.present_locator = self.filter_refine_locator

    def init_elements(self):
        super().init_elements()
        self.site_stg_1_item = super().get_element(self.site_stg_1_item_locator)
        self.filter_all_category = super().get_element(self.filter_all_category_locator)
        self.game_flow_item = super().get_element(self.game_flow_item_locator)
        self.filter_refine = super().get_element(self.filter_refine_locator)
        self.btn_best_match = super().get_element(self.btn_best_match_locator)
        self.price = super().get_element(self.price_locator)
        self.free_assets = super().get_element(self.free_assets_locator)
        self.free_price = super().get_element(self.free_price_locator)
        self.label_quantity_results = super().get_element(self.label_quantity_results_locator)
        self.label_3D = super().get_element(self.label_3D_locator)
        self.filter_publisher = super().get_element(self.filter_publisher_locator)
        self.filter_3D = super().get_element(self.filter_3D_locator)
        self.filter_Tools = super().get_element(self.filter_Tools_locator)
        self.input_publisher = super().get_element(self.input_publisher_locator)
        self.label_item = super().get_element(self.label_item_locator)
        self.checkbox_hide_purchase = super().get_element(self.checkbox_hide_purchase_locator)
        self.input_search_box = super().get_element(self.input_search_box_locator)

