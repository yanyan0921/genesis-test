from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    choose_occupation_locator = (By.XPATH, "//*[@id=\"new_conversations_update_business_info_record_form\"]/div[1]/div/button")
    button_occupation_locator = (By.XPATH, "//*[@id=\"new_conversations_update_business_info_record_form\"]/div[1]/div/div/ul/li[2]/a/span[1]")
    input_company_name_locator = (By.ID, "conversations_update_business_info_record_form_company_name")
    choose_industry_locator = (By.XPATH, "//*[@id=\"new_conversations_update_business_info_record_form\"]/div[3]/div/button")
    button_industry_locator = (By.XPATH, "//*[@id=\"new_conversations_update_business_info_record_form\"]/div[3]/div/div/ul/li[2]/a/span[1]")
    button_save_locator = (By.XPATH, "//*[@id=\"new_conversations_update_business_info_record_form\"]/div[4]/input")
    button_accept_licence_locator = (By.XPATH, "//*[@id=\"new_conversations_accept_updated_tos_form\"]/div[3]/button[2]")
    button_accept_licence2_locator = (By.XPATH, "//*[@id=\"new_conversations_accept_updated_tos_form\"]/div[3]/button[1]")
    btn_unity_update1_locator = (By.XPATH, "//*[@id=\"new_conversations_accept_updated_tos_form\"]/div[2]/button[1]")
    btn_unity_update2_locator = (By.XPATH, "//*[@id=\"new_conversations_accept_updated_tos_form\"]/div[4]/button[2]")
    btn_unity_update3_locator = (By.XPATH, "//*[@id=\"new_conversations_accept_updated_tos_form\"]/div[4]/button[1]")

    btn_id_license1_locator = (By.XPATH, "//*[@id=\"new_conversations_accept_updated_tos_form\"]/div[3]/button[2]")
    btn_id_license2_locator = (By.XPATH, "//*[@id=\"new_conversations_accept_updated_tos_form\"]/div[3]/button[1]")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.choose_occupation = None
        self.button_occupation = None
        self.input_company_name = None
        self.choose_industry = None
        self.button_industry = None
        self.button_save = None
        self.button_accept_licence = None
        self.button_accept_licence2 = None
        self.btn_unity_update1 = None
        self.btn_unity_update2 = None
        self.btn_unity_update3 = None
        self.btn_id_license1 = None
        self.btn_id_license2 = None
        self.present_locator = self.choose_occupation_locator

    def init_elements(self):
        super().init_elements()
        self.choose_occupation = super().get_element(self.choose_occupation_locator)
        self.button_occupation = super().get_element(self.button_occupation_locator)
        self.input_company_name = super().get_element(self.input_company_name_locator)
        self.choose_industry = super().get_element(self.choose_industry_locator)
        self.button_industry = super().get_element(self.button_industry_locator)
        self.button_save = super().get_element(self.button_save_locator)
        self.button_accept_licence = super().get_element(self.button_accept_licence_locator)
        self.button_accept_licence2 = super().get_element(self.button_accept_licence2_locator)
        self.btn_unity_update1 = super().get_element(self.btn_unity_update1_locator)
        self.btn_unity_update2 = super().get_element(self.btn_unity_update2_locator)
        self.btn_unity_update3 = super().get_element(self.btn_unity_update3_locator)
        self.btn_id_license1 = super().get_element(self.btn_id_license1_locator)
        self.btn_id_license2 = super().get_element(self.btn_id_license2_locator)
