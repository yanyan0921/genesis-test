from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-staging.unity.com"
    manage_seat_locator = (By.CSS_SELECTOR, "[class = 'action-ico ico-add-user tooltip open-alert']")
    label_edit_locator = (By.CSS_SELECTOR,"[class = 'action-ico ico-pencil tooltip open-alert']")
    input_box_locator = (By.CLASS_NAME,"fs14")
    label_delete_locator = (By.XPATH,"//*[@id=\"alert_edit_label\"]/div/div/div[2]/span/i")
    close_window_button_locator = (By.XPATH,"//*[@id=\"alert_edit_label\"]/div/h2/i")
    test_label_locator = (By.XPATH,"/html/body/div/section/div[3]/div/div[2]/div[4]/div[3]/table/tbody/tr/td[6]/div/span[1]")

    choose_filter_filterbox_locator = (By.XPATH,"/html/body/div/section/div[3]/div/div[2]/div[4]/div[2]/div[1]/div[4]/div/button/span[1]")
    extension_asset_locator = (By.XPATH,"/html/body/div/section/div[3]/div/div[2]/div[4]/div[2]/div[1]/div[4]/div/div/ul/li[4]/a/span[1]")
    license_name_locator = (By.CSS_SELECTOR,"[class = 'rel']")

    GameGlow_name_locator = (By.XPATH, "/html/body/div/section/div[3]/div/div[2]/div[4]/div[3]/table/tbody/tr/td[1]/a/div[1]")
    arrow_locator = (By.CSS_SELECTOR,"[class = 'action-ico ico-forward tooltip ml10 inbl']")
    the_second_user_locator = (By.XPATH, "//*[@id=\"alert_assign_revoke_seat\"]/div/div[5]/div[2]/div/div[4]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.manage_seat = None
        self.GameGlow_name = None
        self.label_edit = None
        self.input_box = None
        self.label_delete = None
        self.close_window_button = None
        self.test_label = None
        self.choose_filter_filterbox = None
        self.extension_asset = None
        self.license_name = None
        self.arrow = None
        self.the_second_user = None
        self.present_locator = self.GameGlow_name_locator

    def init_elements(self):
        super().init_elements()
        self.manage_seat = super().get_element(self.manage_seat_locator)
        self.GameGlow_name = super().get_element(self.GameGlow_name_locator)
        self.label_edit = super().get_element(self.label_edit_locator)
        self.input_box = super().get_element(self.input_box_locator)
        self.label_delete = super().get_element(self.label_delete_locator)
        self.close_window_button = super().get_element(self.close_window_button_locator)
        self.test_label = super().get_element(self.test_label_locator)
        self.choose_filter_filterbox = super().get_element(self.choose_filter_filterbox_locator)
        self.extension_asset = super().get_element(self.extension_asset_locator)
        self.license_name = super().get_element(self.license_name_locator)
        self.arrow = super().get_element(self.arrow_locator)
        self.the_second_user = super().get_element(self.the_second_user_locator)
