class EventType:
    def __init__(self, type_str):
        self.type_str = type_str

    def validate(data):
        # This is a placeholder for the actual validation logic
        # which can be implemented as needed for each event type.
        return data


class Click(EventType):
    name = "com.userup.event.click"

    def __init__(self):
        super().__init__(Click.name)
