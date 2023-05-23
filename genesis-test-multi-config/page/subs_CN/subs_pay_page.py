from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_weichat_pay_locator = (By.XPATH, "//*[@id=\"payment\"]/div[2]/div[2]/div[2]/dl[2]/dd/div/label")
    btn_weichat_pro_pay_locator = (By.XPATH, "//*[@id=\"payment\"]/div[2]/div[2]/div/dl[2]/dd/div/label")
    btn_c2c_pay_locator = (By.XPATH, "//*[@id=\"payment\"]/div[2]/div[2]/div/dl[3]/dd/div/label")
    btn_licence_locator = (By.XPATH, "//*[@id=\"summary_float\"]/div[1]/div[1]/div/div/label")
    btn_pay_now_locator = (By.XPATH, "//*[@id=\"summary_float\"]/div[1]/div[1]/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.btn_weichat_pay_locator
        self.btn_weichat_pay = None
        self.btn_weichat_pro_pay = None
        self.btn_c2c_pay = None
        self.btn_licence = None
        self.btn_pay_now = None


    def init_elements(self):
        super().init_elements()
        self.btn_weichat_pay = super().get_element(self.btn_weichat_pay_locator)
        self.btn_weichat_pro_pay = super().get_element(self.btn_weichat_pro_pay_locator)
        self.btn_c2c_pay = super().get_element(self.btn_c2c_pay_locator)
        self.btn_licence = super().get_element(self.btn_licence_locator)
        self.btn_pay_now = super().get_element(self.btn_pay_now_locator)
