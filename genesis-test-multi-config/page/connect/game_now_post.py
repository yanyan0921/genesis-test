from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    icon_status_locator = (By.CSS_SELECTOR,".triangle_20fmw_FF")
    select_status_locator = (By.XPATH, "//div[@value='in_dev']")
    select_genre_locator = (By.XPATH, "//*[@id=\"project-post\"]/div/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div/button")
    btn_post_now_locator = (By.XPATH, "//div[@class='button-wrapper_1LtVSqwf']/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.icon_status = None
        self.select_status = None
        self.select_genre = None
        self.btn_post_now= None
        self.present_locator = self.btn_post_now_locator

    def init_elements(self):
        super().init_elements()
        self.icon_status = super().get_element(self.icon_status_locator)
        self.select_status = super().get_element(self.select_status_locator)
        self.select_genre = super().get_element(self.select_genre_locator)
        self.btn_post_now = super().get_element(self.btn_post_now_locator)
