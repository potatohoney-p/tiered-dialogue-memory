import json
from core import Memory
from features import context
with open('examples/input.json') as stream: data=json.load(stream)
memory=Memory(':memory:')
try:
    for text in data['turns']: memory.append('demo','user',text)
    print(json.dumps(context(memory,'demo',data['query'],12,2),sort_keys=True))
finally: memory.close()
