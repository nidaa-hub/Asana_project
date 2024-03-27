from Infra.api_wrapper import APIWrapper
from Utils.read_from_env import Credentials
import requests
from Utils.api_requests import APIRequests
import json



class AsanaApiRequests:

    def __init__(self):
        self.api = APIRequests()
      #  self.my_api = APIWrapper()

    def get_project_names(self):
        result = self.api.get_data("projects")
        project_name = result["data"][0]["name"]
        print(project_name)


    def get_asana_task_name_by_api(self):
        result = self.api.get_data("tasks/1206935420617426")
        project_name = result["data"]["name"]
        print(project_name)






