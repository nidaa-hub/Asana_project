from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class ProjectsPage(BasePage):

    CREATE_PROJECT = (By.XPATH, '//span[text()="Project"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.project_button = self._driver.find_element(By.XPATH, self.CREATE_PROJECT)

  #  def click_on_sidebar_button(self):
 #       self.sidebar_button.click()

    def click_on_create_new_project_button(self):
        self.project_button.click()
