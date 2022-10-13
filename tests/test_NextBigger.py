from unittest import TestCase
from NextBiggest import next_bigger


class Test(TestCase):
    def test_next_bigger(self):
        tests = [
            (12, 21),
            (513, 531),
            (2017, 2071),
            (414, 441),
            (144, 414),
        ]
        for test, ans in tests:
            t = next_bigger(test)
            self.assertEqual(ans, t)

    def test_next_bigger_nil(self):
        tests = [
            (9, -1),
            (111, -1),
            (531, -1)
        ]
        for test, ans in tests:
            t = next_bigger(test)
            self.assertEqual(ans, t)

    def test_big_numbers(self):
        tests = [
            (123456789, 123456798),
            (1234567890, 1234567908),
            (9876543210, -1),
            (9999999999, -1),
        ]
        for test, ans in tests:
            # print(test)
            t = next_bigger(test)
            self.assertEqual(ans, t)
