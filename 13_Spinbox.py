
"""
Topic: Tkinter Spinbox
File: 13_Spinbox.py
Purpose: Learn Spinbox and create a quantity selector.
"""

# 1. SHORT THEORY

"""
Spinbox allows users to select values from a range or a list.

Important options:
from_    - Minimum value
to       - Maximum value
increment - Step between values
values   - Custom list of values
textvariable - Connects a StringVar
"""

# 2. IMPORTS
import tkinter as tk

# 3. WORKING PROGRAM
root = tk.Tk()
root.title("Tkinter Spinbox")
root.geometry("400x400")

# --- Quantity Row (Label next to Spinbox) ---
quantity_frame = tk.Frame(root)
quantity_frame.pack(pady=10)

quantity_label = tk.Label(quantity_frame, text="Select Quantity: ")
quantity_label.pack(side=tk.LEFT)

quantity = tk.Spinbox(quantity_frame, from_=1, to=20, increment=1, width=10)
quantity.pack(side=tk.LEFT)


# --- Age Row (Label next to Spinbox) ---
age_frame = tk.Frame(root)
age_frame.pack(pady=10)

age_label = tk.Label(age_frame, text="Select Age: ")
age_label.pack(side=tk.LEFT)

age_var = tk.StringVar(value="20")
age = tk.Spinbox(
    age_frame,
    values=(18, 19, 20, 21, 22, 23, 24, 25),
    textvariable=age_var,
    width=10
)
age.pack(side=tk.LEFT)


# Read Spinbox values
def show_values():
    result.config(text=f"Quantity: {quantity.get()}\nAge: {age.get()}")

# Set Spinbox value
def set_values():
    quantity.delete(0, tk.END)
    quantity.insert(0, "5")
    age_var.set("22")

# Bind event
def value_changed(event):
    result.config(text=f"Selected Age: {age_var.get()}")

age.bind("<FocusOut>", value_changed)

# Buttons
tk.Button(root, text="Submit", command=show_values).pack(pady=5)
tk.Button(root, text="Set Values", command=set_values).pack(pady=5)

result = tk.Label(root, text="Select your values")
result.pack(pady=15)

root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
1. tk.Spinbox() creates a Spinbox widget.
2. from_ defines the minimum value.
3. to defines the maximum value.
4. increment defines the step value.
5. values provides a custom list of options.
6. get() reads the selected value.
7. delete() and insert() can change the value.
8. set() is used with a connected StringVar.
9. textvariable connects a Tkinter variable.
10. bind() connects an event to a function.
"""
