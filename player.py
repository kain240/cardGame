import uuid
import cards


class Player:
    def __init__(self, name):
        self.id = uuid.UUID
        self.name = name
        self.cards: list[cards.Card] = []

    def __str__(self):
        return self.name

    def show_in_hand_cards(self):
        for card in self.cards:
            print(card, end = ' ')
        print()

    def value_of_cards(self) -> int:
        total_value = 0
        for card in self.cards:
            total_value += card.value.value
        return total_value

    def take_card(self, card: cards.Card) -> None:
        self.cards.append(card)

    def is_valid_play(self, chance:str):
        if chance == "SHOW":
            return self.value_of_cards() <= 10

        card_to_play = cards.card_str_key[chance]

        for card in self.cards:
            if card.value == card_to_play:
                return True

        return False

    def play_card(self, number: str) -> list[cards.Card]:
        remaining_cards = []
        played_cards = []
        card_to_play = cards.card_str_key[number]
        for card in self.cards:
            if card.value == card_to_play:
                played_cards.append(card)
            else:
                remaining_cards.append(card)
        self.cards = remaining_cards
        return played_cards

    def show_cards(self) -> int:
        if self.value_of_cards() <= 10:
            return value_of_cards()
        else:
            print("invalid show!!")
            return -1
