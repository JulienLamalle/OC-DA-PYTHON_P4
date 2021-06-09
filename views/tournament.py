from views.abstract import AbstractView


class TournamentView(AbstractView):
    
    def display_time_control_possibilities(self):
        print("Voici les différents choix possibles : ")
        print("1. Bullet")
        print("2. Blitz")
        print("3. Coup rapide")
        user_choice = 0
        while user_choice not in range (1, 4):
            try:
                user_choice = int(input("Quel time control souhaitez vous choisir ? :"))
                if user_choice not in range (1, 4):
                    print("Désolé mais votre choix ne correspond pas au possibilitées offertes")
                else: 
                    user_confirmation = self.request_confirmation()
                    if user_confirmation == "Y":
                        return self.perform_user_time_control_choice(user_choice)
            except (ValueError, TypeError):
                print("Désolé mais je n'ai pas compris votre choix, veuillez réessayer")
                
    @staticmethod
    def perform_user_time_control_choice(user_choice: int):
        switcher = {
            1: "Bullet",
            2: "Blitz",
            3: "Coup rapide"
        }
        return switcher.get(user_choice)