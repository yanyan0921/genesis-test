from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import logging


class BasePage:

    def __int__(self, driver, wait):
        self.logger = logging.getLogger("main.base.page")
        self.driver = driver
        self.present_locator = None

        if wait:
            self.wait_time = float(wait)
        else:
            self.wait_time = 10

    def init_page(self):
        try:
            self.logger.info("start initialize page")
            if self.wait_for_page_present(self.present_locator):
                self.logger.info("element: " + str(self.present_locator) + " is found")
                self.logger.info("page is present.")
                self.init_elements()
            else:
                self.logger.error("failed to find element: " + self.present_locator)
                self.logger.error("page is not present.")
        except selenium.common.exceptions.TimeoutException as e:
            self.logger.error(e)

    def wait_for_page_present(self, locator):
        return self.wait_for_element_present(locator)

    def wait_for_element_present(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable(locator))

    def wait_for_element_hidden(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.invisibility_of_element_located(locator))

    def navigate(self, url):
        # 导航到对应的url
        self.logger.info("navigate to: " + url)
        self.driver.get(url)

    def get_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element
        except selenium.common.exceptions.NoSuchElementException:
            self.logger.warning("Unable to locate element" + str(locator))

    def init_elements(self):
        self.logger.info("start get elements on page ...")
