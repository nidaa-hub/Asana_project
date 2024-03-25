import time
import unittest

from Infra.browser_wrapper import BrowserWrapper
from Logic.UI_logic.projects_page import ProjectsPage
from Logic.UI_logic.login_page import LogInPage
from Logic.UI_logic.password_page import PasswordPage


class Asana_Page_Test(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("https://app.asana.com/-/login")


    def tearDown(self):
        self.driver.quit()

    def test_check_create_button(self):
        time.sleep(10)
        self.asana_projects_page = ProjectsPage(self.driver)
     #   self.asana_projects_page.click_on_sidebar_button()
