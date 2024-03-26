from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Infra.base_page import BasePage


class HomePage(BasePage):

   # CREATE_BUTTON = '//span[text()="Create"]'
    PROFILE = "//div[contains(@aria-label, 'User settings')]"
    WORKSPACE = "//div[text()='ge']"

    def __init__(self, driver):
        super().__init__(driver)
        self.profile = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.PROFILE)))

    def click_on_profile_icon(self):
        self.profile.click()
        self.workspace = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.WORKSPACE)))

    def click_on_change_workspace_button(self):
        self.workspace.click()


