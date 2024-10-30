import enum
import random


class Suits(enum.Enum):
    Spade = "♠️"
    Heart = "♥️"
    Club = "♣️"
    Diamond = "♦️"


class Value(enum.Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 10
    Queen = 10
    King = 10


card_str_key = {
    'A': Value.Ace,
    '2': Value.Two,
    '3': Value.Three,
    '4': Value.Four,
    '5': Value.Five,
    '6': Value.Six,
    '7': Value.Seven,
    '8': Value.Eight,
    '9': Value.Nine,
    'T': Value.Ten,
    'J': Value.Jack,
    'Q': Value.Queen,
    'K': Value.King,
}


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        for key in card_str_key:
            if self.value == card_str_key[key]:
                return f"{self.suit.value}{key}"


class Deck:
    def __init__(self, card_stack: list[list[Card]] | None = None):
        self.cards = []

        if not card_stack:
            for suit in Suits:
                for num in Value:
                    self.cards.append(Card(suit, num))
        else:
            for cards in card_stack:
                for card in cards:
                    self.cards.append(card)

    def shuffle(self):
        shuffled_deck = []
        for idx in range(self.size()):
            random_card_num = random.randint(0, len(self.cards) - 1)
            shuffled_deck.append(self.cards[random_card_num])
            self.cards.pop(random_card_num)
        self.cards = shuffled_deck

    def size(self):
        return len(self.cards)

    def pop_a_card(self) -> Card:
        card = self.cards[0]
        self.cards.pop(0)
        return card
