
"""
Topic: Tkinter Layout Management
File: 06_Layout_Management.py
Purpose: Learn to arrange widgets using pack(), grid(),
         and place(), with spacing and alignment options.
"""

# 1. SHORT THEORY

"""
Tkinter layout managers control widget positioning.

1. pack() arranges widgets relative to one another.
2. grid() arranges widgets in rows and columns.
3. place() positions widgets using coordinates.
4. padx and pady add external spacing.
5. ipadx and ipady add internal spacing.
6. fill and expand control available space in pack().
7. sticky controls alignment and stretching in grid().
8. rowspan and columnspan allow widgets to occupy
   multiple rows or columns.

Do not mix pack() and grid() inside the same parent.
"""


# 2. IMPORTS

import tkinter as tk


# 3. WORKING PROGRAM — LAYOUT MANAGEMENT

root = tk.Tk()
root.title("Tkinter Layout Management")
root.geometry("600x550")
root.configure(bg="#eaf2f8")

# Demonstrate pack()
title_label = tk.Label(
    root,
    text="Tkinter Layout Managers",
    font=("Arial", 18, "bold"),
    bg="#154360",
    fg="white",
    padx=10,
    pady=10
)
title_label.pack(fill="x", padx=10, pady=10)

# Create a frame for grid() widgets
form_frame = tk.Frame(root, bg="#1325c4")
form_frame.pack(padx=20, pady=20)

# Demonstrate grid() with rows and columns
tk.Label(
    form_frame,
    text="Name:",
    bg="#ea22f8"
).grid(row=0, column=0, padx=5, pady=5, sticky="w")

name_entry = tk.Entry(form_frame, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(
    form_frame,
    text="Email:",
    bg="#ea22f8"
).grid(row=1, column=0, padx=5, pady=5, sticky="w")

email_entry = tk.Entry(form_frame, width=25)
email_entry.grid(row=1, column=1, padx=5, pady=5)

# Demonstrate columnspan
message_label = tk.Label(
    form_frame,
    text="Enter your details above",
    bg="#d6eaf8",
    padx=10,
    pady=5
)
message_label.grid(
    row=2,
    column=0,
    columnspan=2,
    padx=5,
    pady=10,
    sticky="ew"
)

def submit_action():
    name = name_entry.get()
    email = email_entry.get()
    message_label.config(
        text=f"Submitted: Name={name}, Email={email}"
    )

def clear_action():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    message_label.config(text="Enter your details above")

# Demonstrate pack() spacing and expansion in a separate frame
button_frame = tk.Frame(root, bg="#e70707")
button_frame.pack(fill="x", padx=20, pady=10)

submit_button = tk.Button(
    button_frame,
    text="Submit",
    command = submit_action,
    padx=10,
    pady=5
)
submit_button.pack(side="top", padx=10, ipadx=5, ipady=3)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command = clear_action,
)
clear_button.pack(side="top", padx=10)

# Demonstrate place() using x and y coordinates
position_label = tk.Label(
    root,
    bg="#fcf3cf",
    padx=5,
    pady=5
)
position_label.place(x=200, y=430)

root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
Syntax                                  Meaning

widget.pack()                           Arrange using pack
widget.pack(side="left")                Place towards the left
widget.pack(fill="x")                   Fill horizontally
widget.pack(fill="both", expand=True)   Fill and use extra space
widget.pack(padx=10, pady=10)           External spacing
widget.pack(ipadx=10, ipady=5)          Internal spacing
widget.grid(row=0, column=0)             Place in a grid cell
widget.grid(sticky="w")                  Align to the left
widget.grid(sticky="nsew")               Stretch in all directions
widget.grid(columnspan=2)                Occupy two columns
widget.grid(rowspan=2)                   Occupy two rows
widget.place(x=50, y=100)                Set absolute coordinates
widget.place(relx=0.5, rely=0.5)         Use relative coordinates
widget.place(anchor="center")            Position using its center

Important Rules:

1. pack(), grid(), and place() display and arrange widgets.
2. padx and pady control external spacing.
3. ipadx and ipady control internal spacing.
4. row and column indices start at zero.
5. sticky="nsew" stretches a widget within its grid cell.
6. columnspan and rowspan let widgets occupy multiple cells.
7. place() coordinates are relative to the parent container.
8. Avoid mixing pack() and grid() in the same parent.
9. Different frames can use different layout managers.
10. Use grid() for forms and calculator button layouts.
"""
