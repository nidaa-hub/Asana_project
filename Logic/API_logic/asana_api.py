from Infra.api_wrapper import APIWrapper
from Logic.API_logic.api_gid import GetID

import random

class AsanaApiRequests:

    daily_tasks = ["Run", "Walk", "Sleep", "Eat", "Dance", "Pilates", "Read", "Work"]

    def __init__(self):
        self.api = APIWrapper()
        self.new_gid = GetID()

    def get_project_names(self):
        result = self.api.get_data("projects")
        project_name = result["data"][0]["name"]
        return project_name

    def get_asana_task_name_by_api(self):
        result = self.api.get_data("tasks/1206935420617426")
        task_name = result["data"]["name"]
        return task_name

    def create_new_task(self):
        random_task = random.choice(self.daily_tasks)
        data = {"data": {"projects": ["1206935539102605"], "name": random_task}}
        self.api.post_data("tasks", data)
        task_gid = self.new_gid.get_task_gid()
        return task_gid

    def delete_specific_task(self):
        result = self.api.delete_data("tasks/1206935420617426")
        delete_task = result["data"]
        return delete_task

    def create_many_task(self):
        for i in range(3):
            self.create_new_task()





