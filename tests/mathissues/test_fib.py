from unittest import TestCase
from mathissues import fib

class Test(TestCase):
    def test_basic(self):
        self.assertEqual(1, fib.fib(1))
        self.assertEqual(3, fib.fib(2))
        self.assertEqual(8, fib.fib(5))
        self.assertEqual(34, fib.fib(7))