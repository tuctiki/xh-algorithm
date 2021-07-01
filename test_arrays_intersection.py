from unittest import TestCase
import arrays_intersection


class Test(TestCase):
    def test_basic(self):
        self.assertEqual([], arrays_intersection.basic([], []))
        self.assertEqual([2, 2], arrays_intersection.basic([1, 2, 2, 1], [2, 2, 2]))
        self.assertEqual([4, 9], arrays_intersection.basic([4, 9, 5], [9, 4, 9, 8, 4]))

    def test_by_dict(self):
        self.assertEqual([], arrays_intersection.by_dict([], []))
        self.assertEqual([2, 2], arrays_intersection.by_dict([1, 2, 2, 1], [2, 2, 2]))
        self.assertEqual([4, 9], arrays_intersection.by_dict([4, 9, 5], [9, 4, 9, 8, 4]))

    def test_for_sorted(self):
        self.assertEqual([], arrays_intersection.for_sored([], []))
        self.assertEqual([1, 2, 3, 4], arrays_intersection.for_sored([1, 2, 3, 4, 4, 13], [1, 2, 3, 4, 9, 10]))
        self.assertEqual([4, 9], arrays_intersection.for_sored([4, 5, 9], [4, 4, 8, 9, 9]))
