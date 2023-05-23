from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    platform_yes_btn_locator = (By.XPATH, "//*[@id=\"testFormSpecificPlatform\"]/dl/dd[2]/label/span[1]")
    platform_item_locator = (By.XPATH,"//*[@id=\"testFormSpecificPlatform\"]/dl/dd[2]/dl/dd[1]/label/span[2]")
    editor_yes_btn_locator = (By.XPATH,"//*[@id=\"testFormSpecificVersion\"]/dl/dd[2]/label/span[1]")
    editor_item_locator = (By.XPATH,"//*[@id=\"testFormSpecificVersion\"]/dl/dd[2]/dl/dd[4]/label/span[2]")
    srp_select_locator = (By.XPATH, "//*[@id=\"testFormSrps\"]/dl/dd/dl/dd[3]/label/span[1]")
    save_btn_locator = (By.ID,"saveVersionTest")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.platform_yes_btn = None
        self.platform_item = None
        self.editor_yes_btn = None
        self.editor_item = None
        self.save_btn = None
        self.srp_select = None
        self.present_locator = self.save_btn_locator

    def init_elements(self):
        super().init_elements()
        self.platform_yes_btn = super().get_element(self.platform_yes_btn_locator)
        self.platform_item = super().get_element(self.platform_item_locator)
        self.editor_yes_btn = super().get_element(self.editor_yes_btn_locator)
        self.editor_item = super().get_element(self.editor_item_locator)
        self.save_btn = super().get_element(self.save_btn_locator)
        self.srp_select = super().get_element(self.srp_select_locator)