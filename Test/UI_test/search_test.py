import time
import unittest

from Infra.browser_wrapper import BrowserWrapper
from Logic.UI_logic.search_page import SearchPage
from Utils.read_from_env import Credentials
from Utils.asana_login import AsanaLogin
from jirafile import JiraReport


class Asana_Search_Test(unittest.TestCase):
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
                issue_description = "Test failed due to assertion failure in test_search"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))

    def test_search(self):
        self.asana_search = SearchPage(self.driver)
        self.asana_search.search_flow("hello")
        self.assertIn("hello", self.asana_search.get_page_title(), "the title not show")