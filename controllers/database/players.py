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