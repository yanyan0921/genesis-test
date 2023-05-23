from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    title_locator = (By.CLASS_NAME, '_1dKGw')
    Saved_for_Later_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/h1')
    item_price_locator = (By.CLASS_NAME, "mErEH _223RA")
    remove_btn_locator=(By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div/a/div[1]/div[2]/div[1]/div/div')
    lable_Nothing_saved_locator = (By.XPATH,
                         '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]')
    btn_test_title_locator = (By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/div/div[3]/div/div/div/div/div[3]/a/div[2]/div[1]')
    icon_Privacy_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[1]')
    icon_Public_locator = (By.XPATH, '/html/body/div[8]/div/div[2]/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div')
    btn_save_locator = (By.CLASS_NAME, '_3UE3J pDJt- auto IaiTq')
    icon_share_locator = (By.CLASS_NAME, "_3kYVA")
    label_share_locator = (By.CLASS_NAME, "_2zufb")
    icon_close_locator = (By.CLASS_NAME, "ifont ifont-close _2E9BH")
    icon_setting_locator = (By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div[3]')
    input_list_name_locator = (By.CLASS_NAME, "_1gSGR")
    input_description_locator = (By.XPATH, '/html/body/div[8]/div/div[2]/div/div/div[1]/div/div/div[3]/div[2]/div[2]/div/div[1]/textarea')
    label_title_locator = (By.CLASS_NAME, "_39YUl")
    label_description_locator = (By.CLASS_NAME, "_15pxZ")
    btn_delete_list_locator = (By.CLASS_NAME, "_1lTqV")
    btn_yes_locator = (By.CLASS_NAME, "_3UE3J _3zD70 auto _27Drk")
    icon_compare_close_locator = (By.CSS_SELECTOR, "[class = 'uty-2-10-compBar-close']")


    def __init__(self,driver, wait):
        super().__int__(driver, wait)
        self.title = self.title_locator
        self.Saved_for_Later = None
        self.lable_Nothing_saved = None
        self.item_price = self.item_price_locator
        self.remove_btn = self.remove_btn_locator
        self.btn_test_title = None
        self.icon_Privacy = None
        self.icon_Public = None
        self.btn_save = None
        self.icon_share = None
        self.label_share = None
        self.icon_close = None
        self.icon_setting = None
        self.input_list_name = None
        self.input_description = None
        self. btn_delete_list = None
        self.btn_yes = None
        self.label_description = None
        self.icon_compare_close = None

        self.present_locator = self.title_locator

    def init_elements(self):
        super().init_elements()
        self.title= super().get_element(self.title_locator)
        self.Saved_for_Later = super().get_element(self.Saved_for_Later_locator)
        self.lable_Nothing_saved = super().get_element(self.lable_Nothing_saved_locator)
        self.item_price = super().get_element(self.item_price_locator)
        self.btn_test_title = super().get_element(self.btn_test_title_locator)
        self.icon_Privacy = super().get_element(self.icon_Privacy_locator)
        self.icon_Public = super().get_element(self.icon_Public_locator)
        self.btn_save = super().get_element(self.btn_save_locator)
        self.icon_share = super().get_element(self.icon_share_locator)
        self.label_share = super().get_element(self.label_share_locator)
        self.icon_close = super().get_element(self.icon_close_locator)
        self.icon_setting = super().get_element(self.icon_setting_locator)
        self.input_list_name = super().get_element(self.input_list_name_locator)
        self.input_description = super().get_element(self.input_description_locator)
        self.label_title = super().get_element(self.label_title_locator)
        self.label_description = super().get_element(self.label_description_locator)
        self. btn_delete_list = super().get_element(self. btn_delete_list_locator)
        self.btn_yes = super().get_element(self.btn_yes_locator)
        self.remove_btn = super().get_element(self.remove_btn_locator)
        self.icon_compare_close = super().get_element(self.icon_compare_close_locator)

