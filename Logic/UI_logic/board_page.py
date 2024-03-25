from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class BoardPage(BasePage):

    ADD_TASK = "//div[contains(@class,'PotBoardAddTaskDropdownButton')]//div[text()='Add task']"

    def __init__(self, driver):
        super().__init__(driver)
        self.add_task_button = self._driver.find_element(By.XPATH, self.ADD_TASK)

    def click_on_add_task(self):
        self.add_task_button.click()
