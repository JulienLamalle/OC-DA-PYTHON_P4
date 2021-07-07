from views.abstract import AbstractView
from utils.utils import is_float as isFloat

from models.tournament import Tournament
class RoundView(AbstractView):
    @staticmethod
    def display_round_sub_menu():
        print("Menu des rondes")
        print("1. Inscrire les résultats")
        print("0. Annuler et revenir au menu du tournoi")

    @staticmethod
    def display_players_pair(first_player, second_player):
        print(
            f"{first_player.first_name.center(24)} | "
            f"{first_player.last_name.center(24)}"
            f"{second_player.first_name.center(24)} | "
            f"{second_player.last_name.center(24)}"
        )
        
    def set_player_score(self):
        validation = ""
        while validation != "Y":
            score = input("Entrez le score du joueur (celui-ci doit être un nombre): ")
            if not isFloat(score) or score is None:
                print("Nous n'avons pas compris votre saisie, veuillez saisir un nombre")
            else:
                validation = self.request_confirmation()
                if validation == "Y":
                    return float(score)
                
    @staticmethod        
    def display_rounds_header():
        print(
            f"{'Nom'.center(25)} | "
            f"{'Début de ronde'.center(35)} | "
            f"{'Fin de ronde'.center(35)}"
            f"\n{'°' * 100}"
        )
    
    @staticmethod
    def display_rounds_list(tournament: Tournament):
        for game_round in tournament.rounds:
            print(
                f"{game_round.name.center(25)} | "
                f"{game_round.created_at.center(35)} | "
                f"{game_round.finished_at.center(35)}"
                f"\n{'-' * 100}"
            )
            
    @staticmethod
    def display_matchs_list(tournament: Tournament):
        for game_round in tournament.rounds:
            print(f"\n{'=' * 119}")
            print(f"{'-' * 20}".center(119))
            print(f"{game_round.name.center(119)}")
            print(f"{'-' * 20}".center(119))
            print(
                f"{'Nom'.center(20)} | "
                f"{'Prénom'.center(20)} | "
                f"{'Score'.center(25)} | "
                f"{'Nom'.center(20)} | "
                f"{'Prénom'.center(20)}"
                f"\n{'°' * 119}"
            )
            for match in game_round.serialize_match:
                print(
                    f"{match['match'][0][0]['last_name'].center(20)} | "
                    f"{match['match'][0][0]['first_name'].center(20)} | "
                    f"{str(match['match'][0][1]).center(11)} | "
                    f"{str(match['match'][1][1]).center(11)} | "
                    f"{match['match'][1][0]['last_name'].center(20)} | "
                    f"{match['match'][1][0]['first_name'].center(20)}"
                    f"\n{'-' * 119}"
                )
        
