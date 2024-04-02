from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Infra.base_page import BasePage


class ResultPage(BasePage):

    TASKS = "//div[@id='tasks' and @tabindex='0']"

    def __init__(self, driver):
        super().__init__(driver)
        self.tasks_result = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.TASKS)))

    def search_result_page(self):
        return self.tasks_result.is_displayed()