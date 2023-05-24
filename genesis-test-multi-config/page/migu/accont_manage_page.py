from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Page(BasePage):
    base_url = "https://cloud-platform.migu.cn/"
    account_manage_menu = (By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[1]/span')
    new_account_link_button = (By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/div[1]/div/div/div[1]/button')
    dev_account_input = (By.XPATH,
                         '//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/div[2]/div/form/div/div/div[2]/div/div/input')
    link_button = (By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/div[2]/div/div/div[3]/span/button[2]')
    account_search = (By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/div[1]/div/div/div[1]/div/input')
    cancel_link_button = (By.XPATH,
                          '//*[@id="app"]/section/section/main/div[2]/div/div[1]/div/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[7]/div/button')
    account_name_div = (By.XPATH,
                        '//*[@id="app"]/section/section/main/div[2]/div/div[1]/div/div/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[2]/div')
    nodata_text_div = (By.XPATH,
                       '//*[@id="app"]/section/section/main/div[2]/div/div[1]/div/div/div[3]/div/div[1]/div[3]/div/div[1]/div/div/span/div')
    dev_account = (By.XPATH, "//span[contains(text(),'mengran_3')]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.new_account_link_button = None
        self.dev_account_input = None
        self.dev_account = None
        self.link_button = None
        self.account_search = None
        self.account_name_div = None
        self.cancel_link_button = None
        self.confirm_cancel_button = None
        self.nodata_text_div = None
        self.account_manage_menu = self.account_manage_menu
        self.present_locator = self.account_manage_menu

    def init_elements(self):
        super().init_elements()
        self.account_manage_menu = super().get_element(self.account_manage_menu)
        self.new_account_link_button = super().get_element(self.new_account_link_button)
        self.dev_account_input = super().get_element(self.dev_account_input)
        self.dev_account = super().get_element(self.dev_account)
        self.link_button = super().get_element(self.link_button)
        self.account_search = super().get_element(self.account_search)
        self.account_name_div = super().get_element(self.account_name_div)
        self.cancel_link_button = super().get_element(self.cancel_link_button)
        self.confirm_cancel_button = super().get_element(self.confirm_cancel_button)
        self.nodata_text_div = super().get_element(self.nodata_text_div)
