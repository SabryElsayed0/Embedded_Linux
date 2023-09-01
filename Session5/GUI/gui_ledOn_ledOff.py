## this task ask the user to type a word and return its reverse 
from tkinter import *
def led_on():
    my_canavs.itemconfig(my_oval , fill="red")
    l1.config(text="led on")
def led_off():
    my_canavs.itemconfig(my_oval , fill="white")
    l1.config(text="led off")
    
window = Tk()
window.geometry("500x300+700+200")
window.resizable(False,False)


l1 = Label(window, text= "led off")
btn1 = Button(window , text="Led On"  , command=led_on )
btn2 = Button(window , text="Led Off"  , command=led_off )
my_canavs = Canvas(width=100 , height=100)
my_canavs.pack()
my_oval = Canvas.create_oval(my_canavs,100,100,50 ,50,fill="white" , outline="yellow")


l1.place(x = 250 , y = 150)
btn1.place(x = 240 , y = 180)
btn2.place(x = 240 , y = 210)


window.mainloop()
