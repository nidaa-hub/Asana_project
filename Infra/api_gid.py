from Infra.api_wrapper import APIWrapper


class GetID:

    def __init__(self):
        self.api = APIWrapper()

    def get_task_gid(self):
        result = self.api.get_data("projects")
        task_gid = result["data"][0]["gid"]
        return task_gid


