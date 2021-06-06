class Round:
    def __init__(self, name, participants):
        self.name = name
        self.participants = participants

    def serialize_round(self):
        round = {"name": self.name, "participants": self.participants}
        return round
