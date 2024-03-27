import requests
import os
from dotenv import load_dotenv

load_dotenv()

class APIWrapper:

    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")
        self.api_key = os.getenv("APIKEY")

    def api_request(self, endpoint):
        self.url = f"{self.base_url}/{endpoint}"
        self.headers = {"Authorization": self.api_key}

    def get_data(self, endpoint):
        self.api_request(endpoint)
        response = requests.get(self.url, headers=self.headers)
        return response.json()

    def post_data(self, endpoint, data):
        self.api_request(endpoint)
        response = requests.post(self.url, headers=self.headers, json=data)
        return response.json()

    def delete_data(self, endpoint):
        self.api_request(endpoint)
        response = requests.delete(self.url, headers=self.headers)
        return response.json() if response.ok else None

    def put_data(self, endpoint, data):
        self.api_request(endpoint)
        response = requests.put(self.url, headers=self.headers, json=data)
        return response.json() if response.ok else None

