from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    item_name_locator = (By.CSS_SELECTOR,"[class = '_1-e15 _25P-Q']")
    site_stg_1_item_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div/div/div/div/div/a/div[1]/div')
    div_search_item_locator = (By.XPATH, "//*[@id=\"main-layout-scroller\"]/div/div[1]/div/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div/a/div[1]/div[2]/div[2]")
    div_quick_look_locator = (By.CSS_SELECTOR, "[class='_1yJAY']")
    search_icon_locator = (By.CSS_SELECTOR,"[class = 'ifont ifont-search _2GQj8']")
    ddb_package_name_locator = (By.XPATH,
                         '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div[3]/div/div[1]/div/div/div/div/a/div[1]/div')
    item_locator = (By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div[3]/div/div[1]/div/div/div/a/div[1]/div[2]')
    add_to_cart_locator = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/button')
    icon_remove_locator = (By.XPATH, '/html/body/div[1]/div/div/div/di/div/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div[2]/div[3]/button[1]')
    tips_empty_locator = (By.CSS_SELECTOR,"[class = '_3Kg2p']")
    label_price_minicart_locator = (By.XPATH, '/html/body/div[1]/div/div/div/di/div/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/p')

    Qty_box_locator = (By.CSS_SELECTOR, "[class = 'Y1yB6']")
    Qty_1_locator = (By.XPATH,
                     '/html/body/div[1]/div/div/div/di/div/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[1]')
    label_3D_locator = (By.CLASS_NAME,'ifont ifont-close _2RLqu')
    btn_newNleaseDiscount_locator = (By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[3]/div/div/div/div/div[2]/div/div[4]/div[1]/div[1]/div/div/button')
    btn_sort_locator = (By.CLASS_NAME, '_1ofYm')
    label_sort_publishedDate_locator = (By.XPATH,
                                     '//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div[4]')


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.item_name = None
        self.div_search_item = None
        self.div_quick_look = None
        self.site_stg_1_item = None
        self.search_icon = None
        self.ddb_package_name = None
        self.item = None
        self.add_to_cart = None
        self.label_price_minicart = None
        self.icon_remove = None
        self.tips_empty = None
        self.Qty_box = None
        self.Qty_1 = None
        self.label_3D = None
        self.btn_newNleaseDiscount = None
        self.btn_sort = None
        self.label_sort_publishedDate = None
        self.present_locator = self.search_icon_locator

    def init_elements(self):
        super().init_elements()
        self.item_name = super().get_element(self.item_name_locator)
        self.div_search_item = super().get_element(self.div_search_item_locator)
        self.div_quick_look = super().get_element(self.div_quick_look_locator)
        self.site_stg_1_item = super().get_element(self.site_stg_1_item_locator)
        self.search_icon = super().get_element(self.search_icon_locator)
        self.ddb_package_name = super().get_element(self.ddb_package_name_locator)
        self.item = super().get_element(self.item_locator)
        self.add_to_cart = super().get_element(self.add_to_cart_locator)
        self.label_price_minicart = super().get_element(self.label_price_minicart_locator)
        self.icon_remove = super().get_element(self.icon_remove_locator)
        self.tips_empty = super().get_element(self.tips_empty_locator)
        self.Qty_box = super().get_element(self.Qty_box_locator)
        self.Qty_1 = super().get_element(self.Qty_1_locator)
        self.label_3D = super().get_element(self.label_3D_locator)
        self.btn_newNleaseDiscount = super().get_element(self.btn_newNleaseDiscount_locator)
        self.btn_sort = super().get_element(self.btn_sort_locator)
        self.label_sort_publishedDate = super().get_element(self.label_sort_publishedDate_locator)
