import unittest

from Infra.api_wrapper import APIWrapper
from Logic.API_logic.asana_api import AsanaApiRequests


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.api_logic = AsanaApiRequests()

    def test_get_the_project_in_asana_website(self):
        self.api_logic.get_project_names()

    def test_get_specific_task_in_a_project(self):
        self.api_logic.get_asana_task_name_by_api()






