from unittest import TestCase
from arrays import comprefix


class Test(TestCase):
    def test_basic(self):
        self.assertEqual("", comprefix.basic([]))
        self.assertEqual('test', comprefix.basic(['test']))
        self.assertEqual('test', comprefix.basic(['test', 'testb']))
        self.assertEqual('test', comprefix.basic(['testa', 'test', 'testxxb']))
