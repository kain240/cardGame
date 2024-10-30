from player import Player


class ScoreBoard:
    def __init__(self, players: list[Player]):
        self.board: dict[str:int] = {}
        for player in players:
            self.board[player.name] = 0

    def __str__(self):
        return str(self.board)
        # return [f"{player}: {self.board[player]} points" for player in self.board]

    def update_scores(self, scores: dict[str:int]):
        for player in scores:
            self.board[player] += scores[player]

    def publish(self):
        print(self)
