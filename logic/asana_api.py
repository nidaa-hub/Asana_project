import webbrowser

from infra.api_wrapper import APIWrapper
import asana
import json
import requests


class AsanaApiRequests:

    APIKEY = 'Bearer 2/1206875539694934/1206876120648733:cc820a375a52d040190ba8d7eb8cb45e'
    url = 'https://app.asana.com/api/1.0/projects'
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer 2/1206875539694934/1206876120648733:cc820a375a52d040190ba8d7eb8cb45e"}

    def __init__(self, api_object):
        self.my_api = api_object
        self.my_api = APIWrapper()

    def get_a_project_asana_website(self):
       # client = asana.Client.access_token(self.APIKEY)
       # result = client.projects.get_projects({'param': 'value', 'param': 'value'}, opt_pretty=True)
        result = requests.get(self.url, headers=self.headers)
        response_body_json = result.json()
        project_name = response_body_json["data"][0]["name"]
        print(project_name)
        return result

  #  def get_image_of_the_day_url(self):
  #      image = self.planetary_apod_api()
  #      image_url = image["url"]
  #      webbrowser.open(image_url)
  #     return image_url


