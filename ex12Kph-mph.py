from tkinter import *
#Function

def to_kph():
    mph= float(mph_textbox.get())
    kph= mph *1.60934
    kph_textbox.delete(0, END)
    kph_textbox.insert(END, kph)

def to_mph():
    kph= float(kph_textbox.get())
    mph= kph/1.60934
    mph_textbox.delete(0, END)
    mph_textbox.insert(END, mph)


#Build the GUI
window = Tk()
window.title("Speed Converter")

#Add two tkinter label widgets
label1 = Label(window, width=5, heigh=1, text="mph")
label1.grid(row=0, column=0)

label2 = Label(window, width=5, height=1, text="kph")
label2.grid(row=0, column= 2)

#Add two textboxes
mph_textbox= Entry(window, width=10)
mph_textbox.grid(row=1, column=0)

kph_textbox= Entry(window, width=10)
kph_textbox.grid(row=1, column=2)

#Add a frame
button_frame= Frame(window, height=4, width=4)
button_frame.grid(row=1, column=1)

#Add two tkinter button widgets
button1 = Button(button_frame, text = "-->", width=4, command=to_kph)
button1.grid(row=0, column=0)

button2= Button(button_frame, text= "<--", width=4, command= to_mph)
button2.grid(row=1, column=0)

window.mainloop()
