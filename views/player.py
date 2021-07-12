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

    @staticmethod
    def display_players_sub_menu():
        print(f'{"* MENU PLAYERS*"}'.center(119))
        print("1. Ajouter un joueur.")
        print("2. Modifier le classement 'ranking' d'un joueur.")
        print("3. Afficher par 'ranking'.")
        print("0. Retour au menu principal.\n")
        print(f'{"=" * 119}')

    @staticmethod
    def display_players_header():
        print(
            f"{'ID'.center(10)} | "
            f"{'Prénom'.center(25)} | "
            f"{'Nom'.center(25)} | "
            f"{'Date de naissance'.center(20)} | "
            f"{'Sexe'.center(10)} | "
            f"{'Ranking'.center(10)}"
            f"\n{'°' * 119}"
        )

    @staticmethod
    def display_player(
        player_id: int,
        first_name: str,
        last_name: str,
        date_of_birth: str,
        sex: str,
        ranking: str,
    ):
        print(
            f"{str(player_id).center(10)} | "
            f"{first_name.center(25)} | "
            f"{last_name.center(25)} | "
            f"{date_of_birth.center(20)} | "
            f"{sex.center(10)} | "
            f"{str(ranking).center(10)}"
            f"\n{'-' * 119}"
        )
