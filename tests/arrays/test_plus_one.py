from unittest import TestCase
from arrays import plus_one


class Test(TestCase):
    def test_basic(self):
        self.assertEqual([], plus_one.basic([]))
        self.assertEqual([1, 2, 3], plus_one.basic([1, 2, 2]))
        self.assertEqual([1, 0, 0, 0], plus_one.basic([9, 9, 9]))
