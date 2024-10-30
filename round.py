from cards import Deck, Card


class Round:
    def __init__(self, players, round_number):
        self.round_number = round_number
        print(f"Round {self.round_number}...")
        self.players = players
        self.total_players = len(players)
        self.deck = Deck()
        self.card_stack: list[list[Card]] = []
        self.round_over = False
        self.result: dict = {}

    def distribute_cards(self, num_of_cards):
        print(f"distributing {num_of_cards} cards to each player...")
        for _ in range(num_of_cards):
            for idx in range(self.total_players):
                card = self.deck.pop_a_card()
                self.players[idx].take_card(card)

    def show_down(self):
        # todo: implement burst
        for player in self.players:
            self.result[player.name] = player.value_of_cards()

    def starting_player(self) -> int:
        self.round_number += 1
        return self.round_number % self.total_players

    def player_turn(self, current_player_idx):
        print(f"{self.players[current_player_idx].name}'s turn!")
        self.players[current_player_idx].show_in_hand_cards()

        while True:
            chance = input("enter card to play (A/2-9/J/Q/K) or \'show\': \n").upper()

            if self.players[current_player_idx].is_valid_play(chance):
                break
            else:
                print("invalid! retry")

        if chance == "SHOW":
            self.round_over = True
            self.show_down()
            return

        played_cards = self.players[current_player_idx].play_card(chance)
        print(f"{self.players[current_player_idx].name} played {len(played_cards)} {chance}")
        self.card_stack.append(played_cards)
        # todo: implement picking a card

    def controller(self, **kwargs):
        self.deck.shuffle()
        self.distribute_cards(kwargs.get('num_of_cards', 7))

        current_player_idx = self.starting_player()
        while True:
            self.player_turn(current_player_idx)

            current_player_idx += 1
            current_player_idx %= self.total_players

            if self.round_over:
                break
