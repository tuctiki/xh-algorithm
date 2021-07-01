from unittest import TestCase
from arrays import intersection


class Test(TestCase):
    def test_basic(self):
        self.assertEqual([], intersection.basic([], []))
        self.assertEqual([2, 2], intersection.basic([1, 2, 2, 1], [2, 2, 2]))
        self.assertEqual([4, 9], intersection.basic([4, 9, 5], [9, 4, 9, 8, 4]))

    def test_by_dict(self):
        self.assertEqual([], intersection.by_dict([], []))
        self.assertEqual([2, 2], intersection.by_dict([1, 2, 2, 1], [2, 2, 2]))
        self.assertEqual([4, 9], intersection.by_dict([4, 9, 5], [9, 4, 9, 8, 4]))

    def test_for_sorted(self):
        self.assertEqual([], intersection.for_sored([], []))
        self.assertEqual([1, 2, 3, 4], intersection.for_sored([1, 2, 3, 4, 4, 13], [1, 2, 3, 4, 9, 10]))
        self.assertEqual([4, 9], intersection.for_sored([4, 5, 9], [4, 4, 8, 9, 9]))

