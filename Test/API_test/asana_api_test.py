import unittest
from Infra.api_wrapper import APIWrapper
from Logic.API_logic.asana_api import AsanaApiRequests
from Infra.api_gid import GetID


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.api_logic = AsanaApiRequests()
        self.gid = GetID()

    def test_get_the_project_in_asana_website(self):
        self.api_logic.get_project_names()

    def test_get_specific_task_in_a_project(self):
        self.api_logic.get_asana_task_name_by_api("1206944426202212")

    def test_the_delete_task(self):
        self.api_logic.delete_specific_task("1206935420617438")


