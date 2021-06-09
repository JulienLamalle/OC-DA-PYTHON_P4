class Tournament:
    def __init__(
        self, name: str, location: str, start_date: str, end_date: str,  description: str, time_control: str, number_of_turn=4
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = time_control
        self.number_of_turn = number_of_turn
        
    @property
    def serialize_tournament(self):
        tournament = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date":self.end_date,
            "description": self.description,
            "time_control": self.time_control,
            "number_of_turn": self.number_of_turn
        }
        return tournament
        