from cards import Deck, Card
from player import Player
import const


class Round:
    def __init__(self, round_number):
        self.round_number = round_number
        print(f"Round {self.round_number}...")
        self.players: list[Player] = []
        self.total_players = 0
        self.deck = Deck()
        self.card_stack: list[list[Card]] = []
        self.round_over = False
        self.result: dict = {}

    def add_players(self, players: list[str]):
        for player in players:
            self.players.append(Player(player))
        self.total_players = len(players)

    def distribute_cards(self, num_of_cards):
        if num_of_cards*len(self.players) > 49:
            raise Exception("not enough cards to distribute!")

        print(f"distributing {num_of_cards} cards to each player...")
        for _ in range(num_of_cards):
            for idx in range(self.total_players):
                card = self.deck.pop_a_card()
                self.players[idx].take_card(card)

    def show_down(self, current_player_idx: int):
        print(const.separation_line)
        caller_score = self.players[current_player_idx].value_of_cards()
        print(f"{self.players[current_player_idx].name} called \033[1m SHOW \033[0m of cards, "
              f"with a score of {caller_score} points")

        min_score = caller_score
        for player in self.players:
            player_score = player.value_of_cards()
            if player_score < min_score:
                min_score = player_score
                min_scorer = (player.name, player_score)
            self.result[player.name] = player_score

        if min_score == caller_score:
            print(f"{self.players[current_player_idx].name} won the round!!")
            self.result[self.players[current_player_idx].name] = 0
        else:
            print(f"{min_scorer[0]} has the least score of {min_scorer[1]}")
            print(f"{self.players[current_player_idx].name} got burst, and got a penalty of 40 points!!")
            self.result[self.players[current_player_idx].name] = 40

    def starting_player(self) -> int:
        self.round_number += 1
        return self.round_number % self.total_players

    def pick_a_card(self, current_player_idx):
        print(f"Since you changed the number, you have to pick card(s): \n"
              f"1. Last card(s) in the centre {len(self.card_stack[-1])} {self.card_stack[-1][0].value.value}(s), or \n"
              f"2. One card from the top of the Deck")
        while True:
            choice = input()
            if choice == "1" or choice == "2":
                break
            else:
                print("invalid choice; please retry")

        if choice == "1":
            top_cards = self.card_stack.pop(-1)
            print(f"picked card(s):", end=' ')
            for card in top_cards:
                self.players[current_player_idx].take_card(card)
                print(card, end=' ')
            print()

        if choice == "2":
            if self.deck.is_empty():
                self.deck.restore(self.card_stack[:-1])
                self.deck.shuffle()
                self.card_stack = [self.card_stack[-1]]
            card = self.deck.pop_a_card()
            print(f"picked card is {card}")
            self.players[current_player_idx].take_card(card)

    def play_card(self, current_player_idx):
        while True:
            chance = input("enter card to play (A/2-9/J/Q/K) or \'show\': \n").upper()

            if self.players[current_player_idx].is_valid_play(chance):
                break
            else:
                print("invalid entry! please retry")

        if chance == "SHOW":
            self.round_over = True
            self.show_down(current_player_idx)
            return None, chance

        return self.players[current_player_idx].play_card(chance), chance

    def player_turn(self, current_player_idx):
        print(const.separation_line)
        print(f"{self.players[current_player_idx].name}'s turn!")
        self.players[current_player_idx].show_in_hand_cards()

        played_cards, chance = self.play_card(current_player_idx)
        if self.round_over:
            return

        print(f"{self.players[current_player_idx].name} played {len(played_cards)} {chance}(s)")

        if played_cards[0].value != self.card_stack[-1][0].value:
            self.pick_a_card(current_player_idx)

        self.card_stack.append(played_cards)

    def starting_card(self):
        card = self.deck.pop_a_card()
        self.card_stack = [[card]]
        print(f"starting card is {card}")

    def controller(self, **kwargs):
        self.deck.shuffle()
        self.distribute_cards(kwargs.get('num_of_cards', 7))
        # todo: add zero card
        self.starting_card()

        current_player_idx = self.starting_player()
        while True:
            self.player_turn(current_player_idx)

            current_player_idx += 1
            current_player_idx %= self.total_players

            if self.round_over:
                break
