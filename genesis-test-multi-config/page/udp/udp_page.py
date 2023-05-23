from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    btn_myGame_locator=(By.XPATH,".//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[1]/div/div/span")
    btn_partnerStores_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[2]/div/div/span")
    btn_notification_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[2]/div[1]/div/div/div/span")
    btn_logOut_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[2]/div[2]/div/div/div/div/div")
    btn_orgList_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[2]/div[3]/div/div/div/div")
    btn_createGame_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[2]/div[2]/div/div/div[1]")
    btn_selectLanguage_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[3]/span")
    btn_existgamename_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[2]/div[2]/a[1]/div/div[2]")



    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_myGame = None
        self.btn_partnerStores = None
        self.btn_notification = None
        self.btn_logOut = None
        self.btn_orgList = None
        self.btn_createGame = None
        self.btn_selectLanguage = None
        self.btn_existgamename = None
        self.present_locator = self.btn_selectLanguage_locator

    def init_elements(self):
        super().init_elements()
        self.btn_myGame = super().get_element(self.btn_myGame_locator)
        self.btn_partnerStores = super().get_element(self.btn_partnerStores_locator)
        self.btn_notification = super().get_element(self.btn_partnerStores_locator)
        self.btn_logOut = super().get_element(self.btn_logOut_locator)
        self.btn_orgList = super().get_element(self.btn_orgList_locator)
        self.btn_createGame = super().get_element(self.btn_createGame_locator)
        self.btn_selectLanguage = super().get_element(self.btn_selectLanguage_locator)
        self.btn_existgamename = super().get_element(self.btn_existgamename_locator)


