from unittest import TestCase
from arrays import stock_exchange


class Test(TestCase):
    def test_basic(self):
        self.assertEqual(0, stock_exchange.basic([]))
        self.assertEqual(7, stock_exchange.basic([7, 1, 5, 3, 6, 4]))
        self.assertEqual(4, stock_exchange.basic([1, 2, 3, 4, 5]))
        self.assertEqual(0, stock_exchange.basic([7, 6, 4, 3, 1]))
