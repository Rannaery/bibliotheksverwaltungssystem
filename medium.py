import uuid

class Medium:
    def __init__(self, titel, id=None, ausgeliehen_an=None):
        self.titel = titel
        self.id = id if id is not None else str(uuid.uuid4())
        self.ausgeliehen_an = ausgeliehen_an

    def to_dict(self):
        return {
            "id": self.id,
            "titel": self.titel,
            "ausgeliehen_an": self.ausgeliehen_an
        }