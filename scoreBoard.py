class ScoreBoard:
    def __init__(self, players: list[str]):
        self.board: dict[str:int] = {}
        for player in players:
            self.board[player] = 0

    def __str__(self):
        return str(self.board)

    def update_scores(self, scores: dict[str:int]):
        for player in scores:
            self.board[player] += scores[player]

    def publish(self):
        print("the aggregate score of all rounds so far:")
        print(self)
