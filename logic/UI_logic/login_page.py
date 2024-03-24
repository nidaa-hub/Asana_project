from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class LogInPage(BasePage):

    EMAIL_INPUT = '//input[@type="email"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)

    def fill_email_input(self, text):
        self.email_input.send_keys(text)

    def press_enter_on_email_input(self):
        self.email_input.send_keys(Keys.RETURN)

    def email_flow(self, text):
        self.fill_email_input(text)
        self.press_enter_on_email_input()

