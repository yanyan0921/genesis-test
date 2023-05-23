from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    btn_create_pull_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/a")
    btn_issue_page_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/a[2]")
    btn_milestones_page_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/a[2]")
    btn_labels_page_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div/a[1]")

    btn_pull_info_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/li/div[2]/div[1]/a")
    btn_labels_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[2]/div/div[1]/span/svg")
    btn_single_label_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[2]/div/div[1]/div/a[1]")
    btn_milestone_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[2]/div/div[4]/span/svg")
    btn_single_milestone_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[2]/div/div[4]/div/a")
    btn_assignees_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[2]/div/div[7]/span/svg")
    btn_single_assignees_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[2]/div/div[7]/div/a")
    btn_notifi_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/div[1]/div[2]/div/div[15]/div/form/button")
    # input_calender_locator = (By.XPATH, "//*[@id=\"update-issue-deadline-form\"]/input[1]")
    # btn_date_confirm_locator = (By.XPATH, "//*[@id=\"update-issue-deadline-form\"]/button")
    btn_create_pull_request_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[1]/div/div/div/div[5]/button")
    btn_merge_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]/div[1]/div[1]/ui/div[2]/div/div/div[8]/div/button")
    btn_merge_confirm_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]/div[1]/div[1]/ui/div[2]/div/div/div[4]/form/button[1]")
    btn_lock_conversation_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]/div[1]/div[2]/div/div[21]/button")
    btn_commit_page_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[5]/div[1]/div[1]/ui/div[3]/div/div/div/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        self.btn_create_pull_page = None
        self.btn_issue_page = None
        self.btn_milestones_page = None
        self.btn_labels_page = None
        self.btn_pull_info = None
        self.btn_labels = None
        self.btn_single_label = None
        self.btn_milestone = None
        self.btn_single_milestone = None
        self.btn_assignees = None
        self.btn_single_assignees = None
        self.btn_notifi = None
        self.btn_create_pull_request = None
        # self.input_calender = None
        # self.btn_date_confirm = None
        self.btn_merge = None
        self.btn_merge_confirm = None
        self.btn_commit_page = None
        self.btn_lock_conversation = None
        self.present_locator = self.btn_user_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.btn_create_pull_page = super().get_element(self.btn_create_pull_page_locator)
        self.btn_issue_page = super().get_element(self.btn_issue_page_locator)
        self.btn_milestones_page = super().get_element(self.btn_milestones_page_locator)
        self.btn_labels_page = super().get_element(self.btn_labels_page_locator)
        self.btn_pull_info = super().get_element(self.btn_pull_info_locator)
        self.btn_labels = super().get_element(self.btn_labels_locator)
        self.btn_single_label = super().get_element(self.btn_single_label_locator)
        self.btn_milestone = super().get_element(self.btn_milestone_locator)
        self.btn_single_milestone = super().get_element(self.btn_single_milestone_locator)
        self.btn_assignees = super().get_element(self.btn_assignees_locator)
        self.btn_single_assignees = super().get_element(self.btn_single_assignees_locator)
        self.btn_notifi = super().get_element(self.btn_notifi_locator)
        self.btn_create_pull_request = super().get_element(self.btn_create_pull_request_locator)
        # self.input_calender = super().get_element(self.input_calender_locator)
        # self.btn_date_confirm = super().get_element(self.btn_date_confirm_locator)
        self.btn_merge = super().get_element(self.btn_merge_locator)
        self.btn_merge_confirm = super().get_element(self.btn_merge_confirm_locator)
        self.btn_lock_conversation = super().get_element(self.btn_lock_conversation_locator)
        self.btn_commit_page = super().get_element(self.btn_commit_page_locator)
