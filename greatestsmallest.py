num=int(input("enter range: \n"))
empty=[]
for n in range(num):
    numbers=int(input("enter the numbers:" ))
    empty.append(numbers)
    
print("Greatest number is:",max(empty))
print("Smallest number is",min(empty))
