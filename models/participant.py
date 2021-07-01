from models.player import Player

class Participant(Player):
    def __init__(self, first_name: str, last_name: str, date_of_birth: str, sex: str, ranking):
        self.player_id = None
        self.score = 0
        self.ladder = 0
        self.opponents = []
        super().__init__(first_name, last_name, date_of_birth, sex, ranking)

    @property
    def serialize_player(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "sex": self.sex,
            "ranking": self.ranking,
            "id": self.player_id,
            "score": self.score,
            "ladder": self.ladder,
            "opponents": self.opponents,
        }

    @property
    def serialize_player_match(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "id": self.player_id,
        }
