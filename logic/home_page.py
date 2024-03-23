from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class HomePage(BasePage):

    CREATE_BUTTON = '//span[text()="Create"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.create_button = self._driver.find_element(By.XPATH, self.CREATE_BUTTON)

    def click_on_create_button(self):
        self.create_button.click()

