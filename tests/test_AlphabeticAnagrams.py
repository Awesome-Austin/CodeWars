from AlphabeticAnagrams.main import listPosition
from unittest import TestCase


class Test(TestCase):
    def test_list_position_ABAB(self):
        test, ans = 'ABAB', 2
        self.assertEqual(ans, listPosition(test))

    def test_list_position_AAAB(self):
        test, ans = 'AAAB', 1
        self.assertEqual(ans, listPosition(test))

    def test_list_position_BAAA(self):
        test, ans = 'BAAA', 4
        self.assertEqual(ans, listPosition(test))

    def test_list_position_QUESTION(self):
        test, ans = 'QUESTION', 24572
        self.assertEqual(ans, listPosition(test))

    def test_list_position_BOOKKEEPER(self):
        test, ans = 'BOOKKEEPER', 10743
        self.assertEqual(ans, listPosition(test))
