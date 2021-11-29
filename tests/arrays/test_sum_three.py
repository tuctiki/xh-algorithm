from unittest import TestCase
from arrays import sum_three


class Test(TestCase):
    def test_basic(self):
        self.assertEqual([], sum_three.basic([], 1))
        self.assertEqual([], sum_three.basic([2, 3], 1))
        self.assertEqual([1, 2, 4], sum_three.basic([1, 2, 3, 4, 9], 7))