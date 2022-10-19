from unittest import TestCase

from MatrixDeterminant import determinant


class Test(TestCase):
    def test_one_value(self):
        test, ans = ([[5]], 5)
        self.assertEqual(ans, determinant(test))

    def test_4_by_4(self):
        test, ans = ([[4, 6], [3, 8]], 14)
        self.assertEqual(ans, determinant(test))

    def test_3_by_3(self):
        test, ans = ([[2, 4, 2], [3, 1, 1], [1, 2, 0]], 10)
        self.assertEqual(ans, determinant(test))
