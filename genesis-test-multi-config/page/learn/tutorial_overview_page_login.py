"""登录之后的tutorial overview页面"""
from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://learn-int.unity.com/tutorial/create-your-first-unity-project-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1"
    tutorial_content_locator = (
        By.XPATH, "//*[@id='pageBody']/div[2]/div[2]/div/div[1]/div[4]")
    select_version_locator = (
        By.XPATH, "//*[@id='pageBody']/div[2]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div/div/button")
    version_option_one_locator = (
        By.XPATH, "//*[@id='pageBody']/div[2]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div/div/div/div/div[1]")
    version_option_locator = (
        By.XPATH, "//*[@id='pageBody']/div[2]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div/div/div/div/div[3]")
    mark_btn_locator = (
        By.XPATH, "//*[@id='pageBody']/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/button")
    mark_btn_two_locator = (
        By.XPATH, "//div[@id='pageBody']/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div/button")
    mark_btn_three_locator = (
        By.XPATH, "//div[@id='pageBody']/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/div/button")
    mark_all_btn_locator = (
        By.XPATH, "//button/div[contains(text(),'Mark all')]/..")
    xp_earned_locator = (
        By.XPATH, "//*[@id='pageBody']/div[5]/div/div[2]/div/div/div[1]/div/div/div[2]")
    xp_continue_locator = (
        By.XPATH, "//*[@id='pageBody']/div[5]/div/div[2]/div/div/div[1]/div/div/div[4]/button")
    skip_evaluation_locator = (
        By.XPATH, "//*[@id='pageBody']/div[5]/div/div[2]/div/div/div[1]/div/div/div[3]/div[3]/a")
    end_continue_locator = (
        By.XPATH, "//*[@id='pageBody']/div[5]/div/div[2]/div/div/div[1]/div/div/div[3]/div/button")
    next_item_locator = (
        By.XPATH, "//*[@id='pageBody']/div[5]/div/div[2]/div/div/div[1]/div/div/div[3]/div/div[3]/div/div[2]/div")
    continue_to_content_summary_locator = (
        By.XPATH, "//*[@id='pageBody']/div[5]/div/div[2]/div/div/div[1]/div/div/div[3]/div/button")
    content_completed_continue_locator = (
        By.XPATH, "//*[@id='pageBody']/div[5]/div/div[2]/div/div/div[1]/div/div/div[5]/button")
    start_again_locator = (
        By.XPATH, "//*[@id='pageBody']/div[2]/div[2]/div/div[2]/div/div/div/div[4]/div[2]/div/div[2]/div/div/button")
    select_language_locator = (
        By.XPATH, "//*[@id='pageBody']/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div/div/button")
    language_btn_locator = (
        By.XPATH, "//*[@id='pageBody']/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.select_version = None
        self.version_option = None
        self.version_option_one = None
        self.mark_btn = None
        self.mark_btn_two = None
        self.mark_btn_three = None
        self.mark_all_btn = None
        self.xp_earned = None
        self.xp_continue = None
        self.skip_evaluation = None
        self.end_continue = None
        self.next_item = None
        self.continue_to_content_summary = None
        self.content_completed_continue = None
        self.start_again = None
        self.select_language = None
        self.language_btn = None
        self.present_locator = self.tutorial_content_locator

    def init_elements(self):
        super().init_elements()
        self.mark_btn = self.get_element(self.mark_btn_locator)
        self.mark_btn_two = super().get_element(self.mark_btn_two_locator)
        self.mark_btn_three = super().get_element(self.mark_btn_three_locator)
        self.mark_all_btn = super().get_element(self.mark_all_btn_locator)
        self.start_again = super().get_element(self.start_again_locator)
        self.select_language = super().get_element(self.select_language_locator)
        self.language_btn = super().get_element(self.language_btn_locator)
        self.select_version = super().get_element(self.select_version_locator)
        self.version_option = super().get_element(self.version_option_locator)
        self.version_option_one = super().get_element(self.version_option_one_locator)
        self.xp_earned = super().get_element(self.xp_earned_locator)
        self.xp_continue = super().get_element(self.xp_continue_locator)
        self.skip_evaluation = super().get_element(self.skip_evaluation_locator)
        self.end_continue = super().get_element(self.end_continue_locator)
        self.next_item = super().get_element(self.next_item_locator)
        self.continue_to_content_summary = super().get_element(self.continue_to_content_summary_locator)
        self.content_completed_continue = super().get_element(self.content_completed_continue_locator)