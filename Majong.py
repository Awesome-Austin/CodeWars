#! python3

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

    def _tiles_string(self, tiles):
        return ''.join((f'{n}{s}' for s, ns in tiles.items() for n in ns))

    def __repr__(self):
        l = list()
        for



        return repr([(n, s) for s, ns in self.tiles.items() for n in ns])

    def __str__(self):
        return self._tiles_string(self.tiles)


if __name__ == '__main__':
    tiles = "2p 2p 3p 3p 4p 4p 5p 5p 7m 7m 8m 8m 8m"
    hand = Hand(tiles)
    # print(hand.tiles)
    # print(hand._all_tiles)
    print(repr(hand))
