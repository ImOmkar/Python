user = int(input("enter range: \n"))
empty = []
for i in range(user
               ):
    numbers = int(input("enter elem"))
    empty.append(numbers)
print("greatest num is",max(empty))
print("smallest num is",min(empty))                  
