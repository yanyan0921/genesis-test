from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    version_changes_input_locator = (By.ID, "notes")
    save_btn_locator = (By.ID,"saveVersion")
    category_select_box_locator = (By.XPATH,"//*[@id=\"categoryWrap\"]/dd/div[1]/div[1]")
    model3D_characters_locator = (By.XPATH,"//*[@id=\"categoryWrap\"]/dd/div[1]/div[2]/div/div[1]")
    detail_edit_ok_btn_locator = (By.XPATH,"/html/body/div[4]/div[2]/div/input")

    metadata_edit_locator = (By.XPATH,"//*[@id=\"metadata\"]/div[2]/div[1]/dl[2]/dd[2]/a")
    keyImages_edit_locator = (By.XPATH,"//*[@id=\"metadata\"]/div[2]/div[1]/dl[2]/dd[3]/a")

    delete_draft_locator = (By.XPATH,"//*[@id=\"deleteVersionBtn\"]")
    delete_draft_ok_btn_locator = (By.XPATH,"/html/body/div[4]/div[2]/div[2]/input")

    pacman_package_remove_locator =(By.CLASS_NAME,"btn-remove")
    pacman_package_srp_edit_locator = (By.CLASS_NAME,"btn-edit")
    protocol_checkbox_locator = (By.XPATH,"//*[@id=\"agreeWrap\"]/span[1]")
    submit_btn_locator = (By.ID,"submitPackageBtn")
    submit_ok_btn_locator = (By.XPATH,"/html/body/div[4]/div[3]/div[2]/input")



    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.version_changes_input = self.version_changes_input_locator
        self.category_select_box = None
        self.delete_draft = None
        self.delete_draft_ok_btn = None
        self.model3D_characters = None
        self.delete_draft_ok_btn = None
        self.detail_edit_ok_btn = None
        self.metadata_edit = None
        self.keyImages_edit = None
        self.pacman_package_remove = None
        self.pacman_package_srp_edit = None
        self.submit_btn = None
        self.protocol_checkbox = None
        self.submit_ok_btn = None
        self.present_locator = self.save_btn_locator

    def init_elements(self):
        super().init_elements()
        self.version_changes_input = super().get_element(self.version_changes_input_locator)
        self.save_btn = super().get_element(self.save_btn_locator)
        self.category_select_box = super().get_element(self.category_select_box_locator)
        self.delete_draft = super().get_element(self.delete_draft_locator)
        self.delete_draft_ok_btn = super().get_element(self.delete_draft_ok_btn_locator)
        self.model3D_characters = super().get_element(self.model3D_characters_locator)
        self.detail_edit_ok_btn = super().get_element(self.detail_edit_ok_btn_locator)
        self.metadata_edit = super().get_element(self.metadata_edit_locator)
        self.keyImages_edit = super().get_element(self.keyImages_edit_locator)
        self.pacman_package_remove = super().get_element(self.pacman_package_remove_locator)
        self.pacman_package_srp_edit = super().get_element(self.pacman_package_srp_edit_locator)
        self.submit_btn = super().get_element(self.submit_btn_locator)
        self.submit_ok_btn = super().get_element(self.submit_ok_btn_locator)
        self.protocol_checkbox = super().get_element(self.protocol_checkbox_locator)