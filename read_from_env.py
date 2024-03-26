# read_from_env_file_like_username_password.py
import os
from dotenv import load_dotenv

load_dotenv()


class Credentials:

    def get_email(self):
        email = os.getenv("EMAIL")
        if email is None:
            raise ValueError("EMAIL_TXT environment variable is not set")
        return email

    def get_password(self):
        password = os.getenv("PASSWORD")
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
