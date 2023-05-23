from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_select_org_locator = (By.XPATH, "//*[@id=\"org-18966698513222\"]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_select_org = self.btn_select_org_locator
        # please import variable instead of importing rest directly
        # self.org_id = "org-" + gl.get_value('orgId')
        # self.path = "//*[@id=\"" + self.org_id + "\"]/a"
        self.btn_select_org_locator1 = (By.XPATH, self.path)
        self.btn_select_org_1 = self.btn_select_org_locator1
        self.logger.info(self.btn_select_org_1)
        self.present_locator = self.btn_select_org_locator1

    def init_elements(self):
        super().init_elements()
        self.btn_select_org = super().get_element(self.btn_select_org_locator)
        self.btn_select_org_1 = super().get_element(self.btn_select_org_locator1)
