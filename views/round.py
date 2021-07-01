from views.abstract import AbstractView
from utils.utils import is_float as isFloat

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
