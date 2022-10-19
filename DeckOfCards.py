from random import shuffle
from collections import namedtuple

VALUES = {'J': 11, 'Q': 12, 'K': 13, 'A': [1, 14]}


class PlayingCard:
    def __init__(self, face, suit, **kwargs):
        self.face = face
        self.suit = suit
        try:
            self.value = kwargs.pop('value')

        except KeyError:
            try:
                self.value = int(face)
            except ValueError:
                if kwargs.get('aces_high', None) is not None and self.face == 'A':
                    if kwargs['aces_high']:
                        self.value = max(VALUES[self.face])
                    else:
                        self.value = min(VALUES[self.face])
                else:
                    self.value = VALUES[self.face]

    def __repr__(self):
        return f'PlayingCard(face={self.face}, suit={self.suit}, value={self.value})'

    def __str__(self):
        return f'{self.face}{self.suit}'

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        return not self.__gt__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


class DeckOfCards:
    def __init__(self, *args, **kwargs):
        self.suits = tuple('♠ ♣ ♦ ♥'.split())
        self.numbers = tuple(list(range(2, 11)) + 'J Q K A'.split())
        self.cards = [PlayingCard(face=n, suit=s, **kwargs) for s in self.suits for n in self.numbers]

    def shuffle(self):
        shuffle(self.cards)

    def deal_cards(self, deal_num, shuffle_deck=True):
        if shuffle_deck:
            self.shuffle()
        return [self.cards.pop(0) for i in range(deal_num)]


if __name__ == '__main__':
    doc = DeckOfCards(aces_high=False)
    doc.shuffle()
    hand_1 = doc.deal_cards(5, shuffle_deck=False)
    hand_2 = doc.deal_cards(5, shuffle_deck=False)
    max(hand_1)
    max(hand_2)
    print()
