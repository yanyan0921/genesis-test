from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    filter_assets_locator = (
        By.XPATH, '/html/body/div[1]/main/div/div[1]/div/div/div[2]/div/div[1]/div/div/button/span[1]/div/div/div')
    label_filter_assets_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div[1]/div/div/div[2]/div/div[1]/div/div/div[1]/button/span[1]/div/div/div')
    filter_time_locator = (
        By.XPATH, '//*[@id="app"]/main/div/div[1]/div/div/div[2]/div/div[2]/div/div/button/span[1]/div/div/div')
    icon_published_only_locator = (By.CLASS_NAME, 'jss5459 MuiSwitch-input')
    input_filter_search_locator = (By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/input')
    icon_filter_allAssets_locator = (By.XPATH,'/html/body/div[4]/div[3]/div/div[3]/div/div[1]/div/label/span[1]/span[1]/input')
    icon_filter_asset1_locator = (
        By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div/div[2]/div/label/span[1]/span[1]/input')
    icon_filter_asset2_locator = (
        By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div/div[3]/div/label/span[1]/span[1]/input')
    btn_create_preset_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[4]/div[1]/div/a/span[1]')
    input_preset_name_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[4]/div[1]/div/input')
    btn_presetOK_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[4]/div[2]/div[2]/a/span[1]')
    label_preset_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div/div[1]/div/div/label/span[2]')
    icon_preset_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div/div[1]/div/button/span[1]/svg')
    btn_preset_edit_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/div/p[1]')
    btn_preset_delete_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/div/p[2]')
    input_preset_name_edit_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div/input')
    icon_filter_asset4_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/div/div[5]/div/label/span[2]')
    btn_save_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div[2]/div[2]/a/span[1]')
    btn_remove_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/div/p[2]')
    label_preset_intro_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/div/p[2]')
    icon_cookies_locator = (By.XPATH, '/html/body/div[3]/div[3]/div/header/h2/span')
    btn_apply_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/div[4]/div[2]/div[2]/a/span[1]')
    label_searched_assets1_locator = (
        By.XPATH, '/html/body/div[1]/main/div/div[2]/div[3]/div/div[2]/div[2]/dl/dd[1]/div/p/a')
    label_searched_assets2_locator = (
        By.XPATH, '/html/body/div[1]/main/div/div[2]/div[3]/div/div[2]/div[3]/dl/dd[1]/div/p/a')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.filter_assets = None
        self.label_filter_assets = None
        self.filter_time = None
        self.icon_published_only = None
        self.input_filter_search = None
        self.icon_filter_allAssets = None
        self.icon_filter_asset1 = None
        self.icon_filter_asset2 = None
        self.btn_create_preset = None
        self.input_preset_name = None
        self.btn_presetOK = None
        self.label_preset = None
        self.icon_preset = None
        self.btn_preset_edit = None
        self.btn_preset_delete = None
        self.input_preset_name_edit = None
        self.icon_filter_asset4 = None
        self.btn_save = None
        self.btn_remove = None
        self.label_preset_intro = None
        self.icon_cookies = None
        self.btn_apply = None
        self.label_searched_assets1 = None
        self.label_searched_assets2 = None
        self.present_locator = self.filter_assets_locator

    def init_elements(self):
        super().init_elements()
        self.filter_assets = super().get_element(self.filter_assets_locator)
        self.label_filter_assets = super().get_element(self.label_filter_assets_locator)
        self.filter_time = super().get_element(self.filter_time_locator)
        self.icon_published_only = super().get_element(self.icon_published_only_locator)
        self.input_filter_search = super().get_element(self.input_filter_search_locator)
        self.icon_filter_allAssets = super().get_element(self.icon_filter_allAssets_locator)
        self.icon_filter_asset1 = super().get_element(self.icon_filter_asset1_locator)
        self.icon_filter_asset2 = super().get_element(self.icon_filter_asset2_locator)
        self.btn_create_preset = super().get_element(self.btn_create_preset_locator)
        self.input_preset_name = super().get_element(self.input_preset_name_locator)
        self.btn_presetOK = super().get_element(self.btn_presetOK_locator)
        self.label_preset = super().get_element(self.label_preset_locator)
        self.icon_preset = super().get_element(self.icon_preset_locator)
        self.btn_preset_edit = super().get_element(self.btn_preset_edit_locator)
        self.btn_preset_delete = super().get_element(self.btn_preset_delete_locator)
        self.input_preset_name_edit = super().get_element(self.input_preset_name_edit_locator)
        self.icon_filter_asset4 = super().get_element(self.icon_filter_asset4_locator)
        self.btn_save = super().get_element(self.btn_save_locator)
        self.btn_remove = super().get_element(self.btn_remove_locator)
        self.label_preset_intro = super().get_element(self.label_preset_intro_locator)
        self.icon_cookies = super().get_element(self.icon_cookies_locator)
        self.btn_apply = super().get_element(self.btn_apply_locator)
        self.label_searched_assets1 = super().get_element(self.label_searched_assets1_locator)
        self.label_searched_assets2 = super().get_element(self.label_searched_assets2_locator)
