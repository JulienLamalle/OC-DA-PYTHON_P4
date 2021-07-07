from views.abstract import AbstractView


class PlayerView(AbstractView):
    def get_player_sex(self):
        validation = ""
        while validation != "Y":
            sex = input("Veuillez saisir le sexe du joueur (M/F)").upper()
            if sex not in ["M", "F"]:
                print(
                    "Je n'ai pas pu identifier votre réponse, veuillez la saisir à nouveau s'il vous plaît."
                )
            else:
                print(f"Le sexe du jour est : {sex}")
                validation = self.request_confirmation()
                if validation == "Y":
                    return sex

    def print_players_tournament_ranking(self, players):
        print(
            f"{'Classement'.center(15)} | "
            f"{'Prénom'.center(30)} | "
            f"{'Nom'.center(30)} | "
            f"{'Score'.center(15)} | "
            f"{'Niveau'.center(15)}"
        )

        for player in players:
            print(
                f"{str(player.ladder).center(15)} | "
                f"{player.first_name.center(30)} | "
                f"{player.last_name.center(30)} | "
                f"{str(player.score).center(15)} | "
                f"{str(player.ranking).center(15)}"
            )
