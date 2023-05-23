from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    publish_event_locator = (By.XPATH, "//*[@id=\"prepublication\"]/div/div/div/div[1]/div/div/button")
    btn_payment_provider_locator = (By.XPATH,"//button[@class=\"raised-btn_2vTjL538 raised-btn-blue_37QDrHj0 btn_3F6SBCy4 size-medium_3tC1AZkh width-full_2wWLBFy9\"]")
    self_locator =(By.XPATH,"//*[@id=\"prepublication\"]/div/div/div/div[1]/div/dl[1]/dd/div/div/div/div[1]")
    plus_and_plu_locator = (By.XPATH,"//*[@id=\"prepublication\"]/div/div/div/div[1]/div/dl[1]/div/div[2]/div[1]/div/button")
    no_limit_locator = (By.XPATH,"//*[@id=\"prepublication\"]/div/div/div/div[1]/div/dl[1]/div/div[2]/div[2]/div/button")
    bagevent_locator = (By.XPATH,"//*[@id=\"prepublication\"]/div/div/div/div[1]/div/dl[1]/dd/div/div/div/div[2]")
    mapping_locator = (By.XPATH,"//*[@id=\"prepublication\"]/div/div/div/div[1]/div/dl[1]/dd[2]/div/div/input")
    customize_locator =(By.XPATH,"//*[@id=\"prepublication\"]/div/div/div/div[1]/div/dl[1]/dd[1]/div/div/div/div[3]")
    customize_url_locator = (By.XPATH,"//*[@id=\"prepublication\"]/div/div/div/div[1]/div/dl[1]/dd[2]/div/div/input")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.publish_event = None
        self.btn_payment_provider = None
        self.self = None
        self.plus_and_plu = None
        self.no_limit = None
        self.bagevent = None
        self.mapping = None
        self.customize = None
        self.customize_url = None
        self.present_locator = self. publish_event_locator

    def init_elements(self):
        super().init_elements()
        self.publish_event = super().get_element(self.publish_event_locator)
        self.btn_payment_provider = super().get_element(self.btn_payment_provider_locator)
        self.self = super().get_element(self.self_locator)
        self.plus_and_plu = super().get_element(self.plus_and_plu_locator)
        self.no_limit = super().get_element(self.no_limit_locator)
        self.bagevent = super().get_element(self.bagevent_locator)
        self.mapping = super().get_element(self.mapping_locator)
        self.customize = super().get_element(self.customize_locator)
        self.customize = super().get_element(self.customize_locator)