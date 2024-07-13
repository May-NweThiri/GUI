#Match or Unmarch

from tkinter import *

def compare_numbers():
    num1 = entry1.get()
    num2 = entry2.get()
    
    result = ""
    if num1 == num2:
        result = "Match"
    else:
        result = "Unmatch"
    
    my_label.config(text=result)

# Create the main tkinter window
window = Tk()
window.title("My Application")

# Add labels and entry widgets for input
label1 = Label(window, text="Enter Number 1:")
label1.grid(row=0, column=0)
entry1 = Entry(window)
entry1.grid(row=0, column=1)

label2 = Label(window, text="Enter Number 2:")
label2.grid(row=1, column=0)
entry2 = Entry(window)
entry2.grid(row=1, column=1)

# Add an empty tkinter label widget for displaying the result
my_label = Label(window, width=25, height=1, text="")
my_label.grid(row=2, column=0, columnspan=2)

# add button
my_button = Button(window, text="Submit", width=10, command=compare_numbers)
my_button.grid(row=3, column=0, columnspan=2)

window.mainloop()
