
from tkinter import *

#Intialize global variable
operator = ""

#functions
def set_A():
    global operator
    operator = "A"

def set_S():
    global operator
    operator = "S"


def set_M():
    global operator
    operator = "M"

def set_D():
    global operator
    operator = "D"

def evaluate():
    number1 = float(textbox1.get())
    number2= float(textbox2.get())
    textbox_ans.delete(0.0, END)#clear output text box
    if operator == "A":
        textbox_ans.insert(END, number1 +number2)
    elif operator == "S":
        textbox_ans.insert(END, number1-number2)
    elif operator == "M":
        textbox_ans.insert(END, number1 *number2)
    elif operator == "D":
        textbox_ans.insert(END, number1/number2)
        
#Build GUI
window = Tk()
window.title("Calculator")

#Create the labels
label1 = Label(window, text="Number1: ")
label1.grid(row=0, column=0)
label2 = Label(window, text="Number2:")
label2.grid(row=0, column=1)

#Create two text entry boxes
textbox1 = Entry(window, width=10)
textbox1.grid(row=1, column=0)
textbox2 = Entry(window, width=10)
textbox2.grid(row=1, column=1)

#Create the operator buttons
button_add = Button(window, width=10, text="+", command=set_A)
button_add.grid(row=2, column=0)

button_sub = Button(window, width=10, text="-", command=set_S)
button_sub.grid(row=2, column=1)

button_mul = Button(window, width=10, text="*", command=set_M)
button_mul.grid(row=3, column=0)

button_div = Button(window, width=10, text="/", command=set_D)
button_div.grid(row=3, column=1)

button_equal = Button(window, width=10, text="=", command=evaluate)
button_equal.grid(row=4, column=0)

#Create a text output box
textbox_ans = Text(window, width=10, height = 1)
textbox_ans.grid(row=4, column=1)

window.mainloop()
