from controllers.abstract import AbstractController
from models.tournament import Tournament


class TournamentsController(AbstractController):
    def create(self):
        name = self.tournament_view.get_string_value("le nom", "tournoi")
        location = self.tournament_view.get_string_value("la localisation", "tournoi")
        start_date = self.tournament_view.get_string_value("la date du début", "tournoi")
        end_date = self.tournament_view.get_string_value("la date de fin", "tournoi")
        description = self.tournament_view.get_string_value("la description", "tournoi")
        time_control = self.tournament_view.display_time_control_possibilities()
        tournament = Tournament(name, location, start_date, end_date, description, time_control)
        self.tournaments_db.save_tournament(tournament)
        self.tournament_view.display_message_to_user(f"Le tournoi {tournament.name} a été crée avec succès")
        return tournament