from tkinter import Tk, Label, Button

class MyGui:
    def __init__(self, master):
        self.master = master
        master.title("Welcome to GUI")

        self.button = Button(master, text="click me!", command=self.greet)
        self.button.pack()

        self.close_button = Button(master, text="close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("greetings")

root = Tk()
my_gui = MyGui(root)
root.mainloop()
