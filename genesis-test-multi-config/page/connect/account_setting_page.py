from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-int.unity.com/en/account/edit"
    icon_switcher_locator = (By.XPATH,"//i[@class=\"m-icons icon-switcher\"]")
    select_connect_locator = (By.XPATH,"/html/body/div[1]/header/div/div[2]/div[2]/div/a[3]/span")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.icon_switcher = None
        self.select_connect = None
        self.present_locator = self.icon_switcher_locator


    def init_elements(self):
        super().init_elements()
        self.icon_switcher = super().get_element(self.icon_switcher_locator)
        self.select_connect = super().get_element(self.select_connect_locator)