import enum
import random


class Suits(enum.Enum):
    Spade = "♠️"
    Heart = "♥️"
    Club = "♣️"
    Diamond = "♦️"


class DecodeRank:
    def __init__(self, value, code):
        self.value = value
        self.code = code


class Rank(enum.Enum):
    Ace   = DecodeRank(1, 'A')
    Two   = DecodeRank(2, '2')
    Three = DecodeRank(3, '3')
    Four  = DecodeRank(4, '4')
    Five  = DecodeRank(5, '5')
    Six   = DecodeRank(6, '6')
    Seven = DecodeRank(7, '7')
    Eight = DecodeRank(8, '8')
    Nine  = DecodeRank(9, '9')
    Ten   = DecodeRank(10, 'T')
    Jack  = DecodeRank(11, 'J')
    Queen = DecodeRank(12, 'Q')
    King  = DecodeRank(13, 'K')


card_str_to_rank = {
    'A': Rank.Ace,
    '2': Rank.Two,
    '3': Rank.Three,
    '4': Rank.Four,
    '5': Rank.Five,
    '6': Rank.Six,
    '7': Rank.Seven,
    '8': Rank.Eight,
    '9': Rank.Nine,
    'T': Rank.Ten,
    'J': Rank.Jack,
    'Q': Rank.Queen,
    'K': Rank.King,
}
def get_card_rank(code:str) -> Rank:
    if code not in card_str_to_rank:
        raise KeyError(f"invalid code: {code}")
    return card_str_to_rank[code]

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit.value}{self.rank.value.code}"


class Deck:
    def __init__(self, card_stack: list[list[Card]] | None = None):
        self.cards = []

        if not card_stack:
            for suit in Suits:
                for num in Rank:
                    self.cards.append(Card(suit, num))
        else:
            for cards in card_stack:
                for card in cards:
                    self.cards.append(card)

    def restore(self, card_stack: list[list[Card]]):
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

    def is_empty(self):
        return self.size() == 0

    def pop_a_card(self) -> Card:
        if self.is_empty():
            raise Exception("deck is empty")
        return self.cards.pop(0)
