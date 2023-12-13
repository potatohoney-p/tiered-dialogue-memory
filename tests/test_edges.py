import unittest
from core import Memory
from features import context
class EdgeTests(unittest.TestCase):
    def test_zero_budget(self):
        m=Memory(':memory:'); self.addCleanup(m.close); m.append('a','user','hello')
        self.assertEqual(context(m,'a','hello',0)['turns'],[])
    def test_role_validation(self):
        m=Memory(':memory:'); self.addCleanup(m.close)
        with self.assertRaises(ValueError): m.append('a','system','hidden')
    def test_no_truncation(self):
        m=Memory(':memory:'); self.addCleanup(m.close); m.append('a','user','one two three')
        self.assertEqual(context(m,'a','one',2)['turns'],[])
