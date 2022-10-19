from unittest import TestCase

from LastDigitOfAHugeNumber import last_digit


class TestMain(TestCase):
    def test_empty_list(self):
        test, ans = ([], 1)
        self.assertEqual(ans, last_digit(test))

    def test_two_zeros(self):
        test, ans = ([0, 0], 1)
        self.assertEqual(ans, last_digit(test))

    def test_three_zeros(self):
        test, ans = ([0, 0, 0], 0)
        self.assertEqual(ans, last_digit(test))

    def test_two(self):
        test, ans = ([1, 2], 1)
        self.assertEqual(ans, last_digit(test))

    def test_three_1(self):
        test, ans = ([3, 4, 5], 1)
        self.assertEqual(ans, last_digit(test))

    def test_three_2(self):
        test, ans = ([4, 3, 6], 4)
        self.assertEqual(ans, last_digit(test))

    def test_three_3(self):
        test, ans = ([7, 6, 21], 1)
        self.assertEqual(ans, last_digit(test))

    def test_three_4(self):
        test, ans = ([12, 30, 21], 6)
        self.assertEqual(ans, last_digit(test))

    def test_four(self):
        test, ans = ([2, 2, 2, 0], 4)
        self.assertEqual(ans, last_digit(test))

    def test_large_1(self):
        test, ans = ([937640, 767456, 981242], 0)
        self.assertEqual(ans, last_digit(test))

    def test_large_2(self):
        test, ans = ([123232, 694022, 140249], 6)
        self.assertEqual(ans, last_digit(test))

    def test_large_3(self):
        test, ans = ([499942, 898102, 846073], 6)
        self.assertEqual(ans, last_digit(test))
