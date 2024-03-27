# api_requests.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class APIRequests:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")
        self.api_key = os.getenv("APIKEY")

    def get_data(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": self.api_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def post_data(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": self.api_key}
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def delete_data(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": self.api_key}
        response = requests.delete(url, headers=headers)
        return response.json() if response.ok else None

