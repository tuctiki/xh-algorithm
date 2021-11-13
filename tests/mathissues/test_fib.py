from unittest import TestCase
from mathissues import fib

# 1, 1, 2, 3, 5, 8, 13, 21, 34
# 0, 1, 2, 3, 4, 5, 6,  7,  8

class Test(TestCase):
    def test_basic(self):
        self.assertEqual(1, fib.fib(1))
        self.assertEqual(2, fib.fib(2))
        self.assertEqual(8, fib.fib(5))
        self.assertEqual(34, fib.fib(8))
        