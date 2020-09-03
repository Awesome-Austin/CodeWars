
import operator

from collections import Counter


class MajongHand:
    def __init__(self, tiles):
        self._suits = {
            **{c: {'type': 'simple', 'count': 9, 'sort': i} for i, c in enumerate('psm')},
            **{c: {'type': 'honor', 'count': 7, 'sort': 3} for c in 'z'}
        }

        self.tiles = [(int(t[0]), t[1]) for t in tiles.split(' ')]
        self._winning_tiles = set()

        self.get_seven_pairs_tiles()
        self.get_regular_winning_hand()

    def _sort_tiles(self, tiles):
        sorted_tiles = [t for t, so
                        in sorted([(t, self._suits[t[1]]['sort']) for t in tiles], key=operator.itemgetter(1, 0))]
        return sorted_tiles

    def tiles_2_string(self, tiles):
        return ' '.join([f'{t[0]}{t[1]}' for t in self._sort_tiles(tiles)])

    def winning_tiles(self):
        return self.tiles_2_string(self._winning_tiles)

    def get_seven_pairs_tiles(self):
        counts = [t for t, c in Counter(self.tiles).items() if c % 2 == 1]
        if len(counts) == 1:
            self._winning_tiles.add(counts[0])

    def get_regular_winning_hand(self):
        def _get_regular_winning_hand(tiles, melds, pairs, singles):
            if len(singles) > 1:
                return

            if len(melds) > 4:
                return

            if sum([1 for m in melds if len(m) == 2]) > 1:
                return

            if sum([1 for m in melds if len(m) == 2]) == 1 and any([len(pairs) > 1, len(singles) > 0]):
                return

            if len(pairs) > 2:
                return

            for tile in set(tiles):
                if self._suits[tile[1]]['type'] == 'simple':
                    tile1 = (tile[0] + 1, tile[1])
                    tile2 = (tile[0] + 2, tile[1])
                    if tile1 in tiles:
                        temp_tiles = tiles.copy()
                        temp_tiles.remove(tile)
                        temp_tiles.remove(tile1)
                        yield from _get_regular_winning_hand(temp_tiles, melds.copy() + [(tile, tile1)],
                                                             pairs.copy(), singles.copy())

                    if tile2 in tiles:
                        temp_tiles = tiles.copy()
                        temp_tiles.remove(tile)
                        temp_tiles.remove(tile2)
                        yield from _get_regular_winning_hand(temp_tiles, melds.copy() + [(tile, tile2)],
                                                             pairs.copy(), singles.copy())

                    if tile1 in tiles and tile2 in tiles:
                        temp_tiles = tiles.copy()
                        temp_tiles.remove(tile)
                        temp_tiles.remove(tile1)
                        temp_tiles.remove(tile2)
                        yield from _get_regular_winning_hand(temp_tiles, melds.copy() + [(tile, tile1, tile2)],
                                                             pairs.copy(), singles.copy())

                if tiles.count(tile) >= 3:
                    temp_tiles = tiles.copy()
                    for i in range(3):
                        temp_tiles.remove(tile)
                    yield from _get_regular_winning_hand(temp_tiles, melds.copy() + [(tile, tile, tile)],
                                                         pairs.copy(), singles.copy())

                if tiles.count(tile) >= 2:
                    temp_tiles = tiles.copy()
                    for i in range(2):
                        temp_tiles.remove(tile)
                    yield from _get_regular_winning_hand(temp_tiles, melds.copy(), pairs.copy() + [(tile, tile)],
                                                         singles.copy())

                temp_tiles = tiles.copy()
                temp_tiles.remove(tile)
                yield from _get_regular_winning_hand(temp_tiles, melds.copy(), pairs.copy(), singles.copy() + [tile])

            temp_tiles = [t for m in melds for t in m] + [t for p in pairs for t in p] + singles

            if len(self.tiles) != len(temp_tiles):
                return

            if len(melds) == 3 and len(pairs) == 2:
                for pair in pairs:
                    yield pair[0]

            elif len(melds) == 4 and len(singles) == 1:
                yield singles[0]

            elif len(melds) == 4 and len(pairs) == 1:
                tile1, tile2 = [m for m in melds if len(m) == 2][0]

                if abs(tile2[0] - tile1[0]) == 1:
                    i, j = min(tile1[0], tile2[0]) - 1, max(tile1[0], tile2[0]) + 1
                    if i > 0:
                        yield i, tile1[1]

                    if j < 10:
                        yield j, tile1[1]

                elif abs(tile2[0] - tile1[0]) == 2:
                    yield min(tile1[0], tile2[0]) + 1, tile1[1]

            else:
                assert(False)

        for tile in _get_regular_winning_hand(self.tiles, list(), list(), list()):
            winning_tile = self._winning_tiles.add(tile)
            if winning_tile is not None:
                self._winning_tiles.add(winning_tile)


def solution(tiles):
    hand = MajongHand(tiles)
    return hand.winning_tiles()


if __name__ == '__main__':
    tiles = "2p 2p 3p 3p 4p 4p 5p 5p 7m 7m 8m 8m 8m"
    print(solution(tiles))
