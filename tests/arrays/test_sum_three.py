from unittest import TestCase
from arrays import sum_three


class Test(TestCase):
    def test_basic(self):
        self.assertEqual([], sum_three.basic([], 1))
        self.assertEqual([], sum_three.basic([2, 3], 1))
        self.assertEqual([1, 2, 4], sum_three.basic([9, 2, 3, 4, 1], 7))
        self.assertEqual([3, 4, 9], sum_three.basic([9, 2, 3, 4, 1], 16))
        self.assertEqual([], sum_three.basic([2, 4, 6, 8, 10], 101))
        self.assertEqual([], sum_three.basic([100, 101, 98, 33, 78], 1))