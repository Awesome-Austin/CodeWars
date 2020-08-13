#! python3

import operator
from random import shuffle


class Hand:
    def __init__(self, tiles):
        self._suits = {
            **{c: {'type': 'simple', 'count': 9, 'sort': i} for i, c in enumerate('psm')},
            **{c: {'type': 'honor', 'count': 7, 'sort': 3} for c in 'z'}
        }
        self._tile_options = [(n+1, s) for s, s_info in self._suits.items()
                              for n in range(s_info['count']) for i in range(4)]
        self.tiles = [(int(n), suit) for n, suit in tiles.split(' ')]
        for tile in self.tiles:
            self._tile_options.remove(tile)

        self.winning_tiles = list()

        # print([x[0] for x in sorted(self._suits.items()[0], key=lambda x: x[1]['sort'])])

    def __repr__(self):
        return repr(self._sort_tiles(self.tiles.copy()))

    def __str__(self):
        return self._tiles_2_string(self.tiles.copy())

    def _sort_tiles(self, tiles):
        shuffle(tiles)
        sorted_tiles = [t for t, so
                        in sorted([(t, self._suits[t[1]]['sort']) for t in tiles], key=operator.itemgetter(1, 0))]
        return sorted_tiles

    def _tiles_2_string(self, tiles):
        return ' '.join([f'{n}{s}' for n, s in self._sort_tiles(tiles)])

    # def check

if __name__ == '__main__':
    tiles = "2p 2p 3p 3p 4p 4p 5p 5p 7m 7m 8m 8m 8m"
    hand = Hand(tiles)
    # print(hand.tiles)
    # print(hand._all_tiles)
    print(str(hand))
