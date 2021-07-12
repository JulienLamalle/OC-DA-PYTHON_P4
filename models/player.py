class Player:
    def __init__(
        self, first_name: str, last_name: str, date_of_birth: str, sex: str, ranking
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.ranking = ranking

    @property
    def serialize_player(self):
        player = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "sex": self.sex,
            "ranking": self.ranking,
        }
        return player

    @property
    def serialize_match_player(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "id": self.player_id,
        }
