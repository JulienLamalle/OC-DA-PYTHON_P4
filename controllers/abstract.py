from abc import ABC
from views.player import PlayerView
from views.tournament import TournamentView
from controllers.database.players import PlayersDatabaseController
from controllers.database.tournaments import TournamentsDatabaseController

class AbstractController(ABC):
    def __init__(self):
        self.player_view = PlayerView()
        self.players_db = PlayersDatabaseController()
        self.tournament_view = TournamentView()
        self.tournaments_db = TournamentsDatabaseController()