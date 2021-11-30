from unittest import TestCase
from arrays import z_convert


class Test(TestCase):
    def test_opt(self):
        z_convert.opt("LEETCODEISHIRING", 4)