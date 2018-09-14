sub_list=['Maths','Phy','Chem','Java','Mech']
mark_list=[78,74,68,77,67]
empty={}
for i in range(len(sub_list)):
    empty[sub_list[i]] = mark_list[i]
print(empty)

