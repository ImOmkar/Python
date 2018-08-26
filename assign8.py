#WAP to check whether the string is starting with vowel or not.



user=input("Enter a string: \n")

if(user.startswith('a') or user.startswith('e') or user.startswith('i') or user.startswith('o') or user.startswith('u') or user.startswith('A') or user.startswith('E') or user.startswith('I') or user.startswith('O') or user.startswith('U')):
    print("String is starting with vowel")
else:
    print("String is not starting with vowel")
