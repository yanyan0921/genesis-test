from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    input_packageName_locator = (By.XPATH, "//*[@id=\"search-incomming\"]/input")
    packages_tab_text_locator = (By.CSS_SELECTOR,"[class = 'item icob vettingIcon selected']")
    package_menu_locator = (By.XPATH,"/html/body/div[3]/div/section/article[2]/section/div/div/article/div[3]/div[1]/div/article[1]/div[15]")
    metaPackage_menu_locator = (By.XPATH, "/html/body/div[3]/div/section/article[2]/section/div/div[1]/article/div[3]/div/div/article/div[16]")
    accept_package_locator = (By.XPATH,"/html/body/div[4]/div/div[12]/div[2]")
    decline_package_locator = (By.XPATH,"/html/body/div[4]/div/div[13]/div[2]")
    accept_decline_btn_locator = (By.XPATH,"/html/body/div[1]/div/section/article[2]/section/div/div[1]/article/div[5]/div[2]/div[2]/div[2]/form/div[4]/label[1]/div")
    btn_account_locator = (By.XPATH, "/html/body/div[3]/header/nav/ul/li[3]")
    logout_tab_locator = (By.XPATH, "/html/body/div[4]/div[3]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.input_packageName = None
        self.package_menu = None
        self.metaPackage_menu = None
        self.packages_tab_text = None
        self.accept_package = None
        self.decline_package = None
        self.accept_decline_btn = None
        self.btn_account = None
        self.logout_tab = None
        self.present_locator = self.packages_tab_text_locator

    def init_elements(self):
        super().init_elements()
        self.input_packageName = super().get_element(self.input_packageName_locator)
        self.package_menu = super().get_element(self.package_menu_locator)
        self.metaPackage_menu = super().get_element(self.metaPackage_menu_locator)
        self.packages_tab_text = super().get_element(self.packages_tab_text_locator)
        self.accept_package = super().get_element(self.accept_package_locator)
        self.decline_package = super().get_element(self.decline_package_locator)
        self.accept_decline_btn= super().get_element(self.accept_decline_btn_locator)
        self.btn_account = super().get_element(self.btn_account_locator)
        self.logout_tab = super().get_element(self.logout_tab_locator)