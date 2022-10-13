from unittest import TestCase
from PattonsDecoder import decode, encode


class Test(TestCase):
    def test_decode(self):
        tests = [
            (encode("Hello World!"), "Hello World!"),
            ("atC5kcOuKAr!", "Hello World!")
        ]
        for test, answer in tests:
            test.assert_equals(decode(test), answer)
