import unittest

from Infra.api_wrapper import APIWrapper
from Logic.API_logic.asana_api import AsanaApiRequests
from Logic.API_logic.section_api import AsanaSection


class SectionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.section = AsanaSection()
        self.api_logic = AsanaApiRequests()

    def test_change_task_to_another_section(self):
        for i in range(3):
            gid = self.api_logic.create_new_task()
            self.section.change_task_to_another_section(gid)

