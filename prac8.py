L = ['mango','grapes','mango','apple','grapes','grapes']
word_list = []
count_list = []
L2 = list(set(L))
L2.sort()
for each in L2:
    word_list.append(each)
    count_list.append(L.count(each))
print("word list",word_list)
print("count list",count_list)
