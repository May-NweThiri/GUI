from tkinter import *

def is_leap_year():
    # Get the year entered by the user
    year = int(entry_year.get())

    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = "Leap year"
    else:
        result = "Not a leap year"

    # Update the label to display the result
    result_label.config(text=result)

# Create the main tkinter window
window = Tk()
window.title("Leap Year Checker")

# Add label and entry widget for input
label_year = Label(window, text="Enter the year:")
label_year.grid(row=0, column=0)
entry_year = Entry(window)
entry_year.grid(row=0, column=1)

# Add a label widget to display the result
result_label = Label(window, width=20, height=2, text="")
result_label.grid(row=1, column=0, columnspan=2)

# Add a button to trigger the calculation
button_check = Button(window, text="Check", width=10, command=is_leap_year)
button_check.grid(row=2, column=0, columnspan=2)

window.mainloop()
