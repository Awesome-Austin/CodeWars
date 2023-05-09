from unittest import TestCase

from AlphabeticAnagrams import listPosition

class Test(TestCase):
    def test_list_position_ABAB(self):
        test, ans = 'ABAB', 2
        result = listPosition(test)
        self.assertEqual(ans, result)

    def test_list_position_AAAB(self):
        test, ans = 'AAAB', 1
        result = listPosition(test)
        self.assertEqual(ans, result)

    def test_list_position_BAAA(self):
        test, ans = 'BAAA', 4
        result = listPosition(test)
        self.assertEqual(ans, result)

    def test_list_position_QUESTION(self):
        test, ans = 'QUESTION', 24572
        result = listPosition(test)
        self.assertEqual(ans, result)

    def test_list_position_BOOKKEEPER(self):
        test, ans = 'BOOKKEEPER', 10743
        result = listPosition(test)
        self.assertEqual(ans, result)
