import unittest

from Infra.api_wrapper import APIWrapper
from Logic.API_logic.asana_api import AsanaApiRequests


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.api_logic = AsanaApiRequests(self.my_api)

    def test_get_the_project_in_asana_website(self):
        result = self.api_logic.get_a_project_asana_website()
        task_name = self.api_logic.get_asana_task_name_by_api()
   #     assert result, f"Failed to open the link: {'https://apod.nasa.gov/apod/image/2403/2024_03_05_Pons-Brooks_Revuca_1200px.png'}"



