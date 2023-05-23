from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    publisher_title_locator = (By.XPATH, "//*[@id=\"publisherTitle\"]")
    package_tab_locator = (By.XPATH,"//*[@id=\"content-container\"]/nav/div[6]/ul/li[1]/a")
    create_new_package_btn_locator = (By.XPATH,"//*[@id=\"createNew\"]")

    link_text_0_locator = (By.XPATH,"//*[@id=\"content-container\"]/nav/div[1]")
    link_text_1_locator = (By.XPATH,"//*[@id=\"content-container\"]/nav/div[2]")
    link_text_2_locator = (By.XPATH,"//*[@id=\"content-container\"]/nav/div[3]")
    link_text_3_locator = (By.XPATH,"//*[@id=\"content-container\"]/nav/div[4]")
    link_text_4_locator = (By.XPATH,"//*[@id=\"content-container\"]/nav/div[5]")
    link_text_5_locator = (By.XPATH,"//*[@id=\"content-container\"]/nav/div[6]")
    link_text_6_locator = (By.XPATH,"//*[@id=\"content-container\"]/nav/div[7]")


    logout_tab_locator = (By.XPATH,"//*[@id=\"unav\"]/div/a[2]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.publisher_title = self.publisher_title_locator
        self.package_tab = self.package_tab_locator
        self.create_new_package_btn = None
        self.logout_tab = None
        self.link_text_0 = None
        self.link_text_1 = None
        self.link_text_2 = None
        self.link_text_3 = None
        self.link_text_4 = None
        self.link_text_5 = None
        self.link_text_6 = None
        self.present_locator = self.publisher_title_locator

    def init_elements(self):
        super().init_elements()
        self.publisher_title = super().get_element(self.publisher_title_locator)
        self.package_tab = super().get_element(self.package_tab_locator)
        self.create_new_package_btn = super().get_element(self.create_new_package_btn_locator)
        self.logout_tab = super().get_element(self.logout_tab_locator)

        self.link_text_0 = super().get_element(self.link_text_0_locator)
        self.link_text_1 = super().get_element(self.link_text_1_locator)
        self.link_text_2 = super().get_element(self.link_text_2_locator)
        self.link_text_3 = super().get_element(self.link_text_3_locator)
        self.link_text_4 = super().get_element(self.link_text_4_locator)
        self.link_text_5 = super().get_element(self.link_text_5_locator)