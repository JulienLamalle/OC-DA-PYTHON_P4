from tinydb import TinyDB, Query
from models.player import Player

DATABASE = TinyDB("db/db.json")
PLAYERS = DATABASE.table("PLAYERS")


class PlayersDatabaseController:
    def __init__(self):
        self.players = PLAYERS

    @property
    def sort_players_alphabetically(self):
        sorted_players = sorted(self.players, key=lambda player: player["last_name"])
        return sorted_players

    @property
    def sort_players_by_ranking(self):
        sorted_players = sorted(self.players, key=lambda player: player["ranking"])
        return sorted_players

    def save_player(self, player: object):
        self.players.insert(player.serialize_player)

    def search_in_players_table(self, first_name: str, last_name: str):
        for player in self.players:
            if player["first_name"] == first_name and player["last_name"] == last_name:
                return player
        return None

    def get_player_id(self, first_name: str, last_name: str):
        player = self.search_in_players_table(first_name, last_name)
        return player.doc_id if player else None

    def search_player_by_id(self, player_id):
        player = self.players.get(doc_id=int(player_id))
        if player:
            return player
        return None

    def update_player(self, player: Player, player_id: int):
        self.players.update(player.serialize_player, doc_ids=[int(player_id)])
