#WAP to take string as a input and check if the string is in uppercase or lowercase

user=input("Enter a string: \n")
if(user.isupper()):
    print("Entered string is in uppercase")
elif(user.islower()):
    print("Entered string is in lowercase")
else:
    print("**NOW GET LOST**")
