import os

class Config:
    def __init__(self):
        self._base_url = os.getenv('USERUP_BASE_URL', 'http://localhost:8000')
        self._source = os.getenv('USERUP_SOURCE', 'default-source')
        self._credentials = os.getenv('USERUP_CREDENTIALS', 'default-credentials')

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        self._credentials = value

# Config object singleton
config = Config()
