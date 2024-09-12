data = {'record1': {'eid':1,'ename':'swar','age':30,'salary':1000},
        'record2': {'eid':2,'ename':'subho','age':32,'salary':2000}}

for record in data:
    for cols in data[record]:
        print(data[record][cols])  