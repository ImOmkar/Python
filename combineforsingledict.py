d1={'Python':3, 'Java':6, 'Perl':2}
d2={'C++':5, 'AngularJS':3, 'Python':5}
d3={}
for k,v in d2.items():
    d3[k]=v

for k,v in d1.items():
    if k in d2:
        d3[k]=d3[k]+v
    else:
        d3[k]=v
print(d3)

'''d3=d1.copy()
d3(d2)
print(d3)
for k in d1:
    if k in d2:
        d1[k]+=d2[k]
        d3=d1.copy() 
        #d3=d2.copy()
        print(d3)'''
    
        
        
