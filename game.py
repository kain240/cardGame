from round import Round
from scoreBoard import ScoreBoard
import const


class Game:
    def __init__(self, points=100):
        print(const.separation_line)
        print(f"starting a game of {points} points...")
        self.round_number = 0
        self.players: list[str] = []
        # noinspection PyTypeChecker
        self.score_board: ScoreBoard = None
        self.score_limit = points

    def add_players(self, players: list[str]):
        print("Players in the game: ")
        for idx in range(len(players)):
            print(f"Player{idx}: {players[idx]}")
        self.players = players

        self.score_board = ScoreBoard(players=self.players, score_limit=self.score_limit)

    def update_scoreboard(self, scores):
        print(const.separation_line)
        print("result of this round:")
        print(str(scores))
        self.score_board.update_scores(scores)
        self.score_board.publish()

    def evaluate_game(self):
        print(const.separation_line)
        self.players = self.score_board.eliminations(self.players)

    def controller(self, **kwargs):
        print(const.separation_line)
        while len(self.players) > 1:
            self.round_number += 1
            input(f"press \'enter\' to start round{self.round_number}?")

            new_round = Round(
                round_number=self.round_number
            )
            new_round.add_players(self.players)

            new_round.controller(**kwargs)

            self.update_scoreboard(new_round.result)

            self.evaluate_game()

        print("Game Over!!!")
        print(f'{self.players[0]} won')
