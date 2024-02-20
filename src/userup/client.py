from .conn import Conn

class Client:
    def __init__(self, base_url):
        self.conn = Conn(base_url)

    def create_event(self, event_data):
        url = self.conn.build_url('/events')
        response = self.conn.session.post(url, json=event_data)
        return response.json()
