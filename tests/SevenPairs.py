import unittest
from Majong import solution

TESTS = [
    ('1p 1p 3p 3p 4p 4p 5p 5p 6p 6p 7p 7p 9p', '9p'),
    ('2p 2p 3p 3p 4p 4p 5p 5p 7m 7m 8m 8m 8m', '2p 5p 7m 8m'),
    ("4s 4s 4s 1m 1m 1m 5m 6m 7m 8m 2z 2z 2z", '5m 8m'),
    ("2p 3p 4p 7p 7p 7p 1s 8s 8s 8s 1m 2m 3m", '1s'),
    ("6s 7s 8s 1m 1m 1m 7m 7m 7m 8m 9m 9m 9m", '6m 7m 8m 9m'),
    ("6p 6p 6p 3s 4s 5s 7s 8s 9s 9s 9s 2z 2z", '6s 9s 2z'),
    ("4p 5p 6p 6p 6p 7s 7s 7s 1m 1m 3z 3z 3z", '3p 6p 1m'),
    ("4p 4p 4p 4s 4s 4s 3m 3m 3m 4m 3z 3z 3z", '2m 4m 5m'),
    ("2s 3s 4s 4s 4s 2m 2m 2m 6m 6m 6m 7m 8m", '1s 4s 6m 9m'),
    ("1s 1s 1s 2s 3s 4s 5s 6s 7s 8s 9s 9s 9s", '1s 2s 3s 4s 5s 6s 7s 8s 9s'),
    ("1p 1p 1p 3p 6p 7p 8p 3s 4s 5s 2z 3z 4z", ''),
    ("1m 1m 2m 2m 3m 3m 4m 4m 5m 5m 8m 8m 8m", '1m 2m 4m 5m 8m'),
    ("1s 1s 1s 2s 3s 4s 5s 6s 6s 7s 8s 9s 9s", '1s 4s 7s 9s'),
    ("1m 2m 2m 2m 2m 3m 5m 5m 5m 6m 7m 8m 9m", '4m 6m 7m 9m'),
    # ("2p 2p 2p 3p 3p 3p 3p 4p 4p 4p 4p 5p 6p", '1p 2p 5p 6p 7p'),
    ("1p 1p 1p 3p 6p 7p 8p 3s 4s 5s 2m 3m 4m", '2p 3p'),
    ("9p 9p 9p 7p 2p 2p 2p 3s 4s 5s 2m 3m 4m", '7p 8p'),
    ("2p 2p 2p 9p 9p 9p 3s 4s 5s 6z 6z 7z 7z", '6z 7z'),
    # ("1s 1s 1s 1s 2p 2p 2p 3p 3p 3p 4p 4p 4p", ''),
    ("1p 1p 1p 1p 2p 2p 2p 2p 3p 3p 3p 3p 2z", '2z'),
    ("9p 9p 9p 9p 7p 7p 8p 8p 8p 8p 2s 3s 4s", '6p 7p'),
    ("4p 6p 7p 7p 7p 8p 8p 3m 3m 3m 5m 6m 7m", '5p'),
    ("2p 2p 2s 3s 3m 3m 3m 2z 2z 2z 3z 3z 3z", '1s 4s'),
    ("6s 6s 6s 2m 2m 2m 3m 4m 5m 6m 6m 7m 8m", '1m 3m 4m 6m 7m 9m'),
]


class MyTestCase(unittest.TestCase):
    def test_seven_pairs(self):
        for tiles, ans in TESTS:
            self.assertEqual(ans, solution(tiles))


if __name__ == '__main__':
    unittest.main()
