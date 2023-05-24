from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://cloud-platform.migu.cn/"
    pool_manage_menu = (By.XPATH, '//*[@id="app"]/section/section/aside/ul/li[2]/span')
    create_pool_button = (By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/div/div/div/div[1]/button')
    pool_name_input = (
        By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/form/div/div/div[2]/div[2]/div/div/input')
    pool_type_input = (
        By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/form/div/div/div[2]/div[3]/div/div/div/div/div/input')
    pool_type = (By.XPATH, "//span[contains(text(),'弹性')]")
    pool_configuration_input = (
        By.XPATH,
        '//*[@id="app"]/section/section/main/div[2]/div/form/div/div/div[2]/div[4]/div[1]/div/div/div/div/input')
    pool_configuration = (By.XPATH, "//span[contains(text(),'PUB_3060_弹性')]")
    pool_configuration_number = (
        By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/form/div/div/div[2]/div[4]/div[2]/div/div/div/input')
    pool_description = (
        By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/form/div/div/div[2]/div[5]/div/div/textarea')
    create_button = (By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/h2/div[2]/button[1]')
    search_input = (By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/div/div/div/div[1]/div/input')
    pool_name_div = (By.XPATH,
                     '//*[@id="app"]/section/section/main/div[2]/div/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[2]/div')
    del_button = (By.XPATH,
                  '//*[@id="app"]/section/section/main/div[2]/div/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[7]/div/button[1]')
    confirm_del_button = (By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
    no_data_div = (By.XPATH,
                   '//*[@id="app"]/section/section/main/div[2]/div/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div/div/span/div')
    edit_info_button = (By.XPATH,
                        '//*[@id="app"]/section/section/main/div[2]/div/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[7]/div/button[2]')
    save_update_button = (By.XPATH, '//*[@id="app"]/section/section/main/div[2]/div/h2/div[2]/button[1]')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)

        self.url = self.base_url
        self.create_pool_button = None
        self.pool_name_input = None
        self.pool_type_input = None
        self.pool_type = None
        self.pool_configuration_input = None
        self.pool_configuration = None
        self.pool_configuration_number = None
        self.pool_description = None
        self.create_button = None
        self.search_input = None
        self.pool_name_div = None
        self.del_button = None
        self.confirm_del_button = None
        self.search_input = None
        self.no_data_div = None
        self.edit_info_button = None
        self.pool_name_input = None
        self.save_update_button = None
        self.pool_manage_menu = self.pool_manage_menu
        self.present_locator = self.pool_manage_menu

    def init_elements(self):
        super().init_elements()
        self.create_pool_button = super().get_element(self.create_pool_button)
        self.pool_name_input = super().get_element(self.pool_name_input)
        self.pool_type_input = super().get_element(self.pool_type_input)
        self.pool_type = super().get_element(self.pool_type)
        self.pool_configuration_input = super().get_element(self.pool_configuration_input)
        self.pool_configuration = super().get_element(self.pool_configuration)
        self.pool_configuration_number = super().get_element(self.pool_configuration_number)
        self.pool_description = super().get_element(self.pool_description)
        self.create_button = super().get_element(self.create_button)
        self.search_input = super().get_element(self.search_input)
        self.pool_name_div = super().get_element(self.pool_name_div)
        self.del_button = super().get_element(self.del_button)
        self.confirm_del_button = super().get_element(self.confirm_del_button)
        self.search_input = super().get_element(self.search_input)
        self.no_data_div = super().get_element(self.no_data_div)
        self.edit_info_button = super().get_element(self.edit_info_button)
        self.pool_name_input = super().get_element(self.pool_name_input)
        self.save_update_button = super().get_element(self.save_update_button)
        self.pool_manage_menu = super().get_element(self.pool_manage_menu)
