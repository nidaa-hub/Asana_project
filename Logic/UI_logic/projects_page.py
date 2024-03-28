from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Infra.base_page import BasePage

class ProjectsPage(BasePage):

  #  BORAD_BUTTON = '//h2[text()="Projects"]'
    OPEN_TASK = '//div[@data-task-id="1206943310099462"]'
    PRIORITY = "//div[contains(@class,'LabeledRowStructure')]//div[text()='Medium']"
    LOW = ''

    def __init__(self, driver):
        super().__init__(driver)
      #  self.board_button = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.BORAD_BUTTON)))
        self.open_task = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.OPEN_TASK)))

    def click_on_board_button(self):
        self.open_project.click()

    def click_on_task(self):
        self.open_task.click()
        self.priority = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.PRIORITY)))

    def click_on_priority(self):
        self.priority.click()
        self.low = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.LOW)))

    def change_priority_to_low(self):
        self.low.click()

