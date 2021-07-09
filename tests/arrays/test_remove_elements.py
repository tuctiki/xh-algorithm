from unittest import TestCase
from arrays import remove_elements


class Test(TestCase):
    def test_basic(self):
        self.assertEqual(3, remove_elements.basic([3, 2, 2, 3, 2, 3], 2))
        self.assertEqual(0, remove_elements.basic([], 2))
        self.assertEqual(1, remove_elements.basic([3], 2))
        self.assertEqual(0, remove_elements.basic([2, 2, 2, 2], 2))

    def test_sored(self):
        self.assertEqual(4, remove_elements.basic([1, 2, 2, 4, 4, 5], 2))
        self.assertEqual(0, remove_elements.basic([], 2))
        self.assertEqual(1, remove_elements.basic([3], 2))
        self.assertEqual(0, remove_elements.basic([2, 2, 2, 2], 2))

