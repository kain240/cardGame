from player import Player
from round import Round
from scoreBoard import ScoreBoard


class Game:
    def __init__(self, points=100):
        print(f"starting a game of {points} points...")
        self.round_number = 0
        self.players: list[Player] = []
        self.score_board: ScoreBoard = None

    def add_players(self, players: list[str]):
        print("Players in the game: ")
        idx = 1
        for player in players:
            print(f"Player{idx}: {player}")
            self.players.append(Player(player))
            idx += 1

        self.score_board = ScoreBoard(players=self.players)

    def update_scoreboard(self, scores):
        self.score_board.update_scores(scores)

    def evaluate_game(self):
        self.score_board.publish()
        pass

    def controller(self, **kwargs):
        while len(self.players) > 1:
            self.round_number += 1
            new_round = Round(
                players=self.players,
                round_number=self.round_number
            )

            new_round.controller(**kwargs)

            results = new_round.result
            self.update_scoreboard(results)

            self.evaluate_game()

        print("Game Over!!!")
        print(f'{self.players[0].name} won')
