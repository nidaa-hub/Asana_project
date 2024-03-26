from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Infra.base_page import BasePage

from Utils.read_from_env import Credentials

class PasswordPage(BasePage):

    PASSWORD_INPUT = '//input[@type="password"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.credentials = Credentials()
        self.Password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)

    def fill_password_input_text_on_asana_website(self):
        password = self.credentials.get_password()
        self.Password_input.send_keys(password)

    def press_enter_on_password_input(self):
        self.Password_input.send_keys(Keys.RETURN)

    def password_flow_for_asana_website(self):
        self.fill_password_input_text_on_asana_website()
        self.press_enter_on_password_input()
