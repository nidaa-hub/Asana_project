from Infra.api_wrapper import APIWrapper
from Infra.api_gid import GetID
from Utils.read_from_env import Credentials


import random


class AsanaApiRequests:

    daily_tasks = ["Run", "Walk", "Sleep", "Eat", "Dance", "Pilates", "Read", "Work"]

    def __init__(self):
        self.api = APIWrapper()
        self.new_gid = GetID()
        self.data = Credentials()
        self.project_gid = self.data.get_project_gid()

    def get_project_names(self):
        result = self.api.get_data("projects")
        project_name = result["data"][0]["name"]
        return project_name

    def get_asana_task_name_by_api(self, gid):
        task_gid = "tasks/" + gid
        result = self.api.get_data(task_gid)
        task_name = result["data"]["name"]
        return task_name

    def create_new_task(self):
        random_task = random.choice(self.daily_tasks)
        data = {"data": {"projects": [self.project_gid], "name": random_task}}
        self.api.post_data("tasks", data)
        task_gid = self.new_gid.get_task_gid()
        return task_gid

    def is_display_create_task(self, task_gid):
        if task_gid:
            return True
        return False

    def delete_specific_task(self, gid):
        task_gid = "tasks/" + gid
        result = self.api.delete_data(task_gid)
        delete_task = result["data"]
        return delete_task
