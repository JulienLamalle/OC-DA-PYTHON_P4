from views.abstract import AbstractView
from models.tournament import Tournament


class TournamentView(AbstractView):
    def display_time_control_possibilities(self):
        print("Voici les différents choix possibles : ")
        print("1. Bullet")
        print("2. Blitz")
        print("3. Coup rapide")
        user_choice = 0
        while user_choice not in range(1, 4):
            try:
                user_choice = int(input("Quel time control souhaitez vous choisir ? :"))
                if user_choice not in range(1, 4):
                    print(
                        "Désolé mais votre choix ne correspond pas au possibilitées offertes"
                    )
                else:
                    user_confirmation = self.request_confirmation()
                    if user_confirmation == "Y":
                        return self.perform_user_time_control_choice(user_choice)
            except (ValueError, TypeError):
                print("Désolé mais je n'ai pas compris votre choix, veuillez réessayer")

    @staticmethod
    def perform_user_time_control_choice(user_choice: int):
        switcher = {1: "Bullet", 2: "Blitz", 3: "Coup rapide"}
        return switcher.get(user_choice)

    def tournament_sub_menu(self, tournament: Tournament):
        print("Quelle action souhaitez vous effectuer ?")
        if tournament.current_round < 5:
            if (
                not tournament.players
                or len(tournament.serialize_tournament_players) < 8
            ):
                print("1. Ajouter des joueurs.")
                print("0. Quitter le tournoi.")
            else:
                print(f"1. Démarrer le tour : {tournament.current_round}.")
                print("2. Afficher la liste des participants.")
                print("3. Afficher la liste des rondes.")
                print("4. Afficher la liste des matches.")
                print("0. Quitter le tournoi.")
        else:
            print("1. Afficher le classement.")
            print("2. Afficher la liste des rondes.")
            print("3. Afficher la liste des matches.")
            print("0. Quitter le tournoi.")

    @staticmethod
    def display_tournament(
        tournament_id: int,
        name: str,
        location: str,
        start_date: str,
        end_date: str,
        time_control: str,
    ):
        print(
            f"{str(tournament_id)} | "
            f"{name} | "
            f"{location} | "
            f"{start_date} | "
            f"{end_date} | "
            f"{time_control}"
        )

    @staticmethod
    def print_current_tournament(tournament: Tournament):
        print(
            f"{'Ronde en cours'} | "
            f"{'Nom'} | "
            f"{'Lieu'} | "
            f"{'Date de début'} | "
            f"{'Date de fin'} | "
            f"{'Time control'}"
        )
        print(
            f"{str(tournament.current_round)} | "
            f"{tournament.name} | "
            f"{tournament.location} | "
            f"{tournament.start_date} | "
            f"{tournament.end_date} | "
            f"{tournament.time_control}"
        )

    @staticmethod
    def display_menu_tournament():
        print(f'{"* MENU TOURNAMENTS*"}'.center(119))
        print("1. Importez un tournoi.")
        print("0. Retour au menu principal.\n")
        print(f'{"=" * 119}')
