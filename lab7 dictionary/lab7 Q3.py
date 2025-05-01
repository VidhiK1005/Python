d = {
    1: {'dept no': 12, 'salary': 12000},
    4: {'dept no': 3, 'salary': 15000},
    6: {'dept no': 9, 'salary': 10000},
    3: {'dept no': 12, 'salary': 15000},
    8: {'dept no': 9, 'salary': 12000},
    7: {'dept no': 3, 'salary': 18000},
    5: {'dept no': 3, 'salary': 19000}
}

sal={}
for i in d.values():
    if i['dept no'] not in sal:
        sal[i['dept no']]=[]
    sal[i['dept no']].append(i['salary'])

r={}
for k,v in sal.items():
    r[k]={'min salary':min(v),'max salary':max(v)}

print(r)
