#! python3

import collections
import operator


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

        self.winning_tiles = set()

    def __repr__(self):
        return repr(self._sort_tiles(self.tiles.copy()))

    def __str__(self):
        return self._tiles_2_string(self.tiles.copy())

    def _sort_tiles(self, tiles):
        sorted_tiles = [t for t, so
                        in sorted([(t, self._suits[t[1]]['sort']) for t in tiles], key=operator.itemgetter(1, 0))]
        return sorted_tiles

    def _tiles_2_string(self, tiles):
        return ' '.join([f'{n}{s}' for n, s in self._sort_tiles(list(tiles))])

    def check_seven_pair(self):
        # Checks if there are seven doubles
        groups = [k for k, v in collections.Counter(self.tiles).items() if v % 2 == 1]
        if len(groups) == 1 and groups[0] in self._tile_options:
            self.winning_tiles.add(groups[0])
            return True
        return False

    def check_regular_hands(self):
        def _check_regular_hands(melds, pairs, singles, tiles):
            while tiles:
                tile = tiles.pop(0)
                try:
                    assert tile not in [(6, 'm'), (7, 'm'), (8, 'm'), (9, 'm')]
                except:
                    pass
                if self._suits[tile[1]]['type'] == 'simple':
                    run0, run1, run2 = (tile[0] - 1, tile[1]), (tile[0] + 1, tile[1]), (tile[0] + 2, tile[1])

                    if any([run0 in tiles, run1 in tiles]):
                        temp_tiles = tiles.copy()
                        try:
                            temp_tiles.remove(run0)
                        except ValueError:
                            run0 = None

                        try:
                            temp_tiles.remove(run1)
                        except ValueError:
                            run1 = None
                        yield from _check_regular_hands(melds.copy() + [(run0, tile, run1)],
                                                        pairs.copy(), singles.copy(), temp_tiles)

                    if any([run1 in tiles, run2 in tiles]):
                        temp_tiles = tiles.copy()

                        try:
                            temp_tiles.remove(run1)
                        except ValueError:
                            run1 = None

                        try:
                            temp_tiles.remove(run2)
                        except ValueError:
                            run2 = None

                        yield from _check_regular_hands(melds.copy() + [(tile, run1, run2)],
                                                        pairs.copy(), singles.copy(), temp_tiles)

                if tiles.count(tile) > 1:
                    temp_tiles = tiles.copy()
                    temp_tiles.remove(tile)
                    temp_tiles.remove(tile)

                    yield from _check_regular_hands(melds.copy() + [(tile, tile, tile)],
                                                    pairs.copy(), singles.copy(), temp_tiles)

                if tiles.count(tile) == 1:
                    temp_tiles = tiles.copy()
                    temp_tiles.remove(tile)
                    yield from _check_regular_hands(melds.copy(), pairs.copy() + [(tile, tile)],
                                                    singles.copy(), temp_tiles)

                if tiles.count(tile) == 0:
                    yield from _check_regular_hands(melds.copy(), pairs.copy(), singles.copy() + [tile],
                                                    tiles.copy())

            if any([
                len(melds) > 4,
                len(melds) < 3 and len(pairs) == 0,
                len(pairs) > 2,
                len(pairs) > 2,
                len(singles) > 2,
                # len([m for m in melds if None in m]) > 1
            ]):
                pass

            elif len(melds) == 4 and len(pairs) == 1 and len([m for m in melds if None in m]) == 1:
                meld = [m for m in melds if None in m]
                meld = meld[0]
                yield meld[0][0] + meld.index(None), meld[0][1]

            elif sum([len(melds) * 3, len(pairs) * 2, len(singles)]) != 13:
                pass

            elif len(singles) == 1:
                yield singles[0]

            elif len(singles) == 2:
                tile1, tile2 = singles
                dif = abs(tile1[0] - tile2[0])

                if all([tile1[1] == tile2[1], dif < 3]):
                    if dif == 2:
                        yield min(tile1[0], tile2[0]) + 1, tile1[1]

                    elif dif == 1:
                        yield min(tile1[0], tile2[0]) - 1, tile1[1]
                        yield max(tile1[0], tile2[0]) + 1, tile1[1]

            elif len(pairs) == 2:
                for pair in pairs:
                    yield pair[0]

        for added_tile in _check_regular_hands(list(), list(), list(), self._sort_tiles(self.tiles.copy())):
            self.winning_tiles.add(added_tile)

    def get_winning_tiles(self):
        self.check_seven_pair()
        self.check_regular_hands()

        return self._tiles_2_string(self.winning_tiles)


def solution(tiles):
    return Hand(tiles).get_winning_tiles()


if __name__ == '__main__':
    tiles = "2p 2p 3p 3p 4p 4p 5p 5p 7m 7m 8m 8m 8m"
    # hand = Hand(tiles)
    # print(hand.tiles)
    # print(hand._all_tiles)
    # print(str(hand))
    # print(hand.check_seven_pair())
    # print(hand.get_winning_tiles())
    print(solution(tiles))
