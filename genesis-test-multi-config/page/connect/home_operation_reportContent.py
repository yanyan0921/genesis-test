from typing import Tuple

from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-internal.unity.com/"
    radio_Spam_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[3]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div/button")
    radio_copy_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[3]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[2]/div/button")
    radio_offension_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[3]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[3]/div/button")
    radio_adult_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[3]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[4]/div/button")
    radio_other_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[3]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[5]/div[1]/div/button")
    input_other_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[3]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[5]/div[2]/div/input")
    btn_submit_locator = (By.XPATH,"//*[@id=\"pageContent\"]/div[3]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.radio_Spam = None
        self.radio_copy = None
        self.radio_offension = None
        self.radio_adult = None
        self.radio_other = None
        self.input_other = None
        self.btn_submit = None
        self.present_locator = self.btn_submit_locator

    def init_elements(self):
        super().init_elements()
        self.radio_Spam = super().get_element(self.radio_Spam_locator)
        self.radio_copy = super().get_element(self.radio_copy_locator)
        self.radio_offension = super().get_element(self.radio_offension_locator)
        self.radio_adult = super().get_element(self.radio_adult_locator)
        self.radio_other = super().get_element(self.radio_other_locator)
        self.input_other = super().get_element(self.input_other_locator)
        self.btn_submit = super().get_element(self.btn_submit_locator)