from .conn import Conn
from .config import config

from cloudevents.http import CloudEvent, to_structured
from .types import Click  # Import additional event types as needed


class Client:
    def __init__(self, base_url):
        self.conn = Conn(base_url)

    def track(self, user_id, event_type, data):
        attributes = {
            "type": event_type.name(),
            "source": config.source,
            "specversion": "1.0",
            "datacontenttype": "application/json",
        }
        # Validate and format the data based on the event type
        if event_type == Click().type_str:
            data = Click().validate(data)

        # Use the create_event method to send the event
        return self.create_event(user_id, attributes, data)

    def create_event(self, user_id, attributes, data):
        # Create a CloudEvent
        event = CloudEvent(attributes, data)

        print(event)

        # Convert to structured CloudEvent in HTTP format
        headers, body = to_structured(event)

        url = self.conn.build_url(f"/users/{user_id}/events")
        response = self.conn.session.post(url, headers=headers, data=body)
        return response.json()
