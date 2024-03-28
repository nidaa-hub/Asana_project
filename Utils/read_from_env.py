# read_from_env_file_like_username_password.py
import os
from dotenv import load_dotenv

load_dotenv()

class Credentials:

    def get_email(self):
        email = os.getenv("EMAIL")
      #  email = os.environ["EMAIL"]
        if email is None:
            raise ValueError("EMAIL_TXT environment variable is not set")
        return email

    def get_password(self):
        password = os.getenv("PASSWORD")
      #  password = os.environ["PASSWORD"]
        if password is None:
            raise ValueError("PASSWORD environment variable is not set")
        return password

    def get_token(self):
        token= os.getenv("TOKEN")
        if token is None:
            raise ValueError("token environment variable is not set")
        return token

    def get_apikey(self):
        apikey = os.getenv("APIKEY")
        if apikey is None:
            raise ValueError("apikey environment variable is not set")
        return apikey

    def get_jira_token(self):
        jira_token = os.getenv("JIRA_TOKEN")
        if jira_token is None:
            raise ValueError("JIRA_TOKEN environment variable is not set")
        return jira_token

    def get_jira_url(self):
        jira_url = os.getenv("JIRA_URL")
        if jira_url is None:
            raise ValueError("JIRA_URL environment variable is not set")
        return jira_url

    def get_jira_email(self):
        jira_email = os.getenv("JIRA_EMAIL")
        if jira_email is None:
            raise ValueError("Email environment variable is not set")
        return jira_email

    def get_jira_project_key(self):
        jira_project_key = os.getenv("JIRA_PROJECT_KEY")
        if jira_project_key is None:
            raise ValueError("jira project key environment variable is not set")
        return jira_project_key

    def get_project_gid(self):
        project_gid = os.getenv("PROJECT_GID")
        if project_gid is None:
            raise ValueError("asana project gid environment variable is not set")
        return project_gid