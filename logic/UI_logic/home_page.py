from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class HomePage(BasePage):

   # CREATE_BUTTON = '//span[text()="Create"]'
  #  PROJECT = "//a[contains(@aria-label,'CI/CD project, Project')]"
    PROFILE = "//div[contains(@class,'TopbarSettingsMenuButton-avatar')]"
    #SETTING = (By.XPATH, '//*[@id="lui_2286"]')

    def __init__(self, driver):
        super().__init__(driver)
    #    self.create_button = self._driver.find_element(By.XPATH, self.CREATE_BUTTON)
     #   self.project_button = self._driver.find_element(By.XPATH, self.PROJECT)
        self.profile = self._driver.find_element(By.XPATH, self.PROFILE)
     #   self.new_project_button = self._driver.find_element(By.XPATH, self.CREATE_PROJECT)

 #   def click_on_create_button(self):
  #      self.create_button.click()

    def click_on_project(self):
        self.project_button.click()

    def click_on_profile_setting(self):
        self.profile.click()


