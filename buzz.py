s=input("Enter a string: ")
o=['buzz' if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U' else x for x in s]
print(o)
