d={'Java':6,'perl':2,'C++':5,'Python':8,'AngularJS':3,'Ruby':9,'Bootstrap':1}
op=sorted(d, key=d.get, reverse=True)
for each in op[:3]:
    print(each, end=' ')
    
#max_keys={k for k, val in d.items() if val==max(d.values())}
#print(max_key)
