from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class ProjectsPage(BasePage):

    SIDEBAR_BUTTON = '//div[@aria-label="Expand sidebar"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.sidebar_button = self._driver.find_element(By.XPATH, self.SIADEBAR_BUTTON)

    def click_on_sidebar_button(self):
        self.sidebar_button.click()
