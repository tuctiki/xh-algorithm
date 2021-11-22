from unittest import TestCase
from arrays import sum_two


class Test(TestCase):
    def test_basic(self):
        self.assertEqual([], sum_two.basic([], 1))
        self.assertEqual([], sum_two.basic([2, 3], 1))
        self.assertEqual([2, 3], sum_two.basic([1, 2, 3, 4, 9], 7))
