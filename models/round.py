class Round:
    def __init__(self, name: str, created_at: str, finished_at: str = None, start: bool = True ):
        self.matchs = []
        self.name = name
        self.created_at = created_at
        self.finished_at = finished_at
        self.start = start

    @property
    def serialize_round(self):
        return {
            "name": self.name,
            "created_at": self.created_at,
            "finished_at": self.finished_at,
            "round_in_progress": self.start,
            "matchs": self.serialize_match,
            }
        
    @property
    def serialize_match(self):
        serialized_matchs = []
        for match in self.matchs:
            serialized_matchs.append(match.serialize_match)
        return serialized_matchs

