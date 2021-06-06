from tinydb import TinyDB, Query

DATABASE = TinyDB("db/db.json")
PLAYERS = DATABASE.table("PLAYERS")


class PlayersDatabaseController:
    
    def __init__(self):
        self.players = PLAYERS

    def save_player(self, player: object):
        self.players.insert(player.serialize_player)

    def search_in_players_table(self, first_name: str, last_name: str):
        for player in self.players:
            if player["first_name"] == first_name and player["last_name"] == last_name:
                existant_result = player
                return existant_result
        return None