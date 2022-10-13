from random import shuffle


class DeckOfCards:
    def __init__(self):
        self.suits = tuple('♠ ♣ ♦ ♥'.split())
        self.numbers = tuple(list(range(2, 11)) + 'J Q K A'.split())
        self.cards = [f'{n}{s}' for n in self.numbers for s in self.suits]

    def shuffle(self):
        shuffle(self.cards)

    def deal_cards(self, deal_num, shuffle_deck=True):
        if shuffle_deck:
            self.shuffle()
        return [self.cards.pop(0) for i in range(deal_num)]
