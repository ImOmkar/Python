#WAP to take name and the contact number from user and check whether it is correct value or not.



name=input("Enter your name: \n")

number=input("Enter your mobile number: \n")

if (len(name)>2 and len(number)==10):
    print("correct details")
else:
    print("wrong details")


    
