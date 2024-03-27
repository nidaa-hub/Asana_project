from Infra.api_wrapper import APIWrapper
from Infra.api_gid import GetID


class AsanaSection:

    def __init__(self):
        self.api = APIWrapper()
        self.new_gid = GetID()

    def change_task_to_another_section(self, task_gid):
        data = {"data": {"task": task_gid}}
        result = self.api.post_data("sections/1206935539102606/addTask", data)

