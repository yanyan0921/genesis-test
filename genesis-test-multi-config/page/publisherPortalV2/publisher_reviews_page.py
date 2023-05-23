from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_filter_locator = (
        By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div/div/div[2]/div/div/div[1]/button/span[1]')
    label_status_locator = ( By.XPATH, '/html/body/div[3]/div[3]/ul/div[3]/div/span')
    label_unreplied_locator = (
        By.XPATH, '/html/body/div[3]/div[3]/div/ul/div[2]/div/span')
    reviews_locator = (By.CSS_SELECTOR, "[class = 'jss10 jss23 jss13 jss32 jss26 jss34']")
    input_reply_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/textarea')
    btn_post_reply_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[2]/div[3]/div/button/span[1]')
    label_reply_content_locator = ( By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[2]/div[2]/p[2]')
    icon_history_locator = ( By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[3]/div/div[1]/button/span[1]/svg')
    label_reply_status_history_locator = (By.CSS_SELECTOR, "[class = 'jss713 jss10 jss14 jss32']")
    label_reply_content_history_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div/div/div/div/p')
    btn_edit_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/button/span[1]')
    btn_delete_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/button/span[1]')
    title_locator = (By.CSS_SELECTOR,"[class = 'jss10 jss11 jss34']")
    input_search_locator = (By.XPATH,'/html/body/div[1]/main/div/div[2]/div[1]/div/div/input')
    label_reviews_status_locator = (By.XPATH,'//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/dl/dd[3]/div/p')
    label_assets_locator = (By.XPATH, '/html/body/div[3]/div[3]/ul/div[1]/div/span')
    input_assets_name_locator = (By.XPATH, '/html/body/div[3]/div[3]/div[1]/div[2]/div/input')
    checkbox_assets_locator = (By.XPATH, '/html/body/div[3]/div[3]/div[1]/div[3]/div[1]/div/div/div[1]/div/label/span[1]/span[1]/input')
    btn_apply_locator = (By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div[2]/button/span[1]')
    label_assets_name_locator = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div/div[1]/dl/dd[1]/div/div[2]/h4')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_filter = None
        self.label_status = None
        self.label_unreplied = None
        self.reviews = None
        self.input_reply = None
        self.btn_post_reply = None
        self.label_reply_content = None
        self.icon_history = None
        self.label_reply_status_history = None
        self.label_reply_content_history = None
        self.btn_edit = None
        self.btn_delete = None
        self.checkbox_assets = None
        self.label_reviews_status = None
        self.label_assets = None
        self.input_assets_name = None
        self.btn_apply = None
        self.label_assets_name = None

        self.present_locator = self.title_locator

    def init_elements(self):
        super().init_elements()
        self.btn_filter = super().get_element(self.btn_filter_locator)
        self.label_status = super().get_element(self.label_status_locator)
        self.label_unreplied = super().get_element(self.label_unreplied_locator)
        self.reviews = super().get_element(self.reviews_locator)
        self.input_reply = super().get_element(self.input_reply_locator)
        self.btn_post_reply = super().get_element(self.btn_post_reply_locator)
        self.label_reply_content = super().get_element(self.label_reply_content_locator)
        self.icon_history = super().get_element(self.icon_history_locator)
        self.label_reply_status_history = super().get_element(self.label_reply_status_history_locator)
        self.label_reply_content_history = super().get_element(self.label_reply_content_history_locator)
        self.btn_edit = super().get_element(self.btn_edit_locator)
        self.btn_delete = super().get_element(self.btn_delete_locator)
        self.input_search = super().get_element(self.input_search_locator)
        self.icon_history = super().get_element(self.icon_history_locator)
        self.label_reviews_status = super().get_element(self.label_reviews_status_locator)
        self.label_assets = super().get_element(self.label_assets_locator)
        self.input_assets_name = super().get_element(self.input_assets_name_locator)
        self.checkbox_assets = super().get_element(self.checkbox_assets_locator)
        self.btn_apply = super().get_element(self.btn_apply_locator)

        self.label_assets = super().get_element(self.label_assets_locator)
        self.input_assets_name = super().get_element(self.input_assets_name_locator)
        self.checkbox_assets = super().get_element(self.checkbox_assets_locator)
        self.btn_apply = super().get_element(self.btn_apply_locator)
        self.label_assets_name = super().get_element(self.label_assets_name_locator)
