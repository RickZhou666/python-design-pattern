# Card class

from enum import Enum


class Suit(Enum):
    CLUBS = 1
    SPADES = 2
    HEARTS = 3
    DIAMONDS = 4

class Card:
    def __init__(self, value, suit: Suit) -> None:
        self.value = value
        self.suit = suit


class BlackJackCard(Card):
    def __init__(self, value, suit: Suit) -> None:
        super().__init__(value, suit)
    
    def value(self):
        if self.value == 1:
            return 11
        elif self.value < 10:
            return self.value
        return 10
    
    def is_ace():
        return super().value == 1