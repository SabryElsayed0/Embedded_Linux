import math
from tkinter import *

def calc_factorial():
    number = int(e1.get())
    result = math.factorial(number)
    l2 = Label(window , text=f"factorial of {number} is  " + str(result ))
    l2.grid(row=1, column=1)
window = Tk()
window.geometry("500x200+700+200")
window.resizable(False,False)

l1 = Label(window, text= "Enter value of interger N")
e1 = Entry(window)
btn = Button(window , text="validate"  , command=calc_factorial )

l1.grid(row=0 , column=0)
e1.grid(row=0,column=1)
btn.grid(row=2 , column=1)


window.mainloop()
