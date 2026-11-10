
"""
Topic: Tkinter Message Boxes
File: 15_Message_Boxes.py
Purpose: Learn messagebox functions and confirmation dialogs.
"""

# 1. SHORT THEORY

"""
Message Boxes display information and ask users for confirmation.

showinfo()       - Information message
showwarning()    - Warning message
showerror()      - Error message
askyesno()       - Yes or No confirmation
askokcancel()    - OK or Cancel confirmation
askretrycancel() - Retry or Cancel confirmation
askquestion()    - Yes or No question

Messagebox functions return values that can be
used in if conditions.
"""

# 2. IMPORTS

import tkinter as tk
from tkinter import messagebox

# 3. WORKING PROGRAM

root = tk.Tk()
root.title("Tkinter Message Boxes")
root.geometry("400x450")

# Display information
def show_info():
    messagebox.showinfo("Information", "Operation completed successfully!")

# Display warning
def show_warning():
    messagebox.showwarning("Warning", "Please check your input!")

# Display error
def show_error():
    messagebox.showerror("Error", "Something went wrong!")

# Yes or No confirmation
def ask_yes_no():
    answer = messagebox.askyesno("Confirm", "Do you want to continue?")

    if answer:
        result.config(text="You selected Yes")
    else:
        result.config(text="You selected No")

# OK or Cancel confirmation
def ask_ok_cancel():
    answer = messagebox.askokcancel("Confirm", "Do you want to proceed?")

    result.config(text="Confirmed!" if answer else "Cancelled")

# Retry or Cancel confirmation
def ask_retry_cancel():
    answer = messagebox.askretrycancel("Retry", "Do you want to try again?")

    result.config(text="Retry selected" if answer else "Cancelled")

# Yes or No question
def ask_question():
    answer = messagebox.askquestion("Question", "Do you like Python?")

    result.config(text=f"Answer: {answer}")

# Buttons
tk.Button(root, text="Show Info", command=show_info).pack(pady=5)
tk.Button(root, text="Show Warning", command=show_warning).pack(pady=5)
tk.Button(root, text="Show Error", command=show_error).pack(pady=5)
tk.Button(root, text="Ask Yes/No", command=ask_yes_no).pack(pady=5)
tk.Button(root, text="Ask OK/Cancel", command=ask_ok_cancel).pack(pady=5)
tk.Button(root, text="Ask Retry/Cancel", command=ask_retry_cancel).pack(pady=5)
tk.Button(root, text="Ask Question", command=ask_question).pack(pady=5)

result = tk.Label(root, text="Select an option")
result.pack(pady=15)

# Confirm before closing
def close_window():
    answer = messagebox.askyesno("Exit", "Do you want to close the application?")

    if answer:
        root.destroy()

tk.Button(root, text="Exit", command=close_window).pack(pady=5)

root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
1. Import messagebox using:
   from tkinter import messagebox

2. showinfo() displays information.
3. showwarning() displays a warning.
4. showerror() displays an error.
5. askyesno() returns True or False.
6. askokcancel() returns True or False.
7. askretrycancel() returns True or False.
8. askquestion() returns "yes" or "no".
9. Use returned values inside if conditions.
10. Use confirmation dialogs before deletion or exit.
"""
