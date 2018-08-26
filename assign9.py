#WAP to count the total number of vowel in a string
user=input("Enter: \n")
vowels=0
user=user.lower()
for i in user:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels+=1

#vowels+=user.count('a')
#vowels+=user.count('e')
#vowels+=user.count('i')
#vowels+=user.count('o')
#vowels+=user.count('u')
print("We found",vowels,"vowels")

