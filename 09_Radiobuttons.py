
"""
Topic: Tkinter Radiobuttons
File: 09_RadioButtons.py
Purpose: Learn to create radiobuttons, select one option,
         retrieve selected values, and update GUI labels.
"""

# 1. SHORT THEORY

"""
A Radiobutton is a Tkinter widget used to select one option
from a group of available choices.

1. tk.Radiobutton() creates a radiobutton widget.
2. StringVar() stores a selected string value.
3. IntVar() stores a selected integer value.
4. variable connects radiobuttons to a Tkinter variable.
5. value specifies the value assigned to each option.
6. get() retrieves the currently selected value.
7. set() changes the selected option.
8. command executes a function when selection changes.
9. select() selects a radiobutton.
10. deselect() removes the selection.
11. invoke() executes the radiobutton's command.
12. Radiobuttons sharing the same variable form a group.

Radiobuttons are commonly used for gender selection,
payment methods, choices, and selecting operations.
"""


# 2. IMPORTS

import tkinter as tk


# 3. WORKING PROGRAM — RADIOBUTTON MANAGEMENT

root = tk.Tk()
root.title("Tkinter Radiobuttons")
root.geometry("500x500")
root.configure(bg="#eaf2f8")

# Create the title label
title_label = tk.Label(
    root,
    text="Select Your Preferred Language",
    font=("Arial", 18, "bold"),
    fg="#154360",
    bg="#eaf2f8"
)
title_label.pack(pady=15)

# Create a frame for radiobuttons
radio_frame = tk.Frame(
    root,
    bg="white",
    padx=20,
    pady=15,
    relief="groove",
    bd=2
)
radio_frame.pack(padx=20, pady=10)

# Create a StringVar
language_var = tk.StringVar(value="Python")

# Create the Python radiobutton
python_radio = tk.Radiobutton(
    radio_frame,
    text="Python",
    variable=language_var,
    value="Python",
    bg="white",
    font=("Arial", 12)
)
python_radio.pack(anchor="w", pady=5)

# Create the Java radiobutton
java_radio = tk.Radiobutton(
    radio_frame,
    text="Java",
    variable=language_var,
    value="Java",
    bg="white",
    font=("Arial", 12)
)
java_radio.pack(anchor="w", pady=5)

# Create the C++ radiobutton
cpp_radio = tk.Radiobutton(
    radio_frame,
    text="C++",
    variable=language_var,
    value="C++",
    bg="white",
    font=("Arial", 12)
)
cpp_radio.pack(anchor="w", pady=5)

# Create a label to display the selected option
result_label = tk.Label(
    root,
    text="Selected Language: Python",
    font=("Arial", 12, "bold"),
    fg="#196f3d",
    bg="#eaf2f8"
)
result_label.pack(pady=15)


# Define the selection function
def show_selection():
    selected = language_var.get()
    result_label.config(
        text=f"Selected Language: {selected}"
    )


# Define the reset function
def reset_selection():
    language_var.set("Python")
    result_label.config(text="Selected Language: Python")


# Create a frame for buttons
button_frame = tk.Frame(root, bg="#eaf2f8")
button_frame.pack(pady=10)

# Create the submit button
submit_button = tk.Button(
    button_frame,
    text="Submit",
    command=show_selection
)
submit_button.pack(side="left", padx=10)

# Create the reset button
reset_button = tk.Button(
    button_frame,
    text="Reset",
    command=reset_selection
)
reset_button.pack(side="left", padx=10)

root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
Syntax                                  Meaning

tk.Radiobutton(root)                    Create a radiobutton
text="Python"                           Set radiobutton text
tk.StringVar()                          Create a string variable
tk.IntVar()                             Create an integer variable
variable=language_var                   Connect a variable
value="Python"                          Assign an option value
language_var.get()                      Retrieve selected value
language_var.set("Java")                Select the Java option
radio.select()                          Select a radiobutton
radio.deselect()                        Deselect a radiobutton
radio.invoke()                          Execute its command
command=function                        Execute a function on selection
radio.pack()                            Display the radiobutton

Important Rules:

1. Radiobuttons are used to select one option from a group.
2. All radiobuttons in a group must share the same variable.
3. Each radiobutton must have a different value.
4. StringVar() stores string values.
5. IntVar() stores integer values.
6. get() retrieves the selected value.
7. set() changes the selected option.
8. command connects a function to a radiobutton.
9. Different groups can use different variables.
10. root.mainloop() starts the GUI event loop.
"""
