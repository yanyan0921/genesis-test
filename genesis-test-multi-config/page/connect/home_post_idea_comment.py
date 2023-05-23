from typing import Tuple

from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-int.unity.com/"
    texterea_input_locator = (By.TAG_NAME, "textarea")
    button_comment_locator = (By.XPATH,"//button[@class=\"raised-btn_2vTjL538 raised-btn-blue_37QDrHj0 comment_dNPKlrrx\"]")
    icon_like_locator = (By.XPATH,"//button[@class=\"ifont ifont-icons-like like_3WKVIDhr\"]")
    icon_cancel_like_locator = (By.XPATH, "//button[@class=\"ifont ifont-icons-like like_3WKVIDhr liked_ezMb2bP_\"]")
    icon_delete_locator = (By.CLASS_NAME,"delete_8fTx-bqq")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.texterea_input = None
        self.button_comment = None
        self.icon_like = None
        self.icon_cancel_like = None
        self.icon_delete = None
        self.present_locator = self.texterea_input_locator


    def init_elements(self):
        super().init_elements()
        self.texterea_input = super().get_element(self.texterea_input_locator)
        self.button_comment = super().get_element(self.button_comment_locator)
        self.icon_like = super().get_element(self.icon_like_locator)
        self.icon_cancel_like = super().get_element(self.icon_cancel_like_locator)
        self.icon_delete = super().get_element(self.icon_delete_locator)