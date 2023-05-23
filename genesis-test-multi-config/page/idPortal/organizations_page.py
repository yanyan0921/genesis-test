from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-staging.unity.com/en/organizations"
    verify_tip_org_locator = (By.LINK_TEXT,"Verify tip")
    order_request_org_locator = (By.LINK_TEXT, "order request")
    Add_new_locator = (By.CSS_SELECTOR,"[class = 'btn s bg-gr ico ico-plus']")
    the_first_org_locator = (By.XPATH,"//*[@id=\"content-wrapper\"]/div/div[2]/div[2]/div/div[1]/a")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.order_request_org = None
        self.verify_tip_org = None
        self.Add_new = self.Add_new_locator
        self.the_first_org = self.the_first_org_locator
        self.present_locator = self.Add_new_locator

    def init_elements(self):
        super().init_elements()
        self.order_request_org = super().get_element(self.order_request_org_locator)
        self.Add_new = super().get_element(self.Add_new_locator)
        self.verify_tip_org = super().get_element(self.verify_tip_org_locator)
        self.the_first_org = super().get_element(self.the_first_org_locator)







