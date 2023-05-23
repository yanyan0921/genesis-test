from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    model3D_characters_locator = (By.XPATH, "//*[@id=\"categoryWrap\"]/dd/div[1]/div[2]/div/div[1]")
    detail_edit_ok_btn_locator = (By.XPATH, "/html/body/div[4]/div[2]/div/input")

    metadata_edit_locator = (By.XPATH, "//*[@id=\"metadata\"]/div[2]/div[1]/dl[2]/dd[2]/a")
    keyImages_edit_locator = (By.XPATH, "//*[@id=\"metadata\"]/div[2]/div[1]/dl[2]/dd[3]/a")

    delete_draft_locator = (By.XPATH, '/html/body/div[1]/main/div/header/div[1]/div[1]/div[2]/div[2]/button/span[1]')
    delete_draft_ok_btn_locator = (By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/div[2]/button/span[1]")

    pacman_package_remove_locator = (By.CLASS_NAME, "btn-remove")
    pacman_package_srp_locator = (By.XPATH,
                                  '/html/body/div[1]/main/div/div/div/div[1]/div[3]/div[3]/div[1]/div/div/div[1]/div/div/label[1]/span[1]/span/input')
    btn_srp2018_locator = (By.XPATH,'/html/body/div[1]/main/div/div/div/div[1]/div[3]/div[4]/div[1]/div/div/div/div/div/label[1]/span[1]/span/input')
    protocol_checkbox_locator = (By.XPATH, "//*[@id=\"agreeWrap\"]/span[1]")
    btn_unity_remove_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[3]/div[4]/div[1]/div/header/div[2]/div/button/span[1]')
    btn_remove_OK_locator = (By.XPATH, "/html/body/div[3]/div[3]/div/footer/div[2]/div[2]/button/span[1]")
    submit_btn_locator = (By.ID, "submitPackageBtn")
    submit_ok_btn_locator = (By.XPATH, "/html/body/div[4]/div[3]/div[2]/input")
    btn_refresh_package_locator = (
    By.XPATH, '//*[@id="app"]/main/div/div/div/div[1]/div[3]/div[1]/h4/div/button/span[1]')
    publisher_title_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[1]/header/h2/span')
    pacman_package_dependence_locator = (By.XPATH,
                                         '/html/body/div[1]/main/div/div/div/div[1]/div[3]/div[3]/div[1]/div/div/div[2]/div/div/label[1]/span[1]/span/input')
    pacman_additional_dependence_locator = (By.XPATH,
                                            '//*[@id="app"]/main/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/button/span[1]')
    icon_add_dependence_locator = (By.XPATH,
                                   '/html/body/div[1]/main/div/div/div/div[1]/div[3]/div[3]/div[1]/div/div/div[2]/div/div/label[1]/span[1]/span/input')
    input_package_dependence_locator = (By.ID, 'video_link')
    title_dependence_locator = (
    By.XPATH, '//*[@id="app"]/main/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]/h4')
    btn_save_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/div/div/div[2]/footer/button/span[1]')

    btn_description_locator = (
    By.XPATH, '/html/body/div[1]/main/div/header/div[2]/div/div[2]/div/button[3]/span[1]/span')
    input_summary_locator = (
        By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/div/div/div/textarea')
    input_Technical_Details_locator = (By.XPATH,
                                       '/html/body/div[1]/main/div/div/div/div[1]/div[4]/div[1]/div/div/div[2]/div/div/div/div/div/div')
    input_Description_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[3]/div/div/div/div[2]/div/div/div')
    btn_details_locator = (By.XPATH, '//*[@id="app"]/main/div/header/div[2]/div/div[2]/div/button[4]/span[1]/span')
    input_keywords_locator = (By.XPATH, '//*[@id="keyworld-input"]')
    btn_click_keywords_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[3]/div/dl/dd/li[1]/div/svg/path')
    btn_Media_upload_locator = (By.XPATH, '//*[@id="app"]/main/div/header/div[2]/div/div[2]/div/button[5]/span[1]/span')
    upload_screenshots_locator = (By.XPATH, '//*[@id="files_input"]')
    icon_save_locator = (By.XPATH, '//*[@id="List1"]/div/div/footer/button/span[1]')
    icon_card_image_locator = (By.XPATH, '//*[@id="List1"]/div/div/footer/button/span[1]')
    upload_Keyimages_locator = (By.XPATH, '//*[@id="key_image_input"]')
    btn_accepted_locator = (By.XPATH, '/html/body/div[3]/div[3]/div/footer/div[1]/div/button/span[1]')
    btn_submit_locator = (By.XPATH, '//*[@id="app"]/main/div/header/div[1]/div[1]/div[2]/div[4]/button/span[1]')
    checkbox_terms_locator = (By.XPATH, '/html/body/div[3]/div[3]/div/section/div/div[2]/label/span[2]')
    checkbox_autopublish_locator = (By.XPATH, '/html/body/div[3]/div[3]/div/section/div/div[1]/label/span[2]')
    label_submitted_locator = (By.XPATH, '/html/body/div[3]/div[3]/div/header/h2/span')
    icon_cookies_locator = (By.XPATH, '/html/body/div[3]/div[3]/div/header/h2/span')
    label_error_msg_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[2]/div[1]/div/dl/dd[2]/p/div')
    btn_releaseNote_locator = (
    By.XPATH, '/html/body/div[1]/main/div/header/div[2]/div/div[2]/div/button[2]/span[1]/span')
    input_Changelog_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[3]/div/div/div/div[2]/div/div/div')
    label_error_Changelog_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[3]/div/div[2]')
    btn_Localization_locator = (
    By.XPATH, '/html/body/div[1]/main/div/header/div[2]/div/div[2]/div/button[6]/span[1]/span')
    icon_add_chinese_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/div[1]/div/button/span[1]')
    btn_edit_translation_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/dl/dt/div[2]/div[1]/a')
    input_chinese_Changelog_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[1]/div[2]/dl[2]/dd/div[1]/div/div[2]/div/div/div')
    label_error_chinese_Changelog_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[1]/div[2]/dl[2]/dd/div[2]')
    input_chinese_Description_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[1]/div[2]/dl[4]/dd/div[1]/div/div[2]/div/div/div')
    label_error_chinese_Technical_Details_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[1]/div[2]/dl[5]/dd/div[2]')
    input_chinese_Technical_Details_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[1]/div[2]/dl[5]/dd/div[1]/div/div[2]/div/div/div')
    label_error_chinese_Description_locator = (
    By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[1]/div[2]/dl[4]/dd/div[2]')
    btn_package_save_locator = (
    By.XPATH, '//*[@id="app"]/main/div/div/div/div[1]/div[3]/div[3]/div[1]/div[2]/div[2]/button/span[1]')
    label_error_summary_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/div/div/p')
    label_error_Technical_Details_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[4]/div[1]/div[2]')
    label_error_Description_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[3]/div/div[2]')

    input_price_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/input')
    btn_add_discount_locator = (
    By.XPATH, "/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/button/span[1]")
    btn_percent_locator = (By.ID, "launch-discount-discount")
    div_percent30_locator = (By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]")
    div_percent10_locator = (By.XPATH, "/html/body/div[3]/div[3]/ul/li[3]")
    btn_week_locator = (By.ID, "launch-discount-duration")
    div_week1_locator = (By.XPATH, "/html/body/div[3]/div[3]/ul/li[1]")
    div_week2_locator = (By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]")
    label_launch_tips_locator = (By.XPATH, '//*[@id="app"]/main/div/div/div/div[1]/div[2]/div/div[2]/div[2]/p')
    price_error_msg_locator = (By.CLASS_NAME, 'error')
    btn_remove_discount_locator = (
    By.XPATH, "/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/button/span[1]")
    package_name_locator = (By.XPATH, '/html/body/div[1]/main/div/header/div[1]/div[1]/div[1]/div/div/div/input')
    icon_free_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/div[1]/div/label[2]/span[2]')
    icon_close_locator = (By.XPATH, '/html/body/div[3]/div[3]/div/header/button/span[1]')
    label_submit_error_locator = (By.CLASS_NAME, 'errors')
    btn_editor_upload_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[3]/div[3]/div/div[1]/a/span[1]')
    icon_dependence_2rd_locator = (By.XPATH,'/html/body/div[1]/main/div/div/div/div[1]/div[3]/div[3]/div[2]/div/div/div/div/div/label[2]/span[1]/span/input')
    label_package_error_locator = (By.XPATH, '//*[@id="app"]/main/div/div/div/div[1]/div[3]/div[3]/div/div/div/div/div/div[1]/p')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.publisher_title = self.publisher_title_locator
        self.delete_draft_ok_btn = None
        self.model3D_characters = None
        self.detail_edit_ok_btn = None
        self.metadata_edit = None
        self.keyImages_edit = None
        self.pacman_package_remove = None
        self.pacman_package_srp = None
        self.btn_srp2018 = None
        self.submit_btn = None
        self.protocol_checkbox = None
        self.btn_unity_remove = None
        self.btn_remove_OK = None
        self.submit_ok_btn = None
        self.btn_refresh_package = None
        self.pacman_package_dependence = None
        self.pacman_additional_dependence = None
        self.icon_add_dependence = None
        self.input_package_dependence = None
        self.title_dependence = None
        self.btn_save = None

        self.btn_description = None
        self.input_summary = None
        self.input_Technical_Details = None
        self.input_Description = None
        self.btn_details = None
        self.input_keywords = None
        self.btn_click_keywords = None
        self.btn_Media_upload = None
        self.upload_screenshots = None
        self.icon_save = None
        self.icon_card_image = None
        self.btn_accepted = None
        self.upload_Keyimages = None
        self.btn_submit = None
        self.checkbox_terms = None
        self.checkbox_autopublish = None
        self.label_submitted = None
        self.icon_cookies = None
        self.label_error_msg = None
        self.btn_releaseNote = None
        self.input_Changelog = None
        self.label_error_Changelog = None
        self.btn_Localization = None
        self.icon_add_chinese = None
        self.btn_edit_translation = None
        self.input_chinese_Changelog = None
        self.label_error_chinese_Changelog = None
        self.label_error_summary = None
        self.label_error_chinese_summary = None
        self.label_error_Technical_Details = None
        self.label_error_Description = None
        self.input_chinese_Technical_Details = None

        self.label_error_chinese_Technical_Details = None
        self.input_chinese_Description = None
        self.label_error_chinese_Description = None
        self.btn_package_save = None

        self.input_price = None
        self.btn_add_discount = None
        self.btn_percent = None
        self.div_percent30 = None
        self.btn_week = None
        self.div_week1 = None
        self.btn_remove_discount = None
        self.label_error_chinese_Description = None
        self.div_percent10 = None
        self.div_week2 = None
        self.label_launch_tips = None
        self.price_error_msg = None
        self.package_name = None
        self.icon_free = None
        self.icon_close = None
        self.label_submit_error = None
        self.btn_editor_upload = None
        self.icon_dependence_2rd = None
        self.label_package_error = None

        self.present_locator = self.delete_draft_locator

    def init_elements(self):
        super().init_elements()
        self.delete_draft = super().get_element(self.delete_draft_locator)
        self.delete_draft_ok_btn = super().get_element(self.delete_draft_ok_btn_locator)
        self.model3D_characters = super().get_element(self.model3D_characters_locator)
        self.detail_edit_ok_btn = super().get_element(self.detail_edit_ok_btn_locator)
        self.metadata_edit = super().get_element(self.metadata_edit_locator)
        self.keyImages_edit = super().get_element(self.keyImages_edit_locator)
        self.pacman_package_remove = super().get_element(self.pacman_package_remove_locator)
        self.pacman_package_srp = super().get_element(self.pacman_package_srp_locator)
        self.btn_srp2018 = super().get_element(self.btn_srp2018_locator)
        self.submit_btn = super().get_element(self.submit_btn_locator)
        self.submit_ok_btn = super().get_element(self.submit_ok_btn_locator)
        self.protocol_checkbox = super().get_element(self.protocol_checkbox_locator)
        self.btn_unity_remove = super().get_element(self.btn_unity_remove_locator)
        self.btn_remove_OK = super().get_element(self.btn_remove_OK_locator)
        self.btn_refresh_package = super().get_element(self.btn_refresh_package_locator)
        self.pacman_package_dependence = super().get_element(self.pacman_package_dependence_locator)
        self.pacman_additional_dependence = super().get_element(self.pacman_additional_dependence_locator)
        self.icon_add_dependence = super().get_element(self.icon_add_dependence_locator)
        self.input_package_dependence = super().get_element(self.input_package_dependence_locator)
        self.title_dependence = super().get_element(self.title_dependence_locator)
        self.btn_save = super().get_element(self.btn_save_locator)
        self.label_error_summary = super().get_element(self.label_error_summary_locator)
        self.label_error_Technical_Details = super().get_element(self.label_error_Technical_Details_locator)
        self.label_error_Description = super().get_element(self.label_error_Description_locator)

        self.btn_description = super().get_element(self.btn_description_locator)
        self.input_summary = super().get_element(self.input_summary_locator)
        self.input_Technical_Details = super().get_element(self.input_Technical_Details_locator)
        self.input_Description = super().get_element(self.input_Description_locator)
        self.btn_details = super().get_element(self.btn_details_locator)
        self.input_keywords = super().get_element(self.input_keywords_locator)
        self.btn_click_keywords = super().get_element(self.btn_click_keywords_locator)
        self.btn_Media_upload = super().get_element(self.btn_Media_upload_locator)
        self.upload_screenshots = super().get_element(self.upload_screenshots_locator)
        self.icon_save = super().get_element(self.icon_save_locator)
        self.icon_card_image = super().get_element(self.icon_card_image_locator)
        self.upload_Keyimages = super().get_element(self.upload_Keyimages_locator)
        self.btn_accepted = super().get_element(self.btn_accepted_locator)
        self.btn_submit = super().get_element(self.btn_submit_locator)
        self.checkbox_terms = super().get_element(self.checkbox_terms_locator)
        self.checkbox_autopublish = super().get_element(self.checkbox_autopublish_locator)
        self.label_submitted = super().get_element(self.label_submitted_locator)
        self.icon_cookies = super().get_element(self.icon_cookies_locator)
        self.label_error_msg = super().get_element(self.label_error_msg_locator)
        self.btn_releaseNote = super().get_element(self.btn_releaseNote_locator)
        self.input_Changelog = super().get_element(self.input_Changelog_locator)
        self.label_error_Changelog = super().get_element(self.label_error_Changelog_locator)
        self.btn_Localization = super().get_element(self.btn_Localization_locator)
        self.icon_add_chinese = super().get_element(self.icon_add_chinese_locator)
        self.btn_edit_translation = super().get_element(self.btn_edit_translation_locator)
        self.input_chinese_Changelog = super().get_element(self.input_chinese_Changelog_locator)
        self.label_error_chinese_Changelog = super().get_element(self.label_error_chinese_Changelog_locator)
        self.input_chinese_Technical_Details = super().get_element(self.input_chinese_Technical_Details_locator)

        self.label_error_chinese_Technical_Details = super().get_element(
        self.label_error_chinese_Technical_Details_locator)
        self.input_chinese_Description = super().get_element(self.input_chinese_Description_locator)
        self.label_error_chinese_Description = super().get_element(self.label_error_chinese_Description_locator)
        self.btn_package_save = super().get_element(self.btn_package_save_locator)

        self.input_price = super().get_element(self.input_price_locator)
        self.btn_add_discount = super().get_element(self.btn_add_discount_locator)
        self.btn_percent = super().get_element(self.btn_percent_locator)
        self.div_percent30 = super().get_element(self.div_percent30_locator)
        self.btn_week = super().get_element(self.btn_week_locator)
        self.div_week1 = super().get_element(self.div_week1_locator)
        self.btn_remove_discount = super().get_element(self.btn_remove_discount_locator)
        self.div_percent10 = super().get_element(self.div_percent10_locator)
        self.div_week2 = super().get_element(self.div_week2_locator)
        self.label_launch_tips = super().get_element(self.label_launch_tips_locator)
        self.price_error_msg = super().get_element(self.price_error_msg_locator)
        self.package_name = super().get_element(self.package_name_locator)
        self.icon_free = super().get_element(self.icon_free_locator)
        self.icon_close = super().get_element(self.icon_close_locator)
        self.label_submit_error = super().get_element(self.label_submit_error_locator)
        self.btn_editor_upload = super().get_element(self.btn_editor_upload_locator)
        self.icon_dependence_2rd = super().get_element(self.icon_dependence_2rd_locator)
        self.label_package_error = super().get_element(self.label_package_error_locator)