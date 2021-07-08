from unittest import TestCase
from arrays import shift_elements


class Test(TestCase):
    def test_basic(self):
        self.assertEqual([], shift_elements.basic([], 1))
        self.assertEqual([1, 2, 3, 4, 5], shift_elements.basic([1, 2, 3, 4, 5], 0))
        self.assertEqual([5, 1, 2, 3, 4], shift_elements.basic([1, 2, 3, 4, 5], 1))
        self.assertEqual([3, 4, 5, 1, 2], shift_elements.basic([1, 2, 3, 4, 5], 3))
        self.assertEqual([1, 2, 3, 4, 5], shift_elements.basic([1, 2, 3, 4, 5], 5))
