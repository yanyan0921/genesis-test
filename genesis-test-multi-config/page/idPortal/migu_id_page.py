from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Page(BasePage):
    base_url = "https://cloud-platform.migu.cn/#/login?next=/home"
    decline_btn_locator = (By.XPATH, '//*[@id="content-wrapper"]/div/div/div/div/ul/li[2]/a')
    login_btn_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/div/form/button')
    input_username_locator = (By.XPATH, '//*[@id="username"]')
    input_password_locator = (By.XPATH, '//*[@id="password"]')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_username = None
        self.input_password = None
        self.login_btn = None
        self.decline_btn = self.decline_btn_locator
        self.present_locator = self.decline_btn_locator

    def init_elements(self):
        super().init_elements()
        self.decline_btn = super().get_element(self.decline_btn_locator)
        self.input_username = super().get_element(self.input_username_locator)
        self.input_password = super().get_element(self.input_password_locator)
        self.login_btn = super().get_element(self.login_btn_locator)
