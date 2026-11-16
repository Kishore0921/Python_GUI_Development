
"""
Topic: Callbacks
File: 19_Callbacks.py
Purpose: Understand callbacks and connect functions to Tkinter widgets.
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Callbacks")
root.geometry("400x400")

# 1. Basic Callback
def say_hello():
    label.config(text="Hello! Welcome.")

# 2. Callback with Arguments
def greet_user(name):
    label.config(text=f"Hello, {name}!")

# 3. Lambda Callback
def show_message():
    messagebox.showinfo("Message", "Button clicked!")

# 4. Callback Returning a Result
def add_numbers(a, b):
    return a + b

def calculate():
    result = add_numbers(10, 20)
    label.config(text=f"Result: {result}")

# Widgets
label = tk.Label(root, text="Click a button", font=("Arial", 14))
label.pack(pady=15)

# Using command=
tk.Button(root, text="Say Hello", command=say_hello).pack(pady=5)

# Passing Arguments using lambda
tk.Button(
    root,
    text="Greet Kishore",
    command=lambda: greet_user("Kishore")
).pack(pady=5)

# Lambda Callback
tk.Button(
    root,
    text="Show Message",
    command=lambda: show_message()
).pack(pady=5)

# Returning Result
tk.Button(root, text="Add Numbers", command=calculate).pack(pady=5)

root.mainloop()
