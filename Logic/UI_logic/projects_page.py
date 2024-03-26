from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Infra.base_page import BasePage

class ProjectsPage(BasePage):

    OPEN_PROJECT = '//h2[text()="Projects"]'
    PROJECT = '//a[@aria-label="CI/CD project, Project"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.open_project = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.OPEN_PROJECT)))
        self.project = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.PROJECT)))

    def click_on_open_project_button(self):
        self.open_project.click()

    def click_on_project_button(self):
        self.project.click()
