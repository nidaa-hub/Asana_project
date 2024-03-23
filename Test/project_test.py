import time
import unittest

from selenium.webdriver.common.by import By
from infra.browser_wrapper import BrowserWrapper
from logic.projects_page import ProjectsPage
from logic.login_page import LogInPage
from logic.password_page import PasswordPage


class Asana_Page_Test(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("https://app.asana.com/-/login")
        self.login_asana = LogInPage(self.driver)
        self.login_asana.email_flow("gethelpproject2021@gmail.com")
        time.sleep(3)
        self.password_asana = PasswordPage(self.driver)
        self.password_asana.password_flow_for_asana_website("gethelp24")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_check_create_button(self):
        time.sleep(10)
        self.asana_projects_page = ProjectsPage(self.driver)
        self.asana_projects_page.click_on_sidebar_button()
