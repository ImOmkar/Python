L=['Mango','Grapes','Mango','Apple','Grapes','Grapes']
word_list=[]
count_list=[]
L2=list(set(L))
L2.sort()
for each in L2:
    #if each not in word_list:
        word_list.append(each)
        #word_list.sort()
        count_list.append(L.count(each))
        #count_list.sort()
print("word_list =",word_list)
print("count_list =",count_list)
 
    
    
