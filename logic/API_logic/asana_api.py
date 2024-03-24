from infra.api_wrapper import APIWrapper
from Utils import users
import requests
import asana
from asana.rest import ApiException


class AsanaApiRequests:

    url = 'https://app.asana.com/api/1.0/projects'

    def __init__(self, api_object):
        self.token = users.token
        self.ApiKey = users.apiKey
        self.my_api = api_object
        self.my_api = APIWrapper()
        self.headers = {
            "Accept": "application/json",
            "Authorization": self.ApiKey}
        configuration = asana.Configuration()
        configuration.access_token = self.token
        self.api_client = asana.ApiClient(configuration)


    def get_a_project_asana_website(self):
       # client = asana.Client.access_token(self.APIKEY)
       # result = client.projects.get_projects({'param': 'value', 'param': 'value'}, opt_pretty=True)
        result = requests.get(self.url, headers=self.headers)
        response_body_json = result.json()
        project_name = response_body_json["data"][0]["name"]
        print(project_name)
        return result

    def get_asana_task_name_by_api(self):
        project_gid = '1206876108607935'
        tasks = self.api_client.tasks.find_by_project(project_gid)
        print(tasks['name'])



