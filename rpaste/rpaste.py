import requests


class rpaste:
    def __init__(self):
        pass

    def set_content(self, content):
        self.content = content

    def set_password(self, password):
        self.password = password

    def upload(self):
        print("Uploading paste ", self.content)
