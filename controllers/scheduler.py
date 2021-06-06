import sys

from controllers.players import PlayersController
from controllers.tournaments import TournamentsController

class SchedulerController:
    def __init__(self):
        self.player_controller = PlayersController()
        self.tournament_controller = TournamentsController()
        
    def perform(self):
        user_choice = ""
        while user_choice != 0:
            self.tournament_controller.tournament_view.main_menu_who_display_possible_choice_to_user()
            user_choice = self.tournament_controller.tournament_view.get_user_choice(5)
            self.execute_user_choice(user_choice)
    
    def create_new_player(self):
        self.player_controller.create()
        self.perform()
    
    def create_new_tournament(self):
        self.tournament_controller.create()
        self.perform()
    
    def exit_program(self):
        self.tournament_controller.tournament_view.exit_program()
        sys.exit()
            
    def execute_user_choice(self, user_choice: int):
        commands =  {
            1: self.create_new_player,
            2: self.create_new_tournament,
            0: self.exit_program
        }
        getattr(commands[user_choice]())