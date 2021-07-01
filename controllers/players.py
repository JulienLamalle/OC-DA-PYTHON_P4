from models.player import Player
from models.tournament import Tournament
from models.participant import Participant
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
        
    def set_players_list(self, tournament: Tournament):
        actual_players_number_for_tournament = len(tournament.serialize_tournament_players)
        while actual_players_number_for_tournament in range(0, 7):
            actual_players_number_for_tournament = len(tournament.serialize_tournament_players)
            if  actual_players_number_for_tournament == 0:
                self.player_view.display_message_to_user("Creez le 1er joueur")
            else:
                self.player_view.display_message_to_user(f"Creez le {actual_players_number_for_tournament + 1} joueur")
            first_name = self.player_view.get_string_value("le prénom", "joueur")
            last_name = self.player_view.get_string_value("le nom", "joueur")
            if [first_name, last_name] not in tournament.players:
                existing_player = self.players_db.search_in_players_table(first_name, last_name)
                if not existing_player:
                    date_of_birth = self.player_view.get_string_value("la date de naissance", "joueur")
                    sex = self.player_view.get_player_sex()
                    ranking = self.player_view.get_integer_value("le rang", "joueur")
                    player = Participant(first_name, last_name, date_of_birth, sex , ranking)
                    tournament.players.append(player)
                    self.players_db.save_player(Player(first_name, last_name, date_of_birth, sex, ranking))
                    player_found = self.players_db.search_in_players_table(first_name, last_name)
                    player.player_id = player_found.doc_id
                    self.player_view.display_message_to_user(f"Le joueur {player.first_name} {player.last_name} a bien été ajouté")
                else:
                    player = Participant(
                        existing_player["first_name"],
                        existing_player["last_name"],
                        existing_player["date_of_birth"],
                        existing_player["sex"],
                        existing_player["ranking"]
                    )
                    player.player_id = existing_player.doc_id
                    tournament.players.append(player)
                    self.player_view.display_message_to_user(f"Le joueur {player.first_name} {player.last_name} a bien été ajouté au tournoi")
            else:
                self.player_view.display_message_to_user(f"Le joueur {player.first_name} {player.last_name} est déjà présent dans le tournoi")
            self.tournaments_db.update_tournament(tournament)
        self.player_view.display_message_to_user("Tous les joueurs nécessaires ont été créés, le tournoi peut commencer")
        