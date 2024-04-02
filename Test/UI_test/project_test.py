import time
import unittest
from jirafile import JiraReport
from Logic.UI_logic.home_page import HomePage
from Utils.read_from_env import Credentials
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
        if not self._outcome.success:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in test_check_open_project_button"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))

    def test_check_open_project_button(self):
        self.asana_home_page.click_on_profile_icon()
        time.sleep(3)
        self.asana_home_page.click_on_change_workspace_button()
        time.sleep(5)
        self.asana_projects_page = ProjectsPage(self.driver)
        #self.asana_projects_page.click_on_project_button()
       # time.sleep(5)
