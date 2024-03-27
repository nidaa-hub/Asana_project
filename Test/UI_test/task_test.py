import time
import unittest

from Infra.browser_wrapper import BrowserWrapper
from jirafile import JiraReport
from Utils.read_from_env import Credentials
from Utils.asana_login import AsanaLogin
from Logic.UI_logic.projects_page import ProjectsPage

class Asana_Task_Test(unittest.TestCase):
    def setUp(self):
        self.data = Credentials()
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.login = AsanaLogin(self.driver)
        self.login.asana_login_with_email()
        time.sleep(20)


    def tearDown(self):
        self.driver.quit()
        '''     if hasattr(self, '_outcome') and self._outcome.errors:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in non_functional_test"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))'''

    def test_change_task_priority(self):
        self.asana_page = ProjectsPage()
        self.asana_page.click_on_project_button
      #  self.asana_page.click_on_task()
