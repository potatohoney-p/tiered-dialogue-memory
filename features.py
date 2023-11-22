def context(memory,session,query,max_words=40,recent_count=3):
    if max_words<0: raise ValueError('Negative word budget')
    recent=memory.recent(session,recent_count)
    archive=memory.recall(session,query,[r['id'] for r in recent])
    selected=[]; used=0
    for tier,rows in [('recent',list(reversed(recent))),('archive',archive)]:
        for row in rows:
            cost=len(row['text'].split())
            if used+cost<=max_words:
                selected.append({'id':row['id'],'role':row['role'],'text':row['text'],'tier':tier}); used+=cost
    return {'turns':selected,'words':used,'budget':max_words}
