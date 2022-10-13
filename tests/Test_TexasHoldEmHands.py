from unittest import TestCase
from TexasHoldEmHands.main import hand


class MyTestCase(TestCase):
    def test_something(self):
        tests = [
            # ((["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]), ("nothing", ["A", "K", "Q", "J", "9"])),
            # ((["K♠", "Q♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]), ("pair", ["Q", "K", "J", "9"])),
            # ((["K♠", "J♦"], ["J♣", "K♥", "9♥", "2♥", "3♦"]), ("two pair", ["K", "J", "9"])),
            # ((["4♠", "9♦"], ["J♣", "Q♥", "Q♠", "2♥", "Q♦"]), ("three-of-a-kind", ["Q", "J", "9"])),
            # ((["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"]), ("straight", ["K", "Q", "J", "10", "9"])),
            # ((["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]), ("flush", ["Q", "J", "10", "5", "3"])),
            # ((["A♠", "A♦"], ["K♣", "K♥", "A♥", "Q♥", "3♦"]), ("full house", ["A", "K"])),
            # ((["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"]), ("four-of-a-kind", ["2", "3"])),
            # ((["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]), ("straight-flush", ["J", "10", "9", "8", "7"])),
            # ((['4♠', '8♠'], ['10♠', '4♥', '4♣', '9♥', '4♦']), ('four-of-a-kind', ['4', '10'])),
            ((['10♦', '6♥'], ['8♦', '9♦', 'Q♦', 'J♦', '7♠']), ('straight-flush', ['Q', 'J', '10', '9', '8']))
        ]

        for test in tests:
            deal, solution = test
            self.assertEqual(solution, hand(*deal), "Incorrect solution for the following deal: " + str(deal))
