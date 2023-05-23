from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    input_reply_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/textarea')
    btn_post_reply_locator = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/button/span[1]')
    btn_cancel_reply_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[2]/div[3]/div/button/span[1]')
    btn_reply_post_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[2]/div[3]/div/button/span[1]')
    label_reply_content_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[2]/div[2]/p[2]')
    icon_history_locator = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[1]/div[3]/div/div[1]/button')
    label_reply_status_history_locator = (By.XPATH,'//*[@id="app"]/main/div/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/p/span')
    label_reply_content_history_locator = (
    By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div/div/div/div/p')
    btn_edit_locator = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/button/span[1]')
    btn_delete_locator = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/button/span[1]')
    title_locator = (By.CSS_SELECTOR, "[class = 'jss10 jss11 jss34']")
    btn_delete_ok_locator = (By.XPATH,'/html/body/div[3]/div[3]/div/div[3]/div[2]/button/span[1]')
    link_view_on_AS_locator = (By.XPATH, '//*[@id="app"]/main/div/div[1]/div/div/div[2]/div/button/span[1]')
    label_reviews_title_locator = (By.XPATH,'/html/body/div[1]/main/div/div[2]/div/div[1]/div[2]/h3')
    label_reviews_content_locator = (By.XPATH,'/html/body/div[1]/main/div/div[2]/div/div[1]/div[2]/div[1]')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.input_reply = None
        self.btn_post_reply = None
        self.btn_cancel_reply = None
        self.btn_reply_post = None
        self.label_reply_content = None
        self.icon_history = None
        self.label_reply_status_history = None
        self.label_reply_content_history = None
        self.btn_edit = None
        self.btn_delete = None
        self.btn_delete_ok = None
        self.link_view_on_AS = None
        self.label_reviews_title = None
        self.label_reviews_content = None

        self.present_locator = self.title_locator

    def init_elements(self):
        super().init_elements()
        self.input_reply = super().get_element(self.input_reply_locator)
        self.btn_post_reply = super().get_element(self.btn_post_reply_locator)
        self.btn_cancel_reply = super().get_element(self.btn_cancel_reply_locator)
        self.btn_reply_post = super().get_element(self.btn_reply_post_locator)
        self.label_reply_content = super().get_element(self.label_reply_content_locator)
        self.icon_history = super().get_element(self.icon_history_locator)
        self.label_reply_status_history = super().get_element(self.label_reply_status_history_locator)
        self.label_reply_content_history = super().get_element(self.label_reply_content_history_locator)
        self.btn_edit = super().get_element(self.btn_edit_locator)
        self.btn_delete = super().get_element(self.btn_delete_locator)
        self.btn_delete_ok = super().get_element(self.btn_delete_ok_locator)
        self.link_view_on_AS = super().get_element(self.link_view_on_AS_locator)
        self.label_reviews_title = super().get_element(self.label_reviews_title_locator)
        self.label_reviews_content = super().get_element(self.label_reviews_content_locator)

