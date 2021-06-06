from controllers.abstract import AbstractController
from models.tournament import Tournament

class TournamentsController(AbstractController):
  def create(self):
    print("Fonction pour créer un tournoi")