## this task ask the user to type a word and return its reverse 
from tkinter import *
def simple_calculator():
    global v
    value = v.get()
    operand1 = int(e1.get())
    operand2 = int(e2.get())
    if value == 1:
        result = operand1 - operand2
    elif value == 2:
        result = operand1 + operand2
    l2 = Label(window , text=str(result ))
    l2.grid(row=2, column=1)
window = Tk()
window.geometry("500x200+700+200")
window.resizable(False,False)

v = IntVar()
l1 = Label(window, text= "Enter value of N")
e1 = Entry(window)
l2 = Label(window, text= "Enter value of M")
e2 = Entry(window)
btn = Button(window , text="validate"  , command=simple_calculator )

r1 = Radiobutton(window , text="sub" , variable=v , value=1,fg = "orange" , font = 30)
r2 = Radiobutton(window , text="sum" , variable=v , value=2,fg = "orange" , font= 30)

l1.grid(row=0 , column=0)
e1.grid(row=0,column=1)
l2.grid(row=1 , column=0)
e2.grid(row=1,column=1)
btn.grid(row=3 , column=1)
r1.place(x = 0 , y = 50)
r2.place(x = 0 , y = 70)

window.mainloop()
