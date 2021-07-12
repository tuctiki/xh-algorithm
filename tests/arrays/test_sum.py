from unittest import TestCase
from arrays import sum


class Test(TestCase):
    def test_basic(self):
        self.assertEqual([], sum.basic([], 1))
        self.assertEqual([], sum.basic([2, 3], 1))
        self.assertEqual([2, 3], sum.basic([1, 2, 3, 4, 9], 7))
