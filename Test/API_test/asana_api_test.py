import unittest
from Infra.api_wrapper import APIWrapper
from Logic.API_logic.asana_api import AsanaApiRequests
from Infra.api_gid import GetID
from jirafile import JiraReport


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.api_logic = AsanaApiRequests()
        self.gid = GetID()

    def tearDown(self):
        if not self._outcome.success:
            try:
                # Assertion passed, report bug to Jira
                jira_report = JiraReport()
                issue_summary = "Test Assertion Failure"
                issue_description = "Test failed due to assertion failure in test_the_delete_task"
                jira_report.create_issue(issue_summary, issue_description)
                print("Issue Created")
            except Exception as e:
                print("Failed to report bug to Jira:", str(e))

    def test_get_the_project_in_asana_website(self):
        project_name = self.api_logic.get_project_names()
        self.assertEqual(project_name, "test project")

    def test_get_specific_task_in_a_project(self):
        task_name = self.api_logic.get_asana_task_name_by_api("1206944426202212")
        self.assertEqual(task_name, "Walk")

    def test_the_delete_task(self):
        delete_task = self.api_logic.delete_specific_task("1206987643403686")
        self.assertIsNone(delete_task, "The task is not deleted")
