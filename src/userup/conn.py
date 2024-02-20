import requests
from urllib.parse import urljoin

class Conn:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def build_url(self, endpoint):
        return urljoin(self.base_url, endpoint)
