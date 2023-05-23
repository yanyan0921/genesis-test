from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-staging.unity.com"
    selectAll_checkbox_locator = (By.XPATH, "//*[@id=\"alert_assign_revoke_seat\"]/div/div[4]/div[1]/div/label")
    Assign_Seat_button_locator = (By.XPATH,"//*[@id=\"alert_assign_revoke_seat\"]/div/div[4]/div[2]/button[2]")
    Revoke_Seat_button_locator =(By.XPATH,"//*[@id=\"alert_assign_revoke_seat\"]/div/div[4]/div[2]/button[1]")
    close_window_button_locator = (By.CSS_SELECTOR,"[class = 'close-alert page-close-btn']")
    the_first_user_locator =(By.XPATH,"//*[@id=\"alert_assign_revoke_seat\"]/div/div[5]/div[1]/div/div[4]/a")
    the_second_user_locator =(By.XPATH,"//*[@id=\"alert_assign_revoke_seat\"]/div/div[5]/div[2]/div/div[4]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.selectAll_checkbox = self.selectAll_checkbox_locator
        self.Assign_Seat_button = None
        self.Revoke_Seat_button = None
        self.close_window_button = None
        self.the_first_user = None
        self.the_second_user = None
        self.present_locator = self.selectAll_checkbox_locator

    def init_elements(self):
        super().init_elements()
        self.selectAll_checkbox = super().get_element(self.selectAll_checkbox_locator)
        self.Assign_Seat_button = super().get_element(self.Assign_Seat_button_locator)
        self.Revoke_Seat_button = super().get_element(self.Revoke_Seat_button_locator)
        self.close_window_button = super().get_element(self.close_window_button_locator)
        self.the_first_user = super().get_element(self.the_first_user_locator)
        self.the_second_user = super().get_element(self.the_second_user_locator)
