import unittest
from core import Memory
from features import context
class FeatureTests(unittest.TestCase):
    def setUp(self):
        self.m=Memory(':memory:'); self.addCleanup(self.m.close)
        for t in ['blue planet','new subject','latest turn']: self.m.append('a','user',t)
    def test_recent_then_archive(self):
        c=context(self.m,'a','blue',6,1)
        self.assertEqual([r['tier'] for r in c['turns']],['recent','archive'])
        self.assertEqual(c['words'],4)
    def test_budget(self): self.assertEqual(context(self.m,'a','blue',2,1)['words'],2)
    def test_no_duplicates(self):
        c=context(self.m,'a','turn',20,3); ids=[r['id'] for r in c['turns']]; self.assertEqual(len(ids),len(set(ids)))
