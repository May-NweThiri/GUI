from tkinter import *
from tkinter import messagebox

# Functions go here:
def calculate_price():
    ticket = ticket_var.get()
    ticket_class = class_var.get()
    is_return = return_var.get()
    meal = meal_var.get()

    if ticket == "e":
        if ticket_class == "b":
            if is_return == "y":
                price = 178 # Edinburgh business return
            else:
                price = 87 # Edinburgh one way
        else: # economy class
            if is_return == "y":
                if meal == "y":
                    price = 52 + 18 # Edinburgh return with meal
                else: # no meal
                    price = 52 # Edinburgh return
            else: # one way
                if meal == "y":
                    price = 32 + 12 # Edinburgh economy one way with meal
                else:
                    price = 32 # Edinburgh economy one way
    else: # Cardiff
        if ticket_class == "b":
            if is_return == "y":
                price = 138 # Cardiff business return
            else:
                price = 72 # Cardiff one way
        else: # economy class
            if is_return == "y":
                if meal == "y":
                    price = 50 + 18 # Cardiff return with meal
                else: # no meal
                    price = 50 # Cardiff return
            else: # one way
                if meal == "y":
                    price = 36 + 12 # Cardiff economy one way with meal
                else:
                    price = 36 # Cardiff economy one way
    
    messagebox.showinfo("Ticket Price", f"The price of the ticket is: ${price}")

# GUI code goes here:
# Create the main tkinter window
window = Tk()
window.title("Ticket Price Calculator")

# Ticket destination
Label(window, text="Choose the tickets:").grid(row=0, column=0, sticky=W)
ticket_var = StringVar()
radio1 = Radiobutton(window, text="Edinburgh", variable=ticket_var, value="e")
radio1.grid(row=1, column=0, sticky=W)
radio1.select()
radio2 = Radiobutton(window, text="Cardiff", variable=ticket_var, value="c")
radio2.grid(row=2, column=0, sticky=W)

# Ticket class
Label(window, text="Choose the class:").grid(row=0, column=1, sticky=W)
class_var = StringVar()
radio3 = Radiobutton(window, text="Economy", variable=class_var, value="eco")
radio3.grid(row=1, column=1, sticky=W)
radio3.select()
radio4 = Radiobutton(window, text="Business", variable=class_var, value="b")
radio4.grid(row=2, column=1, sticky=W)

# Return ticket
Label(window, text="Return ticket:").grid(row=3, column=0, sticky=W)
return_var = StringVar()
radio5 = Radiobutton(window, text="Yes", variable=return_var, value="y")
radio5.grid(row=4, column=0, sticky=W)
radio5.select()
radio6 = Radiobutton(window, text="No", variable=return_var, value="n")
radio6.grid(row=5, column=0, sticky=W)

# Meal preference
Label(window, text="Meal:").grid(row=3, column=1, sticky=W)
meal_var = StringVar()
radio7 = Radiobutton(window, text="Yes", variable=meal_var, value="y")
radio7.grid(row=4, column=1, sticky=W)
radio7.select()
radio8 = Radiobutton(window, text="No", variable=meal_var, value="n")
radio8.grid(row=5, column=1, sticky=W)

# calculate button
my_button = Button(window, text="Calculate Price", width=15, command=calculate_price)
my_button.grid(row=6, column=0)

# Enter the main loop event
window.mainloop()
