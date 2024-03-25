from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class HomePage(BasePage):

   # CREATE_BUTTON = '//span[text()="Create"]'
   # PROJECT = '//span[text()="CI/CD project"]'
    PROFILE = "//div[contains(@aria-label, 'User settings')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.profile = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.PROFILE)))
        #self.profile = self._driver.fined_element(By.XPATH,self.PROFILE)
    #    self.create_button = self._driver.find_element(By.XPATH, self.CREATE_BUTTON)
     #   self.project_button = self._driver.find_element(By.XPATH, self.PROJECT)
     #   self.new_project_button = self._driver.find_element(By.XPATH, self.CREATE_PROJECT)

    def click_on_profile_icon(self):
        self.profile.click()


