from tinydb import TinyDB
from models.tournament import Tournament

DATABASE = TinyDB("db/db.json")
TOURNAMENTS = DATABASE.table("TOURNAMENTS")


class TournamentsDatabaseController:
    def __init__(self):
        self.tournaments = TOURNAMENTS

    def save_tournament(self, tournament: Tournament):
        self.tournaments.insert(tournament.serialize_tournament)

    def update_tournament(self, tournament: Tournament):
        self.tournaments.update(
            tournament.serialize_tournament, doc_ids=[tournament.tournament_id]
        )

    def search_tournament_by_id(self, tournament_id: int):
        tournament = self.tournaments.get(doc_id=int(tournament_id))
        if tournament:
            return tournament
        return None
