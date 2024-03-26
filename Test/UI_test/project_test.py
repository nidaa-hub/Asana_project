import time
import unittest

from Logic.UI_logic.home_page import HomePage
from read_from_env import Credentials
from Infra.browser_wrapper import BrowserWrapper
from Logic.UI_logic.projects_page import ProjectsPage
from Utils.asana_login import AsanaLogin


class Asana_Page_Test(unittest.TestCase):
    def setUp(self):
        self.data = Credentials()
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.login = AsanaLogin(self.driver)
        self.login.asana_login_with_email()
        time.sleep(5)
        self.asana_home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_check_open_project_button(self):
        self.asana_home_page.click_on_profile_icon()
        time.sleep(3)
        self.asana_home_page.click_on_change_workspace_button()
        time.sleep(5)
        self.asana_projects_page = ProjectsPage(self.driver)
        self.asana_projects_page.click_on_project_button()
       # time.sleep(5)
