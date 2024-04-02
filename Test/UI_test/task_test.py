import time
import unittest

from Infra.browser_wrapper import BrowserWrapper
from Logic.UI_logic.home_page import HomePage
from Utils.read_from_env import Credentials
from Utils.asana_login import AsanaLogin
from Logic.UI_logic.projects_page import ProjectsPage
from jirafile import JiraReport

class Asana_Task_Test(unittest.TestCase):
    def setUp(self):
        self.data = Credentials()
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver()
        self.login = AsanaLogin(self.driver)
        self.login.asana_login_with_email()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()
        if not self._outcome.success:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in test_change_task_priority_Medium"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))

    def test_change_task_priority_Medium(self):
        self.asana_home_page = HomePage(self.driver)
        self.asana_home_page.click_on_project_button()
        self.asana_project = ProjectsPage(self.driver)
        self.asana_project.click_on_task()
        self.asana_project.click_on_priority()
        self.medium_priority = self.asana_project.is_display_priority_medium_button()
        self.assertTrue(self.medium_priority, "Priority is not Medium")
