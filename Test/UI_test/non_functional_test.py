import time
import unittest
from Utils import users
from Utils.read_from_env import Credentials
from infra.config_loader import ConfigLoader

from infra.browser_wrapper import BrowserWrapper
from logic.UI_logic.display_page import DisplayPage
from logic.UI_logic.home_page import HomePage
from logic.UI_logic.login_page import LogInPage
from logic.UI_logic.password_page import PasswordPage
from logic.UI_logic.projects_page import ProjectsPage
from logic.UI_logic.setting_page import SettingPage


class Asana_non_functional_Test(unittest.TestCase):
    def setUp(self):
        self.data = Credentials()
        config_loader = ConfigLoader()
        config = config_loader.load_config()
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(config["url"])
        self.login_asana = LogInPage(self.driver)
        self.login_asana.email_flow(self.data.get_email())
        time.sleep(2)
        self.password_asana = PasswordPage(self.driver)
        self.password_asana.password_flow_for_asana_website(self.data.get_password())
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_change_to__dark_mode(self):
        self.asana_home_page = HomePage(self.driver)
        self.asana_home_page.click_on_profile_icon()
        time.sleep(5)
        self.asana_setting_page = SettingPage(self.driver)
        self.asana_setting_page.click_on_setting_button()
        time.sleep(3)
        self.asana_display = DisplayPage(self.driver)
        self.asana_display.click_on_display_button()
        self.asana_display.click_on_theme_button()
        self.asana_display.click_on_dark_mode()




        












