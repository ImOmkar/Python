user_input=int(input("enter the range: \n"))
empty=list()

for i in range(user_input):
    user_finput=float(input())
    empty.append(user_finput)

total=0
for i in empty:
    total=total+i
    
round(total, 2)
print("Total: \n",total)
mean=total/user_input
round(mean, 2)
print("Mean: \n",mean)
percentage=mean/total*100
round(percentage, 2)
print("Percentage: \n",percentage)
