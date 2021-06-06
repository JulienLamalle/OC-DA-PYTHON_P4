from models.player import Player
from controllers.abstract import AbstractController

class PlayersController(AbstractController):
    def create(self):
        first_name = self.player_view.get_string_value("le prénom", "joueur")
        last_name = self.player_view.get_string_value("le nom", "joueur")
        if not self.players_db.search_in_players_table(first_name, last_name):
            date_of_birth = self.player_view.get_string_value("la date de naissance", "joueur")
            sex = self.player_view.get_player_sex()
            ranking = self.player_view.get_integer_value("le rang", "joueur")
            player = Player(first_name, last_name, date_of_birth, sex , ranking)
            self.players_db.save_player(player)
            self.player_view.display_message_to_user(f"{first_name} {last_name} a bien été ajouté à la base de données")
        else:
            self.player_view.display_message_to_user(f"Le joueur {first_name} {last_name} existe déjà")
        