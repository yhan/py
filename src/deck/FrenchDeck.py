import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high_ordering(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

def spades_high_ordering_suit_first(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return suit_values[card.suit] * len(FrenchDeck.ranks) + rank_value

deck = FrenchDeck()

def setcard(deck, position, card):
    deck._cards[position] = card


FrenchDeck.__setitem__ = setcard

deck[10] = Card('0', 'KING')
print(deck[10])


def card_to_str(card):
    return '%s of %s' %card

Card.__str__ = card_to_str
print(deck[10])


for c in deck.__iter__():
    print(c)
