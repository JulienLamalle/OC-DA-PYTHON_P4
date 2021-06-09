from tinydb import TinyDB, Query

DATABASE = TinyDB("db/db.json")
TOURNAMENTS = DATABASE.table("TOURNAMENTS")


class TournamentsDatabaseController:
    def __init__(self):
        self.tournaments = TOURNAMENTS

    def save_tournament(self, tournament: object):
        self.tournaments.insert(tournament.serialize_tournament)
