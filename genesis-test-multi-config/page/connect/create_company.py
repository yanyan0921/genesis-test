from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    input_company_name_locator = (By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/input")
    icon_company_name_locator = (By.CSS_SELECTOR, ".active_1tGpmPsf > .input_3yaUP2ah")
    error_company_locator = (By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/span")
    icon_type_locator = (By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/button/div/div[2]")
    select_type_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[7]")
    error_type_locator = (By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/span")
    icon_scale_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/button/div/div[2]")
    select_scale_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[5]")
    error_scale_locator =(By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/span")
    input_city_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/div/div/div/input")
    click_city_locator=(By.XPATH,"//div[@id='pageContent']/div/div[6]/div[2]/div/div/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/input")
    error_city_locator =(By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/span")
    input_website_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div[2]/div/input")
    error_website_locator = (By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/span")
    company_type_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[4]/div/div[2]/div[2]/div/div[1]/button")
    button_true_locator = (By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[3]/div/button[2]")
    error_msg_companyname_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[1]/div[6]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/span")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.icon_company_name = None
        self.input_company_name = None
        self.error_company = None
        self.icon_type = None
        self.select_type = None
        self.error_type = None
        self.icon_scale = None
        self.select_scale = None
        self.error_scale = None
        self.input_city = None
        self.click_city = None
        self.error_city = None
        self.input_website = None
        self.error_website = None
        self.company_type = None
        self.button_true = None
        self.error_msg_companyname = None
        self.present_locator = self.input_company_name_locator

    def init_elements(self):
        super().init_elements()
        self.icon_company_name = super().get_element(self.icon_company_name_locator)
        self.error_msg_companyname = super().get_element(self.error_msg_companyname_locator)
        self.input_company_name = super().get_element(self.input_company_name_locator)
        self.error_company = super().get_element(self.error_company_locator)
        self.icon_type = super().get_element(self.icon_type_locator)
        self.select_type = super().get_element(self.select_type_locator)
        self.error_type = super().get_element(self.error_type_locator)
        self.icon_scale = super().get_element(self.icon_scale_locator)
        self.select_scale = super().get_element(self.select_scale_locator)
        self.error_scale = super().get_element(self.error_scale_locator)
        self.input_city = super().get_element(self.input_city_locator)
        self.click_city = super().get_element(self.click_city_locator)
        self.error_city = super().get_element(self.error_city_locator)
        self.input_website = super().get_element(self.input_website_locator)
        self.input_website = super().get_element(self.input_website_locator)
        self.error_website = super().get_element(self.error_website_locator)
        self.button_true = super().get_element(self.button_true_locator)