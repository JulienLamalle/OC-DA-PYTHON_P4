class Tournament:
    def __init__(
        self, name: str, location: str, start_date: str, end_date: str,  description: str, time_control: str, number_of_turn=4, current_round= 1, tournament_id=0
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = time_control
        self.number_of_turn = number_of_turn
        self.current_round = current_round
        self.tournament_id = tournament_id
        self.players = []
        self.rounds = []
        
    @property
    def serialize_tournament(self):
        tournament = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date":self.end_date,
            "description": self.description,
            "time_control": self.time_control,
            "number_of_turn": self.number_of_turn,
            "current_round": self.current_round,
            "tournament_id": self.tournament_id,
            "players": self.serialize_tournament_players,
            "rounds": self.serialize_tournament_rounds
        }
        return tournament
    
    @property
    def serialize_tournament_players(self):
        serialized_players = []
        for player in self.players:
            serialized_players.append(player.serialize_player)
        return serialized_players
    
    @property
    def serialize_tournament_rounds(self):
        serialized_rounds = []
        for round in self.rounds:
            serialized_rounds.append(round.serialize_round)
        return serialized_rounds
    
    def sort_players_by_score(self):
        sorted_players = sorted(self.players, key=lambda player: (player.score, player.ranking), reverse=True)
        return sorted_players
    
    def sort_players_by_rank(self):
        sorted_players = sorted(self.players, key=lambda player: player.ranking, reverse=True)
        return sorted_players
    
    def generate_first_round_pairs(self):
        players = self.sort_players_by_rank()
        tournament_number_of_players = 8
        first_players_part = players[0: int(tournament_number_of_players / 2)]
        second_players_part = players[int(tournament_number_of_players / 2) :]
        players_pairs = []
        index = 0
        for index in range(int(tournament_number_of_players / 2)):
            players_pair = [first_players_part[index], second_players_part[index]]
            players_pairs.append(players_pair)
            first_players_part[index].opponents.append(second_players_part[index].player_id)
            second_players_part[index].opponents.append(first_players_part[index].player_id)
            index += 1
        return players_pairs
    
    def generate_pairs(self):
        players = self.sort_players_by_score()
        players_pairs = []
        while players:
            index = 1
            while (index <= len(players) and len(players) > 2 and players[index].player_id in players[0].opponents):
                index += 1
            players_pair = [players[0], players[index]]
            players[0].opponents.append(players[index].player_id)
            players[index].opponents.append(players[0].player_id)
            del players[index]
            del players[0]
            players_pairs.append(players_pair)
        return players_pairs