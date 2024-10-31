from game import Game

game = Game(points=50)

# noinspection SpellCheckingInspection
game.add_players(players=['Vaibhav', 'Khushi'])

game.controller(num_of_cards=3)
