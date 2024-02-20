import requests

class Conn:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def build_url(self, endpoint):
        return f"{self.base_url}{endpoint}"
