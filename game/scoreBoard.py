class ScoreBoard:
    def __init__(self, players: list[str], score_limit: int):
        self.board: dict[str:int] = {}
        self.players = players
        self.score_limit = score_limit
        for player in players:
            self.board[player] = 0

    def __str__(self):
        return str(self.board)

    def update_scores(self, scores: dict[str:int]):
        for player in scores:
            self.board[player] += scores[player]

    def publish(self):
        print("the aggregated score of all rounds so far:")
        print(self)

    def eliminations(self, players):
        remaining_players = []
        for player in players:
            player_score = self.board[player]
            if player_score < self.score_limit:
                remaining_players.append(player)
            else:
                print(f"{player} got eliminated with a score of {player_score} points")

        return remaining_players
