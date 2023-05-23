from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    btn_create_issue_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/a")
    btn_issue_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/a[2]")
    btn_issue_info_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]/li[1]/div[2]/div[1]/a")
    input_comment_locator = (By.XPATH, "//*[@id=\"comment-form\"]/div[2]/div[1]/div/div[2]/div[6]")
    btn_submit_locator = (By.XPATH, "//*[@id=\"comment-form\"]/div[4]/div/button")
    btn_milestones_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div/a[2]")
    btn_issue_close_locator = (By.ID, "status-button")
    btn_labels_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div/a[1]")
    btn_labels_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/div/div[3]")
    btn_single_label_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/a[1]")
    btn_milestone_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/div/div[6]")
    btn_single_milestone_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/div/div[6]/div/a")
    btn_assignees_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/div/div[9]")
    btn_single_assignees_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/div/div[9]/div/a[1]")
    btn_notifi_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/div/div[14]/div/form/button")
    input_calender_locator = (By.XPATH, "//*[@id=\"update-issue-deadline-form\"]/input[1]")
    btn_date_confirm_locator = (By.XPATH, "//*[@id=\"update-issue-deadline-form\"]/button")
    info_issue_create_verify_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[1]/div")
    info_issue_comment_verify_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/div")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        self.btn_issue_page = None
        self.btn_create_issue_page = None
        self.btn_issue_info = None
        self.btn_submit = None
        self.input_comment = None
        self.btn_milestones_page = None
        self.btn_issue_close = None
        self.btn_labels_page = None
        self.btn_labels = None
        self.btn_single_label = None
        self.btn_milestone = None
        self.btn_single_milestone = None
        self.btn_assignees = None
        self.btn_single_assignees = None
        self.btn_notifi = None
        self.input_calender = None
        self.btn_date_confirm = None
        self.info_issue_create_verify = None
        self.info_issue_comment_verify = None
        self.present_locator = self.btn_user_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.btn_create_issue_page = super().get_element(self.btn_create_issue_page_locator)
        self.btn_issue_page = super().get_element(self.btn_issue_page_locator)
        self.btn_issue_info = super().get_element(self.btn_issue_info_locator)
        self.btn_submit = super().get_element(self.btn_submit_locator)
        self.input_comment = super().get_element(self.input_comment_locator)
        self.btn_milestones_page = super().get_element(self.btn_milestones_page_locator)
        self.btn_issue_close = super().get_element(self.btn_issue_close_locator)
        self.btn_labels_page = super().get_element(self.btn_labels_page_locator)
        self.btn_labels = super().get_element(self.btn_labels_locator)
        self.btn_single_label = super().get_element(self.btn_single_label_locator)
        self.btn_milestone = super().get_element(self.btn_milestone_locator)
        self.btn_single_milestone = super().get_element(self.btn_single_milestone_locator)
        self.btn_assignees = super().get_element(self.btn_assignees_locator)
        self.btn_single_assignees = super().get_element(self.btn_single_assignees_locator)
        self.btn_notifi = super().get_element(self.btn_notifi_locator)
        self.input_calender = super().get_element(self.input_calender_locator)
        self.btn_date_confirm = super().get_element(self.btn_date_confirm_locator)
        self.info_issue_create_verify = super().get_element(self.info_issue_create_verify_locator)
        self.info_issue_comment_verify = super().get_element(self.info_issue_comment_verify_locator)
