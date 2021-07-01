from abc import ABC
from views.player import PlayerView
from views.tournament import TournamentView
from views.round import RoundView
from controllers.database.players import PlayersDatabaseController
from controllers.database.tournaments import TournamentsDatabaseController

class AbstractController(ABC):
    def __init__(self):
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.round_view = RoundView()
        self.players_db = PlayersDatabaseController()
        self.tournaments_db = TournamentsDatabaseController()