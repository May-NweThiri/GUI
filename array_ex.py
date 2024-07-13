#Ch 11 Demo Task Integer Array

from tkinter import *
task = [None] *4 #global variable
#Functions
def input_data():
    #collect values from Entry boxes
    data_item = int(tbox1.get())
    index = int(tbox2.get())
    #insert new value into array
    task[index] = data_item

def output_data():
    #collect index required
    index = int(tbox3.get())
    #clear output text box and display value
    tbox4.delete(0, END)
    tbox4.insert(END, task[index])

    

window =Tk()
window.title("My Application")
bg_colour = "black"

#create two frames
input_frame = Frame(window, bg = bg_colour)
input_frame.grid(row=0, column=0)
output_frame = Frame(window, bg=bg_colour)
output_frame.grid(row=0, column=1)

#Create the labels
input_label1 = Label(input_frame, text= "Data Item to Add:", bg=bg_colour)
input_label1.grid(row=1, column=0, sticky = W)
input_label2 = Label(input_frame, text= "Index to be Used: ", bg= bg_colour)
input_label2.grid(row=2, column=0, sticky = W)

output_label1 = Label(output_frame, text= "Index to Display: ", bg=bg_colour)
output_label1.grid(row=1, column=0, sticky= W)
output_label2 = Label(output_frame, text= "Value in Index: ", bg= bg_colour)
output_label2.grid(row=2, column=0, sticky = W)

#Create the buttons
input_button = Button(input_frame, text= "Input", command=input_data, width=20)
input_button.grid(row=0, column=0, columnspan=2)
output_button = Button(output_frame, text="Output", command= output_data, width=20)
output_button.grid(row=0, column=0, columnspan= 2)

#Create the textboxes
tbox1 = Entry(input_frame, width=10)
tbox1.grid(row=1, column=1)
tbox2 = Entry(input_frame, width=10)
tbox2.grid(row=2, column=1)

tbox3 = Entry(output_frame, width=10)
tbox3.grid(row=1, column=1)
tbox4= Entry(output_frame, width=10)
tbox4.grid(row=2, column=1)

window.mainloop
