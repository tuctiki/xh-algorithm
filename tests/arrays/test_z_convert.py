from unittest import TestCase
from arrays import z_convert


class Test(TestCase):
    def test_basic(self):
        z_convert.basic("LEETCODEISHIRING", 4)