from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    href_manage_seats_locator = (By.XPATH, "//*[@id=\"receiptApp\"]/div/div/div/div[1]/footer/a[1]")
    label_total_amount_locator = (By.XPATH, "//*[@id=\"receiptApp\"]/div/div/div/div[2]/div/div[2]/dl[3]/dd")
    label_total_tax_locator = (By.XPATH, "//*[@id=\"receiptApp\"]/div/div/div/div[2]/div/div[2]/dl[2]/dd")
    icon_overlay_locator = (By.ID, "init-overlay")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.href_manage_seats_locator
        self.label_total_amount = None
        self.label_total_tax = None
        self.href_manage_seats = self.href_manage_seats_locator

    def init_elements(self):
        super().init_elements()
        super().wait_for_element_hidden(self.icon_overlay_locator)
        super().wait_for_element_clickable(self.href_manage_seats_locator)
        self.href_manage_seats = super().get_element(self.href_manage_seats_locator)
        self.label_total_tax = super().get_element(self.label_total_tax_locator)
        self.label_total_amount = super().get_element(self.label_total_amount_locator)
