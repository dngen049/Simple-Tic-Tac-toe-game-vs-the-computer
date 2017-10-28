from tkinter import *
import tkinter.messagebox
import random

root = Tk()
root.title("TIC TAC TOE")
root.geometry('400x100')

button1 = Button(root, text="   ", width=10, command=lambda:player(button1))
button1.grid(row=1, column=1)
button2 = Button(root, text=" ", width=10, command=lambda:player(button2))
button2.grid(row=1, column=2)
button3 = Button(root, text="  ", width=10, command=lambda:player(button3))
button3.grid(row=1, column=3)

button4 = Button(root, text="   ", width=10, command=lambda:player(button4))
button4.grid(row=2, column=1)
button5 = Button(root, text=" ", width=10, command=lambda:player(button5))
button5.grid(row=2, column=2)
button6 = Button(root, text="  ", width=10, command=lambda:player(button6))
button6.grid(row=2, column=3)

button7 = Button(root, text="   ", width=10,command=lambda:player(button7))
button7.grid(row=3, column=1)
button8 = Button(root, text=" ", width=10, command=lambda:player(button8))
button8.grid(row=3, column=2)
button9 = Button(root, text="  ", width=10, command=lambda:player(button9))
button9.grid(row=3, column=3)

Button= [button1, button2, button3, button4, button5, button6, button7, button8, button9]

click = True
print(Button)
def player(bout):
    bout["text"]= "X"
    Button.remove(bout)
    
    button_2 =random.choice(Button)
    button_2['text'] = "O"
    Button.remove(button_2)
