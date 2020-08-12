#! python3

from collections import Counter


class Hand:
    def __init__(self, tiles):
        self._suits = {'simple': [9, 'psm'], 'honor': [7, 'z']}
        self._all_tiles = {
            suit: [i+1 for i in range(n) for j in range(4)] for n, suits in self._suits.values() for suit in suits
        }

        self.tiles = dict()
        for n, suit in tiles.split(' '):
            n = int(n)
            self.tiles.setdefault(suit, list())
            self.tiles[suit].append(n)
            self._all_tiles[suit].remove(n)

    def __str__(self):
        print([f'{s}{self.tiles[s]}' for n, suits in self._suits.values() for suit in suits for s in suit if s in self.tiles.keys()])




if __name__ == '__main__':
    tiles = "2p 2p 3p 3p 4p 4p 5p 5p 7m 7m 8m 8m 8m"
    hand = Hand(tiles)
    # print(hand.tiles)
    # print(hand._all_tiles)
    print(str(hand))