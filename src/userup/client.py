from .conn import Conn

class Client:
    def __init__(self, base_url):
        self.conn = Conn(base_url)
