from player import Player
from round import Round
from scoreBoard import ScoreBoard


class Game:
    def __init__(self, points=100):
        print(f"starting a game of {points} points...")
        self.round_number = 0
        self.players: list[str] = []
        self.score_board: ScoreBoard = None

    def add_players(self, players: list[str]):
        print("Players in the game: ")
        for idx in range(len(players)):
            print(f"Player{idx}: {players[idx]}")
        self.players = players

        self.score_board = ScoreBoard(players=self.players)

    def update_scoreboard(self, scores):
        print("result of this round:")
        print(str(scores))
        self.score_board.update_scores(scores)
        self.score_board.publish()

    def controller(self, **kwargs):
        # todo: remove player as they hit score
        while len(self.players) > 1:
            self.round_number += 1
            input(f"press \'enter\' to start round{self.round_number}?")

            new_round = Round(
                round_number=self.round_number
            )
            new_round.add_players(self.players)

            new_round.controller(**kwargs)

            results = new_round.result
            self.update_scoreboard(results)

        print("Game Over!!!")
        print(f'{self.players[0]} won')
