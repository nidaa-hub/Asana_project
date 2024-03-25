import time
from Utils.read_from_env import Credentials
from Infra.browser_wrapper import BrowserWrapper
from Logic.UI_logic.login_page import LogInPage
from Logic.UI_logic.password_page import PasswordPage


class AsanaLogin:
    def __init__(self, driver):
        self.driver = driver

    def asana_login_with_email(self):
        self.login_asana = LogInPage(self.driver)
        self.login_asana.email_flow()
        time.sleep(2)
        self.password_asana = PasswordPage(self.driver)
        self.password_asana.password_flow_for_asana_website()
