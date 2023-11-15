import unittest
from core import Memory
class CoreTests(unittest.TestCase):
    def setUp(self): self.m=Memory(':memory:'); self.addCleanup(self.m.close)
    def test_recent_order(self):
        for t in ['one','two','three']: self.m.append('a','user',t)
        self.assertEqual([r['text'] for r in self.m.recent('a',2)],['two','three'])
    def test_session_isolation(self):
        self.m.append('private','user','blue planet'); self.assertEqual(self.m.recall('other','blue'),[])
    def test_archive_retrieval(self):
        identifier=self.m.append('a','user','blue planet'); self.assertEqual(self.m.recall('a','planet')[0]['id'],identifier)
    def test_exclusion(self):
        i=self.m.append('a','user','blue planet'); self.assertEqual(self.m.recall('a','planet',[i]),[])
