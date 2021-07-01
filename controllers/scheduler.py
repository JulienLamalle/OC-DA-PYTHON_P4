import sys

from controllers.players import PlayersController
from controllers.tournaments import TournamentsController

from models.tournament import Tournament

class SchedulerController:
    def __init__(self):
        self.player_controller = PlayersController()
        self.tournament_controller = TournamentsController()
        
    def perform(self):
        user_choice = ""
        while user_choice != 0:
            self.tournament_controller.tournament_view.main_menu_who_display_possible_choice_to_user()
            user_choice = self.tournament_controller.tournament_view.get_user_choice(6)
            self.execute_user_choice(user_choice)
    
    def create_new_player(self):
        self.player_controller.create()
        self.perform()
    
    def create_new_tournament(self):
        tournament = self.tournament_controller.create()
        if tournament:
            self.get_tournament_user_choice(tournament)
        self.perform()
    
    def exit_program(self):
        self.tournament_controller.tournament_view.exit_program()
        sys.exit()
            
    def execute_user_choice(self, user_choice: int):
        commands =  {
            1: self.create_new_player,
            2: self.create_new_tournament,
            3: self.use_existing_tournament,
            0: self.exit_program
        }
        getattr(commands[user_choice]())
        
    
    def use_existing_tournament(self):
        self.tournament_controller.tournament_view.display_message_to_user("Utiliser un tournoi déjà existant")
        self.tournament_controller.index()
        tournament = self.tournament_controller.select_tournament()
        if tournament:
            self.get_tournament_user_choice(tournament)
        self.perform()
        
    def get_tournament_user_choice(self, tournament: Tournament):
        user_choice = ""
        while user_choice != 0:
            self.tournament_controller.tournament_view.tournament_sub_menu(tournament)
            user_choice = self.tournament_controller.tournament_view.get_user_choice(5)
            self.tournament_perform(user_choice, tournament)
            
    def tournament_perform(self, user_choice, tournament: Tournament):
        if tournament.current_round <= 4:
            if (not tournament.players or len(tournament.serialize_tournament_players) < 8):
                if user_choice == 1:
                    self.tournament_controller.tournament_view.display_message_to_user(
                        "Créez 8 joueurs."
                    )
                    self.player_controller.set_players_list(tournament)
                elif user_choice == 0:
                    self.perform()
            else:
                if user_choice == 1:
                    self.tournament_controller.tournament_view.display_message_to_user(
                        "Tournoi en cours."
                    )
                    self.tournament_controller.start_tournament_rounds(tournament)
                elif user_choice == 2:
                    self.tournament_controller.tournament_view.print_current_tournament(
                        tournament
                    )
                    self.tournament_controller.tournament_view.display_message_to_user(
                        "Liste des participants."
                    )
                    self.tournament_controller.print_tournament_players(tournament)
                elif user_choice == 3:
                    self.tournament_controller.tournament_view.print_current_tournament(
                        tournament
                    )
                    self.tournament_controller.tournament_view.display_message_to_user(
                        "Liste des rondes."
                    )
                    self.tournament_controller.print_rounds_tournament(tournament)
                elif user_choice == 4:
                    self.tournament_controller.tournament_view.print_current_tournament(
                        tournament
                    )
                    self.tournament_controller.tournament_view.display_message_to_user(
                        "Liste des matches."
                    )
                    self.tournament_controller.print_matches_tournament(tournament)
                elif user_choice == 0:
                    self.perform()
            user_choice = ""
        else:
            if user_choice == 1:
                self.tournament_controller.tournament_view.print_current_tournament(
                    tournament
                )
                self.tournament_controller.tournament_view.display_message_to_user(
                    "Résultat du tournoi"
                )
                self.tournament_controller.print_players_tournament(tournament)
            elif user_choice == 2:
                self.tournament_controller.tournament_view.print_current_tournament(
                    tournament
                )
                self.tournament_controller.tournament_view.display_message_to_user("Liste des rondes.")
                self.tournament_controller.print_rounds_tournament(tournament)
            elif user_choice == 3:
                self.tournament_controller.tournament_view.print_current_tournament(
                    tournament
                )
                self.tournament_controller.tournament_view.display_message_to_user("Liste des mathes.")
                self.tournament_controller.print_matches_tournament(tournament)
            if user_choice == 0:
                self.perform()