from .conn import Conn

from cloudevents.http import CloudEvent, to_structured

class Client:
    def __init__(self, base_url):
        self.conn = Conn(base_url)

    def create_event(self, user_id, attributes, data):
        # Create a CloudEvent
        attributes['source'] = f'/users/{user_id}'
        event = CloudEvent(attributes, data)
        # Convert to structured CloudEvent in HTTP format
        headers, body = to_structured(event)

        url = self.conn.build_url(f'/users/{user_id}/events')
        response = self.conn.session.post(url, headers=headers, data=body)
        return response.json()
