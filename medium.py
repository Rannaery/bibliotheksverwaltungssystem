class Medium:
    def __init__(self, titel):
        self.titel = titel

    def to_dict(self):
        return {"titel": self.titel}