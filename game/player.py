import uuid
from . import cards


class Player:
    def __init__(self, name):
        self.id = uuid.UUID
        self.name = name
        self.cards: list[cards.Card] = []

    def __str__(self):
        return self.name

    def show_in_hand_cards(self):
        for card in self.cards:
            print(card, end=' ')
        print()

    def value_of_cards(self, zero_card: cards.Card) -> int:
        total_value = 0

        for card in self.cards:
            if card.rank == zero_card.rank:
                card_val = 0
            elif card.rank.value.value >= 10:
                card_val = 10
            else:
                card_val = card.rank.value.value

            total_value += card_val

        return total_value

    # noinspection PyShadowingNames
    def take_card(self, card: cards.Card) -> None:
        self.cards.append(card)
        self.cards.sort(key=lambda card: card.rank.value.value)

    def is_valid_play(self, chance: str, zero_card: cards.Card):
        if chance == '':
            return False

        if chance == "SHOW":
            return self.value_of_cards(zero_card=zero_card) <= 10

        card_to_play = cards.get_card_rank(chance)

        for card in self.cards:
            if card.rank == card_to_play:
                return True

        return False

    def play_card(self, number: str) -> list[cards.Card]:
        remaining_cards = []
        played_cards = []
        card_to_play = cards.get_card_rank(number)
        for card in self.cards:
            if card.rank == card_to_play:
                played_cards.append(card)
            else:
                remaining_cards.append(card)
        self.cards = remaining_cards
        return played_cards
