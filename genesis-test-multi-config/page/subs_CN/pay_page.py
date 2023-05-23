from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_ali_login_locator = (By.XPATH, "//*[@id=\"J_tip_qr\"]/a")
    btn_wechat_qrcode_locator = (By.XPATH, "//*[@id=\"qrcode\"]/img")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.btn_ali_login_locator
        self.btn_ali_login = None
        self.btn_wechat_qrcode = None

    def init_elements(self):
        super().init_elements()
        self.btn_ali_login = super().get_element(self.btn_ali_login_locator)
        self.btn_wechat_qrcode = super().get_element(self.btn_wechat_qrcode_locator)
