
"""
Topic: Tkinter Entry Fields
File: 05_Entry_Fields.py
Purpose: Learn to create input fields, read and insert text,
         use password masking, and display user input.
"""

# 1. SHORT THEORY

"""
An Entry field accepts single-line text input from the user.

Important concepts:

1. tk.Entry() creates an input field.
2. get() reads the entered text.
3. insert() adds text at a specified position.
4. delete() removes text from the field.
5. StringVar() stores text in a Tkinter variable.
6. textvariable connects an Entry to a variable.
7. show="*" masks password characters.
8. width controls the input field width.
9. config() changes widget properties.
10. pack() displays the widget.
"""


# 2. IMPORTS

import tkinter as tk


# 3. WORKING PROGRAM — ENTRY FIELD MANAGEMENT

root = tk.Tk()
root.title("Tkinter Entry Fields")
root.geometry("450x450")
root.configure(bg="#eaf2f8")

title_label = tk.Label(
    root,
    text="User Registration Login",
    font=("Arial", 20, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
title_label.pack(pady=15)

# Create a name input field with a default value
tk.Label(root, text="Enter Name:", bg="#eaf2f8").pack()

name_entry = tk.Entry(root, width=30, font=("Arial", 12))
name_entry.pack(pady=5)

# Create a password input field
tk.Label(root, text="Enter Password:", bg="#eaf2f8").pack()

password_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12),
    show="*"
)
password_entry.pack(pady=5)

# Create a variable connected to an Entry field
email_text = tk.StringVar()

tk.Label(root, text="Enter Email:", bg="#eaf2f8").pack()

email_entry = tk.Entry(
    root,
    width=30,
    textvariable=email_text
)
email_entry.pack(pady=5)

# Read and display the user's input
def submit_details():
    name = name_entry.get()
    password = password_entry.get()
    email = email_text.get()

    result_label.config(
        text=f"Name: {name}\nEmail: {email}"
    )

# Clear all input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    result_label.config(text="")

submit_button = tk.Button(
    root,
    text="Submit",
    command=submit_details
)
submit_button.pack(pady=8)

clear_button = tk.Button(
    root,
    text="Clear Fields",
    command=clear_fields
)
clear_button.pack(pady=5)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    bg="#eaf2f8",
    fg="#196f3d"
)
result_label.pack(pady=10)

root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
Syntax                                  Meaning

tk.Entry(root)                          Create an input field
entry.get()                             Read entered text
entry.insert(0, "Hello")                Insert text at the beginning
entry.delete(0, tk.END)                 Clear the input field
tk.StringVar()                          Create a string variable
textvariable=variable                   Link Entry to a variable
show="*"                                Mask password characters
width=30                                Set input field width
entry.config(state="disabled")          Disable the field
entry.config(state="normal")            Enable the field
command=submit_details                  Connect a button to a function
result_label.config(text="Hello")       Update a label
entry.pack()                            Display the Entry widget
root.mainloop()                         Start the event loop

Important Rules:

1. Use get() to retrieve the input.
2. Use insert() to add text and delete() to remove text.
3. tk.END represents the end of the input field.
4. show="*" hides password characters visually.
5. textvariable connects the Entry to a Tkinter variable.
6. Use config() to modify an existing widget.
7. Do not display or print passwords unnecessarily.
8. Tkinter Entry fields accept single-line input.
"""
