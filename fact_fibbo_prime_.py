print("-------------- Facttorial program ---------------\n")

fact = 1
num = int(input("enter number: "))
for i in range(1, num+1):
    fact = fact * i
print(fact)


print("")
print("-------------fibonacci series upto 10--------\n")

a,b = 0, 1
for i in range(0, 10):
    print(a)
    a, b = b, a+b

print("")
print("-------------fibonacci by user input--------\n")
    
a, b = 0, 1
num = int(input("enter number: "))
for i in range(0, num):
    print(a)
    a, b = b, a+b
    

print("")
print("-------------prime number-----------\n")

start = 10
end = 25
for val in range(start, end+1):
    if val > 1:
        for n in range(2, val):
            if val % n == 0:
                print(val, "is not a prime number")
                break
        else:
            print(val, "is a prime number")

print("")
print("----------- * pattern in -----------------\n")

def pyrmd(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")

n = 5
pyrmd(n)

print("")
print("-----------* pattern opposite-------\n")

def pyrmdoppo(n):
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
        
n = 5
pyrmdoppo(n)

print("")
print("-----------* pattern opposite-------\n")

def tripymrd(n):
    k = 1*n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
        
n = 5
tripymrd(n)

print("----------------tkinter-----------\n")

from tkinter import Tk, Label, Button

class MyGui:
    def __init__(self, master):
        self.master = master
        master.title("My App")

        self.label = Label(master, text="Click")
        self.label.pack()

        self.button = Button(master, text="click me", command=self.greet)
        self.button.pack()

        self.button_close = Button(master, text="close me", command=quit)
        self.button.pack()

    def greet(self):
        print("greetings")
        
root = Tk()
my_gui = MyGui(root)
root.mainloop
