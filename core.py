import re
import sqlite3
class Memory:
    def __init__(self,path):
        self.db=sqlite3.connect(path)
        self.db.execute('CREATE TABLE IF NOT EXISTS turns (id INTEGER PRIMARY KEY, session TEXT, role TEXT, text TEXT)')
    def close(self): self.db.close()
    def append(self,session,role,text):
        if not session or role not in ('user','assistant') or not isinstance(text,str) or not text.strip(): raise ValueError('Invalid conversation turn')
        with self.db:
            cursor=self.db.execute('INSERT INTO turns(session,role,text) VALUES (?,?,?)',(session,role,text))
        return cursor.lastrowid
    def recent(self,session,count=3):
        if count<0: raise ValueError('Negative window size')
        rows=self.db.execute('SELECT id,role,text FROM turns WHERE session=? ORDER BY id DESC LIMIT ?',(session,count)).fetchall()
        return [{'id':i,'role':r,'text':t} for i,r,t in reversed(rows)]
    def recall(self,session,query,exclude=(),limit=3):
        if limit<0: raise ValueError('Negative recall limit')
        terms=set(re.findall(r'[a-z]+',query.lower())); result=[]
        for identifier,role,text in self.db.execute('SELECT id,role,text FROM turns WHERE session=? ORDER BY id',(session,)):
            score=len(terms & set(re.findall(r'[a-z]+',text.lower())))
            if score and identifier not in exclude: result.append({'id':identifier,'role':role,'text':text,'score':score})
        return sorted(result,key=lambda r:(-r['score'],-r['id']))[:limit]
