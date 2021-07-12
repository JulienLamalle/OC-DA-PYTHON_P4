from controllers.abstract import AbstractController
from models.tournament import Tournament
from models.participant import Participant
from models.round import Round
from models.match import Match

from datetime import datetime
import time


class TournamentsController(AbstractController):
    def index(self):
        if self.tournaments_db:
            for tournament in self.tournaments_db.tournaments:
                self.tournament_view.display_tournament(
                    tournament.doc_id,
                    tournament["name"],
                    tournament["location"],
                    tournament["start_date"],
                    tournament["end_date"],
                    tournament["time_control"],
                )
            return self.tournaments_db.tournaments
        self.tournament_view.display_message_to_user(
            "Nous n'avons trouvé aucun tournoi dans la base de données"
        )
        return None

    def create(self):
        name = self.tournament_view.get_string_value("le nom", "tournoi")
        location = self.tournament_view.get_string_value("la localisation", "tournoi")
        start_date = self.tournament_view.get_string_value(
            "la date du début", "tournoi"
        )
        end_date = self.tournament_view.get_string_value("la date de fin", "tournoi")
        description = self.tournament_view.get_string_value("la description", "tournoi")
        time_control = self.tournament_view.display_time_control_possibilities()
        tournament = Tournament(
            name, location, start_date, end_date, description, time_control
        )
        self.tournaments_db.save_tournament(tournament)
        self.tournament_view.display_message_to_user(
            f"Le tournoi {tournament.name} a été crée avec succès"
        )
        return tournament

    def select_tournament(self):
        tournament_id = self.tournament_view.get_integer_value("l'id", "tournoi")
        existing_tournament = self.tournaments_db.search_tournament_by_id(tournament_id)
        if existing_tournament:
            self.tournament_view.display_tournament(
                existing_tournament.doc_id,
                existing_tournament["name"],
                existing_tournament["location"],
                existing_tournament["start_date"],
                existing_tournament["end_date"],
                existing_tournament["time_control"],
            )
            tournament = Tournament(
                existing_tournament["name"],
                existing_tournament["location"],
                existing_tournament["start_date"],
                existing_tournament["end_date"],
                existing_tournament["description"],
                existing_tournament["time_control"],
            )
            tournament.tournament_id = existing_tournament.doc_id
            if existing_tournament["players"]:
                for existing_player in existing_tournament["players"]:
                    player = Participant(
                        existing_player["first_name"],
                        existing_player["last_name"],
                        existing_player["date_of_birth"],
                        existing_player["sex"],
                        existing_player["ranking"],
                    )
                    player.player_id = self.players_db.get_player_id(
                        existing_player["first_name"],
                        existing_player["last_name"],
                    )
                    player.score = existing_player["score"]
                    player.ladder = existing_player["ladder"]
                    for opponent in existing_player["opponents"]:
                        player.opponents.append(opponent)
                    tournament.players.append(player)
            if existing_tournament["rounds"]:
                for existing_round in existing_tournament["rounds"]:
                    game_round = Round(
                        existing_round["name"], existing_round["created_at"]
                    )
                    game_round.start = existing_round["round_in_progress"]
                    game_round.finished_at = existing_round["finished_at"]
                    tournament.rounds.append(game_round)
                    for existing_match in existing_round["matchs"]:
                        match = Match(
                            existing_match["match"][0][0],
                            existing_match["match"][1][0],
                            existing_match["match"][0][1],
                            existing_match["match"][1][1],
                        )
                        game_round.matchs.append(match)
            tournament.current_round = existing_tournament["current_round"]
            tournament.tournament_id = existing_tournament.doc_id
            self.tournament_view.display_message_to_user(
                f"Le tournoi {tournament.name} a correctement été trouvé et importé !"
            )
            return tournament
        else:
            self.tournament_view.display_message_to_user(
                "Aucun tournoi n'a pu être trouvé"
            )
            return None

    def print_tournament_players(self, tournament: Tournament):
        self.player_view.print_players_tournament_ranking(
            tournament.sort_players_by_score()
        )

    def start_tournament_rounds(self, tournament: Tournament):
        if tournament.current_round <= 4:
            index = 1
            name = f"Round {tournament.current_round}"
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            game_round = Round(name, str(created_at))
            self.round_view.display_round_sub_menu()
            if tournament.current_round == 1:
                self.round_view.display_message_to_user("Première ronde")
                players_pairs = tournament.generate_first_round_pairs()
            else:
                self.round_view.display_message_to_user(
                    f"{tournament.current_round}ème round"
                )
                players_pairs = tournament.generate_pairs()
            if players_pairs:
                confirm = ""
                while confirm != "Y":
                    self.round_view.display_round_sub_menu()
                    for first_player, second_player in players_pairs:
                        self.round_view.display_players_pair(
                            first_player, second_player
                        )
                    self.round_view.display_message_to_user(
                        f"{game_round.name} est en cours, Patientez jusque la fin des matchs avant d'inscrire les résultats"
                    )
                    self.round_view.display_message_to_user(
                        "Si vous quittez celle-ci, la ronde sera supprimée"
                    )
                    user_choice = self.round_view.get_user_choice(2)
                    if user_choice == 0:
                        self.round_view.display_message_to_user(
                            "Si vous quittez maintenant la ronde, celle-ci sera supprimée"
                        )
                        confirm = self.round_view.request_confirmation()
                        if confirm == "Y":
                            return
                    else:
                        self.start_round(game_round, players_pairs, tournament, index)
                        return
            else:
                self.round_view.display_message_to_user(
                    "Oula, quelque chose s'est mal passé, merci de recommencer"
                )
                return
        else:
            self.round_view.display_message_to_user(
                "Ce tournoi est maintenant terminée"
            )
            return

    def start_round(self, game_round, players_pairs, tournament, index):
        for first_player, second_player in players_pairs:
            self.round_view.display_message_to_user(f"Le match {index} commence.")
            self.round_view.display_message_to_user(
                f"\nJoueur : {first_player.first_name} {first_player.last_name}\n"
            )
            first_player_score = self.round_view.set_player_score()
            first_player.score += first_player_score
            self.round_view.display_message_to_user(
                f"\nJoueur : {second_player.first_name} {second_player.last_name}\n"
            )
            second_player_score = self.round_view.set_player_score()
            second_player.score += second_player_score
            match = Match(
                first_player.serialize_match_player,
                second_player.serialize_match_player,
                first_player_score,
                second_player_score,
            )
            game_round.matchs.append(match)
            index += 1
        tournament.rounds.append(game_round)
        tournament.current_round += 1
        game_round.finished_at = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        game_round.start = False
        if tournament.current_round == 5:
            ladder = 1
            for player in tournament.sort_players_by_score():
                player.ladder = ladder
                ladder += 1
            self.round_view.display_message_to_user(
                f"Le tournoi est TERMINÉ! Vous pouvez désormais afficher les résultats"
            )
        else:
            self.round_view.display_message_to_user(
                f"Le tour {tournament.current_round - 1} est terminé !"
            )
        self.tournaments_db.update_tournament(tournament)

    def display_tournament_rounds(self, tournament: Tournament):
        self.round_view.display_rounds_header()
        self.round_view.display_rounds_list(tournament)
        validation = self.round_view.request_user_validation_for_return()
        if validation == "Y":
            return

    def display_tournament_matchs(self, tournament: Tournament):
        self.round_view.display_matchs_list(tournament)
        validation = self.round_view.request_user_validation_for_return()
        if validation == "Y":
            return
