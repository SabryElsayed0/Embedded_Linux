from tkinter import *
def display_reverse_word():
    data = e1.get()[::-1]
    print(data)
    l2 = Label(window , text=data )
    l2.grid(row=1, column=1)
window = Tk()
window.geometry("500x100+700+200")
window.resizable(False,False)

l1 = Label(window, text= "Enter a word")
e1 = Entry(window)

l1.grid(row=0 , column=0)
e1.grid(row=0,column=1)

btn = Button(window , text="validate"  , command=display_reverse_word )
btn.grid(row=2 , column=1)

window.mainloop()
