from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Infra.base_page import BasePage

from Utils.read_from_env import Credentials

class LogInPage(BasePage):

    EMAIL_INPUT = '//input[@type="email"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.credentials = Credentials()
        self.email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)

    def fill_email_input(self):
        email = self.credentials.get_email()
        self.email_input.send_keys(email)

    def press_enter_on_email_input(self):
        self.email_input.send_keys(Keys.RETURN)

    def email_flow(self):
        self.fill_email_input()
        self.press_enter_on_email_input()

