u=int(input("Enter MRP:\n"))

o=int(input("Enter offer no:\n"))

for i in range(1):
    if(o==1):
        print("MRP Price after applying Discount: ",u*0.75)
    elif(o==2):
        print("MRP price after applying Discount: ",u*0.6)
    elif(o==3):
        print("MRP price  after applying Discount: ",u*0.4)
    elif(o==4):
        print("MRP price after applying Discount: ",u*0.25)
    else:
        print("***GET LOST***")
