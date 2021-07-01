class Match:
    def __init__(
        self, first_player, second_player, first_player_score, second_player_score
    ):
        self.first_player = first_player
        self.second_player = second_player
        self.first_player_score = first_player_score
        self.second_player_score = second_player_score
        self.matchs = ([first_player, first_player_score], [second_player, second_player_score])

    @property
    def serialize_match(self):
        return {"match": self.matchs}