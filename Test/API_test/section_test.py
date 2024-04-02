import unittest

from Infra.api_wrapper import APIWrapper
from Logic.API_logic.asana_api import AsanaApiRequests
from Logic.API_logic.section_api import AsanaSection
from jirafile import JiraReport


class SectionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.section = AsanaSection()
        self.api_logic = AsanaApiRequests()

    def tearDown(self):
        if not self._outcome.success:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in test_change_task_to_another_section"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))

    def test_change_task_to_another_section(self):
        for i in range(3):
            self.gid = self.api_logic.create_new_task()
            self.section.change_task_to_another_section(self.gid)
        is_create = self.api_logic.is_display_create_task(self.gid)
        self.assertTrue(is_create, "The section not exited")
