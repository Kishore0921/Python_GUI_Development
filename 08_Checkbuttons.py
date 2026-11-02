
"""
Topic: Tkinter Checkbuttons
File: 08_Checkbuttons.py
Purpose: Learn to create checkbuttons, manage multiple selections,
         retrieve selected values, and update GUI labels.
"""

# 1. SHORT THEORY

"""
A Checkbutton is a Tkinter widget used to select or deselect options.

1. tk.Checkbutton() creates a checkbutton widget.
2. BooleanVar() stores True or False values.
3. variable connects a checkbutton to a Tkinter variable.
4. get() retrieves the selected value.
5. set() changes the variable value.
6. onvalue specifies the value when selected.
7. offvalue specifies the value when deselected.
8. command executes a function when the option changes.
9. select() selects a checkbutton.
10. deselect() deselects a checkbutton.
11. toggle() switches between selected and deselected states.
12. Multiple checkbuttons allow multiple selections.

Checkbuttons are commonly used for preferences, hobbies,
skills, and selecting multiple options.
"""


# 2. IMPORTS

import tkinter as tk


# 3. WORKING PROGRAM — CHECKBUTTON MANAGEMENT

root = tk.Tk()
root.title("Tkinter Checkbuttons")
root.geometry("500x500")
root.configure(bg="#eaf2f8")

# Create the title label
title_label = tk.Label(
    root,
    text="Select Your Programming Skills",
    font=("Arial", 18, "bold"),
    fg="#154360",
    bg="#eaf2f8"
)
title_label.pack(pady=15)

# Create a frame for checkbuttons
check_frame = tk.Frame(
    root,
    bg="white",
    padx=20,
    pady=15,
    relief="groove",
    bd=2
)
check_frame.pack(padx=20, pady=10)

# Create Tkinter Boolean variables
python_var = tk.BooleanVar()
java_var = tk.BooleanVar()
cpp_var = tk.BooleanVar()

# Create the Python checkbutton
python_check = tk.Checkbutton(
    check_frame,
    text="Python",
    variable=python_var,
    onvalue=True,
    offvalue=False,
    bg="white",
    font=("Arial", 12)
)
python_check.pack(anchor="w", pady=5)

# Create the Java checkbutton
java_check = tk.Checkbutton(
    check_frame,
    text="Java",
    variable=java_var,
    bg="white",
    font=("Arial", 12)
)
java_check.pack(anchor="w", pady=5)

# Create the C++ checkbutton
cpp_check = tk.Checkbutton(
    check_frame,
    text="C++",
    variable=cpp_var,
    bg="white",
    font=("Arial", 12)
)
cpp_check.pack(anchor="w", pady=5)

# Create a label to display selected options
result_label = tk.Label(
    root,
    text="Selected Skills: None",
    font=("Arial", 12, "bold"),
    fg="#196f3d",
    bg="#eaf2f8",
    wraplength=400
)
result_label.pack(pady=15)


# Define the submit function
def submit_action():
    selected = []

    if python_var.get():
        selected.append("Python")

    if java_var.get():
        selected.append("Java")

    if cpp_var.get():
        selected.append("C++")

    if selected:
        result_label.config(
            text="Selected Skills: " + ", ".join(selected)
        )
    else:
        result_label.config(text="No skills selected")


# Define the clear function
def clear_action():
    python_var.set(False)
    java_var.set(False)
    cpp_var.set(False)

    result_label.config(text="Selected Skills: None")


# Create a frame for buttons
button_frame = tk.Frame(root, bg="#eaf2f8")
button_frame.pack(pady=10)

# Create the submit button
submit_button = tk.Button(
    button_frame,
    text="Submit",
    command=submit_action
)
submit_button.pack(side="left", padx=10)

# Create the clear button
clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_action
)
clear_button.pack(side="left", padx=10)

root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
Syntax                                  Meaning

tk.Checkbutton(root)                    Create a checkbutton
text="Python"                           Set checkbutton text
tk.BooleanVar()                         Create a Boolean variable
variable=python_var                     Connect a variable
onvalue=True                            Value when selected
offvalue=False                          Value when deselected
variable.get()                          Retrieve the selected value
variable.set(True)                      Select the option
variable.set(False)                     Deselect the option
check.select()                          Select a checkbutton
check.deselect()                        Deselect a checkbutton
check.toggle()                          Toggle the checkbutton
command=function                        Execute a function on change
check.pack()                            Display the checkbutton

Important Rules:

1. Checkbuttons allow multiple options to be selected.
2. BooleanVar() stores True or False values.
3. get() retrieves the current variable value.
4. set() changes the variable value.
5. onvalue and offvalue define selected and deselected values.
6. command connects a function to a checkbutton.
7. select(), deselect(), and toggle() control checkbutton states.
8. Each independent checkbutton should have its own variable.
9. Use a list to collect multiple selected options.
10. root.mainloop() starts the GUI event loop.
"""
