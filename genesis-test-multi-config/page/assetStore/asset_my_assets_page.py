from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    myAssets_title_locator = (By.CLASS_NAME,"_2NeyA")
    site_stg_1_locator = (By.CSS_SELECTOR,"[class = '_161YN _30Ec_']")
    add_label_btn_locator = (By.CLASS_NAME, '_2CO3_')
    input_label_box_locator = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div[4]/div/div/input')
    btn_save_locator = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div[6]/button[2]')
    verify_label_locator = (By.CLASS_NAME, 'le_6J')
    verify_btn_locator = (By.XPATH,
                            '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[5]/div[1]/div/div[3]/div[2]/div/div[1]/text()')
    edit_label_btn_locator = (By.CLASS_NAME, "_2CO3_")
    delete_label_btn_locator = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div[5]/div/div[1]/div[2]')
    label_verify_locator = (
    By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div[5]/div')



    skip_button_locator = (By.CLASS_NAME,"_3c34s")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.site_stg_1 = self.site_stg_1_locator
        self.skip_button = self.skip_button_locator
        self.add_label_btn = None
        self.input_label_box = None
        self.btn_save = None
        self.verify_label = None
        self.add_label_btn = None
        self.input_label_box = None
        self.btn_save = None
        self.verify_label = None
        self.verify_btn = None
        self.edit_label_btn = None
        self.delete_label_btn = None
        self.label_verify = None
        self.present_locator = self.myAssets_title_locator

    def init_elements(self):
        super().init_elements()
        self.myAssets_title = super().get_element(self.myAssets_title_locator)
        self.site_stg_1 = super().get_element(self.site_stg_1_locator)
        self.skip_button = super().get_element(self.skip_button_locator)
        self.add_label_btn = super().get_element(self.add_label_btn_locator)
        self.input_label_box = super().get_element(self.input_label_box_locator)
        self.btn_save = super().get_element(self.btn_save_locator)
        self.verify_label = super().get_element(self.verify_label_locator)
        self.verify_btn = super().get_element(self.verify_btn_locator)
        self.edit_label_btn = super().get_element(self.edit_label_btn_locator)
        self.delete_label_btn = super().get_element(self.delete_label_btn_locator)
        self.label_verify = super().get_element(self.label_verify_locator)


