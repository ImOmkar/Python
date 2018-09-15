def student_info():
    global percentage #for the access in grade function
    total=0
    std_nm=input("Name of Student: ")
    std_rno=int(input("Student's roll no: "))
    noof_sub=int(input("No of subjects: "))
    for i in range(noof_sub):
        sub=int(input(''))
        total  += sub
        percentage=total/noof_sub
    print("Marks Total is: ",total)
    print("Your Percentage is",percentage,"%")
    

def grade():
    print("Your Grade is")
    if percentage >= 60:
        print("A")
    elif percentage >= 40 :
        print("B")
    else:
        print("*FAIL*")
        
student_info()
grade()
