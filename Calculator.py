#step 1: Importing
from tkinter import *

#step 2: GUI interaction
window = Tk()
window.geometry('500x500')

#step 3: adding inputs
#entrybox
e= Entry(window , width=60 , borderwidth=6)
e.place(x=0 , y=0)

#buttons
def click(num):
    result= e.get()
    e.delete(0 ,END)
    e.insert(0 , str(result) + str(num))

b = Button(window , text='1' , width=12 , command= lambda:click(1) , bg = "lightgray")
b.place(x=10 ,y=60)

b = Button(window , text='2' , width=12, command= lambda:click(2) , bg = "lightgray")
b.place(x=90 ,y=60)

b = Button(window , text='3' , width=12, command= lambda :click(3) , bg = "lightgray")
b.place(x=180 ,y=60)

b = Button(window , text='4' , width=12, command= lambda :click(4) , bg = "lightgray")
b.place(x=10 ,y=120)

b = Button(window , text='5' , width=12, command= lambda :click(5) , bg = "lightgray")
b.place(x=90 ,y=120)

b = Button(window , text='6' , width=12, command= lambda :click(6) , bg = "lightgray")
b.place(x=180 ,y=120)

b = Button(window , text='7' , width=12, command= lambda :click(7) , bg = "lightgray")
b.place(x=10 ,y=180)

b = Button(window , text='8' , width=12, command= lambda :click(8) , bg = "lightgray")
b.place(x=90 ,y=180)

b = Button(window , text='9' , width=12, command= lambda :click(9) , bg = "lightgray")
b.place(x=180 ,y=180)

b = Button(window , text='0' , width=12, command= lambda :click(0) , bg = "lightgray")
b.place(x=90 ,y=240)

#operators
def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i= int(n1)
    e.delete(0, END)

b = Button(window , text='+' , width=12 , command= add , bg = "darkgray")
b.place(x=270 ,y=60)

def sub():
    n1 = e.get()
    global math
    math = "substraction"
    global i
    i= int(n1)
    e.delete(0, END)

b = Button(window , text='-' , width=12 , command= sub , bg = "darkgray")
b.place(x=270 ,y=120)

def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i= int(n1)
    e.delete(0, END)

b = Button(window , text='*' , width=12 , command= mult , bg = "darkgray")
b.place(x=270 ,y=180)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i= int(n1)
    e.delete(0, END)

b = Button(window , text='/' , width=12 , command= div , bg = "darkgray")
b.place(x=270 ,y=240)

def clear():
    e.delete(0,END)


b = Button(window , text='clear' , width=12 , command= clear , bg = "orange")
b.place(x=10 ,y=240)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i +int(n2))
    elif math == "substraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))


b = Button(window , text='=' , width=12 , command= equal , bg = "gray")
b.place(x=180 ,y=240)

#step 4: mainloop
mainloop()