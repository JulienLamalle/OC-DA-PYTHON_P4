from views.abstract import AbstractView

class PlayerView(AbstractView):
  def get_player_sex(self):
    validation = ""
    while validation != "Y":
      sex = input("Veuillez saisir le sexe du joueur (M/F)").upper()
      if sex not in ["M", "F"]:
        print("Je n'ai pas pu identifier votre réponse, veuillez la saisir à nouveau s'il vous plaît.")
      else:
        print(f"Le sexe du jour est : {sex}")
        validation = self.request_confirmation()
        if validation == "Y": 
          return sex