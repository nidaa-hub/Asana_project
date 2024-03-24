import time
import unittest
from Utils import users
from Utils.read_from_env import Credentials
from infra.config_loader import ConfigLoader

from infra.browser_wrapper import BrowserWrapper
from logic.UI_logic.home_page import HomePage
from logic.UI_logic.login_page import LogInPage
from logic.UI_logic.password_page import PasswordPage
from logic.UI_logic.projects_page import ProjectsPage



class Asana_Page_Test(unittest.TestCase):
    def setUp(self):
        self.data = Credentials()
        config_loader = ConfigLoader()
        config = config_loader.load_config()
        url = config["url"]
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(url)
        self.login_asana = LogInPage(self.driver)
        self.login_asana.email_flow(self.data.get_email())
        time.sleep(2)
        self.password_asana = PasswordPage(self.driver)
        self.password_asana.password_flow_for_asana_website(self.data.get_password())
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_check_create_button(self):
        print("hello")
        self.asana_home_page = HomePage(self.driver)
        #self.asana_home_page.click_on_profile_setting()

      #  self.asana_project = ProjectsPage(self.driver)
      #  self.asana_home_page.click_on_create_button()
      #  time.sleep(5)
      #  self.asana_project.click_on_create_new_project_button()
      #  time.sleep(5)
     #   self.asana_home_page.click_on_profile_setting()
      #  time.sleep(5)


        












