import unittest

from function1.func1 import sum_numbers


class TestSumNumbers(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(1, 2, 3), 6)
        self.assertTrue(sum_numbers(0, 0, 1))
        self.assertIs(sum_numbers(5, 6, 7), 18)
        # self.assertRaises(TypeError, sum_numbers('a', 5, 7))
