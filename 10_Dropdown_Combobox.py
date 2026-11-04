"""
Topic: Tkinter Dropdown / Combobox
File: 10_Dropdown_Combobox.py
Purpose: Learn to create dropdown menus, define dropdown values,
         retrieve and update selections, handle selection events,
         and update other widgets based on the selected option.
"""

# 1. SHORT THEORY

"""
A Dropdown is a GUI component that allows users to select one
option from a predefined list of values.

1. ttk is a Tkinter module that provides themed widgets.
2. ttk.Combobox() creates a dropdown widget.
3. values defines the available dropdown options.
4. get() retrieves the currently selected value.
5. set() changes the selected value.
6. current() selects an item using its index.
7. state="readonly" prevents users from typing custom values.
8. bind() connects an event to a function.
9. <<ComboboxSelected>> is triggered when the user selects an option.
10. event is passed to the function connected using bind().
11. A Label can be updated using config() based on the selection.

Dropdowns are commonly used for selecting departments, courses,
cities, countries, categories, and other predefined options.
"""


# 2. IMPORTS

import tkinter as tk
from tkinter import ttk


# 3. WORKING PROGRAM — DROPDOWN / COMBOBOX MANAGEMENT

root = tk.Tk()
root.title("Tkinter Dropdown / Combobox")
root.geometry("500x500")
root.configure(bg="#eaf2f8")

# Create the title label
title_label = tk.Label(
    root,
    text="Select Your Department",
    font=("Arial", 18, "bold"),
    fg="#154360",
    bg="#eaf2f8"
)
title_label.pack(pady=20)

# Create a frame for the dropdown
dropdown_frame = tk.Frame(
    root,
    bg="white",
    padx=25,
    pady=20,
    relief="groove",
    bd=2
)
dropdown_frame.pack(padx=20, pady=10)

# Create the instruction label
instruction_label = tk.Label(
    dropdown_frame,
    text="Choose your department:",
    font=("Arial", 12),
    bg="white"
)
instruction_label.pack(pady=10)

# Define dropdown values
departments = [
    "Computer Science",
    "Information Science",
    "Electronics",
    "Mechanical",
    "Civil"
]

# Create the Combobox
department_combo = ttk.Combobox(
    dropdown_frame,
    values=departments,
    font=("Arial", 11),
    width=30,
    state="readonly"
)
department_combo.pack(pady=10)

# Select the first item by default
department_combo.current(0)


# Define a function to handle selection
def selection_action(event):
    selected_department = department_combo.get()

    result_label.config(
        text="Selected Department: " + selected_department
    )

    description_label.config(
        text="You selected the " + selected_department + " department."
    )


# Connect the selection event to the function
department_combo.bind(
    "<<ComboboxSelected>>",
    selection_action
)


# Define a function to change the selection
def change_selection():
    department_combo.set("Electronics")

    result_label.config(
        text="Selected Department: " + department_combo.get()
    )

    description_label.config(
        text="You selected the Electronics department."
    )


# Define a function to reset the dropdown
def clear_selection():
    department_combo.current(0)

    result_label.config(
        text="Selected Department: None"
    )

    description_label.config(
        text="Please select your department."
    )


# Create a label to display the selected value
result_label = tk.Label(
    root,
    text="Selected Department: Computer Science",
    font=("Arial", 12, "bold"),
    fg="#196f3d",
    bg="#eaf2f8",
    wraplength=400
)
result_label.pack(pady=15)

# Create a description label
description_label = tk.Label(
    root,
    text="Please select your department.",
    font=("Arial", 11),
    fg="#154360",
    bg="#eaf2f8",
    wraplength=400
)
description_label.pack(pady=5)

# Create a frame for buttons
button_frame = tk.Frame(root, bg="#eaf2f8")
button_frame.pack(pady=15)

# Create the change button
change_button = tk.Button(
    button_frame,
    text="Set Electronics",
    command=change_selection
)
change_button.pack(side="left", padx=10)

# Create the clear button
clear_button = tk.Button(
    button_frame,
    text="Reset",
    command=clear_selection
)
clear_button.pack(side="left", padx=10)


root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
Syntax                                  Meaning

from tkinter import ttk                Import themed widgets
ttk.Combobox(root)                     Create a dropdown
values=["Python", "Java"]              Define dropdown options
state="readonly"                       Prevent manual typing
combo.get()                            Retrieve selected value
combo.set("Python")                    Set a value
combo.current(0)                       Select item at index 0
combo.current(1)                       Select item at index 1
combo.current()                        Get selected item's index
combo.bind()                           Connect an event to a function
"<<ComboboxSelected>>"                 Event when an option is selected
event                                   Event information passed to function
label.config(text=value)               Update a label
combo.pack()                           Display the dropdown

Important Rules:

1. ttk.Combobox() creates a dropdown widget.
2. Import ttk using from tkinter import ttk.
3. values defines the available dropdown options.
4. get() retrieves the currently selected value.
5. set() changes the dropdown value.
6. current(index) selects an option using its position.
7. Indexing starts from 0.
8. state="readonly" prevents users from typing custom values.
9. bind() connects an event to a function.
10. <<ComboboxSelected>> detects user selection.
11. The function connected using bind() receives an event argument.
12. Use config() to update another widget based on the selection.
13. root.mainloop() starts the GUI event loop.
"""