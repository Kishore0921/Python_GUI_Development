
"""
Topic: Tkinter Labels
File: 03_Labels.py
Purpose: Learn to create, customize, update, and display text and images
         using Tkinter Label widgets.
"""

# 1. SHORT THEORY

"""
A Label is a Tkinter widget used to display text or images in a GUI.

Important concepts:

1. tk.Label() creates a label widget.
2. text displays a fixed text value.
3. textvariable connects a label to a Tkinter variable.
4. font specifies the font family, size, and style.
5. fg and bg control foreground and background colors.
6. width and height control label dimensions.
7. anchor positions content inside the label.
8. justify aligns multiple lines of text.
9. padx and pady provide internal padding.
10. config() updates label properties after creation.
11. tk.PhotoImage() loads supported image formats such as PNG.
12. relief controls the border appearance.
13. bd specifies border thickness.
14. pack() displays the label in its parent container.

A PhotoImage object should be stored in a variable so that
Python retains a reference to the image.
"""

# 2. IMPORTS

import tkinter as tk
from pathlib import Path


# 3. WORKING PROGRAM — LABEL MANAGEMENT

root = tk.Tk()
root.title("Tkinter Labels")
root.geometry("750x650")
root.configure(bg="#eaf2f8")

title_label = tk.Label(
    root,
    text="Python GUI Development",
    font=("Arial", 22, "bold"),
    fg="#154360",
    bg="#eaf2f8",
    width=35,
    height=2,
    anchor="center",
    justify="center",
    padx=10,
    pady=5,
    relief="raised",
    bd=3
)
title_label.pack(pady=15)

status_text = tk.StringVar(value="Status: Application Running")

status_label = tk.Label(
    root,
    textvariable=status_text,
    font=("Arial", 13, "italic"),
    fg="#196f3d",
    bg="#eaf2f8",
    padx=10,
    pady=5
)
status_label.pack(pady=5)

description_label = tk.Label(
    root,
    text="Tkinter labels can display text, status messages,\n"
         "instructions, and images in desktop applications.",
    font=("Arial", 12),
    fg="#212f3c",
    bg="white",
    width=55,
    height=4,
    anchor="w",
    justify="left",
    wraplength=500,
    padx=15,
    pady=10,
    relief="solid",
    bd=2
)
description_label.pack(pady=10)

image_path = Path(__file__).with_name("logo.png")
image_reference = None

if image_path.exists():
    image_reference = tk.PhotoImage(file=str(image_path))
    image_label = tk.Label(
        root,
        image=image_reference,
        bg="#eaf2f8",
        relief="groove",
        bd=2,
        padx=10,
        pady=10
    )
    image_label.pack(pady=10)
else:
    image_label = tk.Label(
        root,
        text="Place a supported PNG image named logo.png\n"
             "in the same folder to display it here.",
        font=("Arial", 10),
        fg="#616a6b",
        bg="#eaf2f8",
        padx=10,
        pady=10
    )
    image_label.pack(pady=10)

def update_label():
    title_label.config(
        text="Labels Updated Successfully",
        fg="#7d3c98",
        relief="sunken"
    )
    status_text.set("Status: Label Updated")
    description_label.config(
        text="The config() method updates label properties.\n"
             "The textvariable updates when its linked variable changes.",
        bg="#fcf3cf",
        fg="#784212"
    )

update_button = tk.Button(
    root,
    text="Update Labels",
    font=("Arial", 12, "bold"),
    command=update_label
)
update_button.pack(pady=15)

root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
Syntax                                  Meaning

tk.Label(root, text="Hello")            Create a label
text="Hello"                            Display fixed text
textvariable=variable                   Display variable value
tk.StringVar(value="Hello")             Create a Tkinter string variable
font=("Arial", 16, "bold")              Set font family, size, and style
fg="blue"                               Set foreground color
bg="white"                              Set background color
width=30                                Set label width
height=2                                Set label height
anchor="w"                              Position content to the left
justify="left"                          Align multiple lines to the left
padx=10                                 Set horizontal internal padding
pady=10                                 Set vertical internal padding
label.config(text="Updated")            Update label properties
tk.PhotoImage(file="logo.png")          Load a supported image
relief="raised"                         Create a raised border
relief="sunken"                         Create a sunken border
relief="solid"                          Create a solid border
relief="groove"                         Create a grooved border
bd=3                                    Set border thickness
label.pack()                            Display the label
root.mainloop()                         Start the GUI event loop

Important Rules:

1. Create the root window before creating labels.
2. Use a geometry manager to display every label.
3. fg controls text color, while bg controls background color.
4. text displays fixed text; textvariable links a Tkinter variable.
5. Use config() to update an existing label.
6. anchor controls content positioning within a label.
7. justify controls alignment of multiple lines.
8. padx and pady add internal padding.
9. Label width and height generally use character-based units.
10. PhotoImage supports PNG and GIF; image support can vary by
    Tkinter version and image format.
11. Keep a reference to PhotoImage to prevent it from disappearing.
12. The image file must exist at the specified path.
13. relief controls border appearance, while bd controls thickness.
"""
