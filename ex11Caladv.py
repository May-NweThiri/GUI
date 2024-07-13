#End of chapter task(3)
from tkinter import *

def keyboard1():
    label.config(text = "1")
def keyboard2():
    label.config(text = "2")
def keyboard3():
    label.config(text = "3")
def keyboard4():
    label.config(text = "4")
def keyboard5():
    label.config(text = "5")
def keyboard6():
    label.config(text = "6")
def keyboard7():
    label.config(text = "7")
def keyboard8():
    label.config(text = "8")
def keyboard9():
    label.config(text = "9")



#Build the GUI
window = Tk()
window.title("MY APP")

#Create the label
label = Label(window, text=  "")
label.grid(row=0, column=3)

#Create the button
button1= Button(window, text="1", command= keyboard1)
button1.grid(row=1, column=2)

button2= Button(window, text="2", command= keyboard2)
button2.grid(row=1, column=3)

button3= Button(window, text="3", command= keyboard3)
button3.grid(row=1, column=4)

button4= Button(window, text="4", command= keyboard4)
button4.grid(row=2, column=2)

button5= Button(window, text="5", command= keyboard5)
button5.grid(row=2, column=3)

button6= Button(window, text="6", command= keyboard6)
button6.grid(row=2, column=4)

button7= Button(window, text="7", command= keyboard7)
button7.grid(row=3, column=2)

button8= Button(window, text="8", command= keyboard8)
button8.grid(row=3, column=3)

button9= Button(window, text="9", command= keyboard9)
button9.grid(row=3, column=4)

window.mainloop()



