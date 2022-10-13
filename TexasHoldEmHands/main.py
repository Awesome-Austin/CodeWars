from collections import namedtuple, defaultdict

CARDS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
Card = namedtuple('Card', ['card', 'face', 'suit', 'rank'])


def hand(hole_cards, community_cards):
    def _fill_in_best_hand(bh):
        if len(bh) < 5:
            remaining_options = [c for c in options if c not in bh]
            remaining_options.sort(key=lambda c: c.rank)
            return remaining_options[len(bh)-5:]
        else:
            return list()

    def _sort_and_clean_return(bh):
        fill_cards = _fill_in_best_hand(bh)
        fill_cards.sort(key=lambda c: c.rank, reverse=True)
        fill_cards = [c.face for c in fill_cards]

        hand_cards = list()
        for c in bh:
            if c.face not in hand_cards:
                hand_cards.append(c.face)

        return hand_cards + fill_cards

    def _find_max_straight(_ranks=None, _options=None):
        if _ranks is None:
            _ranks = ranks

        if _options is None:
            _options = options

        try:
            straight_start = max(
                [i for i in range(len(_ranks) - 4) if all([(x + 1) == y for x, y in zip(_ranks[:-1], _ranks[1:])][i:i + 4])]
            )
        except ValueError:
            return list()
        best_ranks = _ranks[straight_start:straight_start+5]
        straight = [c for c in _options if c.rank in best_ranks]
        return straight

    options = [Card(c, c[:-1], c[-1], CARDS[c[:-1]]) for c in hole_cards + community_cards]
    options.sort(key=lambda c: c.rank)

    suits = {c.suit: [o for o in options if o.suit == c.suit] for c in options}
    has_flush = any([len(cards) >= 5 for s, cards in suits.items()])

    of_a_kind = defaultdict(dict)
    for r, cards in [(c.rank, [o for o in options if o.rank == c.rank]) for c in options]:
        of_a_kind[len(cards)][r] = cards

    ranks = list({c.rank for c in options})
    ranks.sort()
    has_straight = any(
        [all([(x + 1) == y for x, y in zip(ranks[:-1], ranks[1:])][i:i + 4]) for i in range(len(ranks) - 4)]
    )

    if not has_straight and not has_flush and max(of_a_kind) == 1:
        return "nothing", _sort_and_clean_return([])

    if has_straight and has_flush:
        best_hand = [cards for s, cards in suits.items() if len(cards) >= 5][-1]
        best_hand = _find_max_straight(list({c.rank for c in best_hand}), best_hand)
        if best_hand:
            best_hand.sort(key=lambda c: c.rank, reverse=True)
            best_hand = best_hand[:5]
            return 'straight-flush',  _sort_and_clean_return(best_hand)

    if max(of_a_kind) >= 4:
        best_hand = of_a_kind[max(of_a_kind)][max(of_a_kind[max(of_a_kind)])]
        return "four-of-a-kind", _sort_and_clean_return(best_hand)

    if max(of_a_kind) == 3:
        if len(of_a_kind[3]) >= 2:
            _of_a_kind_list = list(of_a_kind[3])
            _of_a_kind_list.sort()
            best_hand = of_a_kind[3][_of_a_kind_list[-1]]
            best_hand += of_a_kind[3][_of_a_kind_list[-2]][-2:]
            return "full house", _sort_and_clean_return(best_hand)

        elif 2 in of_a_kind:
            best_hand = of_a_kind[3][max(of_a_kind[3])]
            best_hand += of_a_kind[2][max(of_a_kind[2])]
            return "full house", _sort_and_clean_return(best_hand)

    if has_flush:
        best_hand = [cards for s, cards in suits.items() if len(cards) >= 5][-1]
        best_hand.sort(key=lambda c: c.rank, reverse=True)
        best_hand = best_hand[:5]
        return "flush", _sort_and_clean_return(best_hand)

    if has_straight:
        best_hand = _find_max_straight()
        best_hand.sort(key=lambda c: c.rank, reverse=True)
        return "straight", _sort_and_clean_return(best_hand)

    if max(of_a_kind) == 3:
        best_hand = of_a_kind[3][max(of_a_kind[3])]
        return "three-of-a-kind", _sort_and_clean_return(best_hand)

    if max(of_a_kind) == 2:
        if len(of_a_kind[2]) >= 2:
            _of_a_kind_list = list(of_a_kind[2])
            _of_a_kind_list.sort()
            best_hand = of_a_kind[2][_of_a_kind_list[-1]]
            best_hand += of_a_kind[2][_of_a_kind_list[-2]][-2:]
            best_hand.sort(key=lambda c: c.rank, reverse=True)
            return "two pair", _sort_and_clean_return(best_hand)

        else:
            best_hand = of_a_kind[2][max(of_a_kind[2])]
            return "pair", _sort_and_clean_return(best_hand)
