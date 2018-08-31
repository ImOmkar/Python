n=int(input("enter the range: "))
n1=1
n2=1
for i in range(1,n+1):
    print(n1, end=' ')
    temp=n1
    n1=n2
    n2=temp+n2
