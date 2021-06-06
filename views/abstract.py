from abc import ABC


class AbstractView(ABC):
    
    @staticmethod
    def main_menu_who_display_possible_choice_to_user():
        print("1. Ajouter un nouveau joueur")
        print("2. Créer un tournoi")
        print("0. Quitter le programme")
        
    @staticmethod 
    def get_user_choice(limit_choice):
        user_choice = ""
        while user_choice not in range(0, limit_choice):
            try:
                user_choice = int(input("Choisissez ce que vous souhaitez faire :"))
            except (ValueError, TypeError):
                print("Désolé votre réponse n'est pas valide")
        return user_choice
    
    @staticmethod
    def exit_program():
        print("Merci d'avoir utilisé ce programme, à bientôt !")
        
    @staticmethod    
    def request_confirmation():
        validation = ""
        while validation not in ["Y", "N"]:
            validation = input("Confirmez-vous cela ? (Y/N)").upper()
            if validation not in ["Y", "N"]:
                print(
                    "Je n'ai pas pu identifier votre réponse, veuillez la saisir à nouveau s'il vous plaît."
                )
            return validation
        
    @staticmethod
    def display_message_to_user(message: str):
        print(f"{message}")

    def get_string_value(self, first_argument: str, second_argument: str):
        validate = ""
        while validate != "Y":
            value = input(f"Veuillez saisir {first_argument} du {second_argument}:")
            if not value:
                print(
                    f"Votre saisie n'a pas été comprise, veuillez rééssayer d'indiquer {first_argument} du {second_argument}"
                )
            else:
                print(f"{first_argument} du {second_argument} est : {value}")
                validate = self.request_confirmation()
                if validate == "Y":
                    return value

    def get_integer_value(self, first_argument: str, second_argument: str):
        validate = ""
        while validate != "Y":
            value = input(f"Veuillez saisir {first_argument} du {second_argument}:")
            if not value.isnumeric() or not value:
                print(
                    f"Votre saisie n'a pas été comprise, veuillez rééssayer d'indiquer {first_argument} du {second_argument}"
                )
            else:
                print(f"{first_argument} du {second_argument} est : {value}")
                validate = self.request_confirmation()
                if validate == "Y":
                    return value
                
