from page.base_page import BasePage
from selenium.webdriver.common.by import By

class Page(BasePage):
    icon_sign_in_locator = (By.XPATH, "//*[@id=\"main-header\"]/div/div/a[3]")
    btn_sign_in_locator = (By.XPATH, "//*[@id=\"user-panel\"]/div/div/a[1]")
    btn_plus_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[2]/a")
    btn_No_Thanks_locator = (By.XPATH, "//*[@id=\"modalPlanPro\"]/div/div[2]/div[2]/a[2]")
    btn_plus_yes_locator = (By.XPATH, "/html/body/div[1]/div/section/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[3]/div[3]/div[1]/div/a[1]")
    btn_plus_subscribe_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div[3]/div[2]/div[2]/a[1]")
    btn_pro_locator = (By.XPATH, "/html/body/div[1]/div/section/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/a[1]")
    btn_go_pro_locator = (By.LINK_TEXT, "Go Pro")
    btn_upgrade_pro_locator = (By.XPATH, '/html/body/div[1]/div/section/div[1]/section[2]/div/div/div[1]/div/div/div[2]/a[1]')
    btn_upgrade_enterprise_locator = (By.XPATH, '/html/body/div[1]/div/section/div[1]/section[2]/div/div/div[2]/div/div/div[2]/a[1]')
    btn_cookie_locator = (By.XPATH, "//*[@id=\"onetrust-close-btn-container\"]/button")
    btn_revenue_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[3]/div[3]/div[1]/div/a[1]")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_plus = None
        self.btn_No_Thanks = None
        self.btn_plus_yes = None
        self.btn_plus_subscribe = None
        self.btn_pro = None
        self.btn_sign_in = None
        self.icon_sign_in = None
        self.btn_sign_in = None
        self.btn_go_pro = None
        self.btn_upgrade_pro = None
        self.btn_upgrade_enterprise = None
        self.btn_cookie = None
        self.btn_revenue = None
        self.present_locator = self.icon_sign_in_locator

    def init_elements(self):
        super().init_elements()
        self.btn_plus = super().get_element(self.btn_plus_locator)
        self.btn_No_Thanks = super().get_element(self.btn_No_Thanks_locator)
        self.btn_plus_yes = super().get_element(self.btn_plus_yes_locator)
        self.btn_plus_subscribe = super().get_element(self.btn_plus_subscribe_locator)
        self.btn_pro = super().get_element(self.btn_pro_locator)
        self.icon_sign_in = super().get_element(self.icon_sign_in_locator)
        self.btn_sign_in = super().get_element(self.btn_sign_in_locator)
        self.btn_go_pro = super().get_element(self.btn_go_pro_locator)
        self.btn_upgrade_pro = super().get_element(self.btn_upgrade_pro_locator)
        self.btn_upgrade_enterprise = super().get_element(self.btn_upgrade_enterprise_locator)
        self.btn_cookie = super().get_element(self.btn_cookie_locator)
        self.btn_revenue = super().get_element(self.btn_revenue_locator)
