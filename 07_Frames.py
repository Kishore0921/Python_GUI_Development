
"""
Topic: Tkinter Frames
File: 07_Frames.py
Purpose: Learn to create frames, group widgets, organize
         window sections, and use nested frames.
"""

# 1. SHORT THEORY

"""
A Frame is a container used to organize widgets in a window.

1. tk.Frame() creates a frame.
2. Frames group related widgets together.
3. width and height specify frame dimensions.
4. bg sets the background color.
5. relief controls the border appearance.
6. bd specifies border thickness.
7. padx and pady provide internal padding.
8. Nested frames are frames placed inside other frames.
9. Layout managers arrange widgets inside frames.
10. Frames help organize header, content, and footer sections.

Frames can use different layout managers in separate containers.
"""


# 2. IMPORTS

import tkinter as tk


# 3. WORKING PROGRAM — FRAME MANAGEMENT

root = tk.Tk()
root.title("Tkinter Frames")
root.geometry("600x500")
root.configure(bg="#eaf2f8")

# Create the header frame
header_frame = tk.Frame(
    root,
    bg="#154360",
    height=70,
    relief="raised",
    bd=3
)
header_frame.pack(fill="x", padx=10, pady=10)
header_frame.pack_propagate(False)  # Keep the specified height

# Add a title inside the header frame
title_label = tk.Label(
    header_frame,
    text="Tkinter Frame Management",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#154360"
)
title_label.pack(pady=18)

# Create the content frame
content_frame = tk.Frame(
    root,
    bg="#d6eaf8",
    width=500,
    height=250,
    relief="sunken",
    bd=3,
    padx=10,
    pady=10
)
content_frame.pack(fill="x", padx=20, pady=10)
content_frame.pack_propagate(False)  # Keep the specified size

# Add a label inside the content frame
name_label = tk.Label(
    content_frame,
    text="Enter your name:",
    font=("Arial", 12),
    bg="#c9e914"
)
name_label.pack(pady=5)

# Add an entry field inside the content frame
name_entry = tk.Entry(content_frame, width=35, font = ("Times New Roman", 12))
name_entry.pack(pady=5)

# Create a nested frame for buttons
button_frame = tk.Frame(
    content_frame,
    bg="#d6eaf8",  # Changed from #ee2762 to match content_frame
    padx=10,
    pady=10
)
button_frame.pack(pady=5)


# Define the submit function
def submit_action():
    name = name_entry.get()
    result_label.config(text=f"Welcome, {name}")

# Define the clear function
def clear_action():
    name_entry.delete(0, tk.END)
    result_label.config(text="")

# Create the submit button
submit_button = tk.Button(
    button_frame,
    text="Submit",
    command=submit_action
)
submit_button.pack(side="left", padx=5)

# Create the clear button
clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_action
)
clear_button.pack(side="left", padx=5)

# Display the result inside the content frame
result_label = tk.Label(
    content_frame,
    text="",
    font=("Arial", 12, "bold"),
    bg="#d6eaf8",  # Changed from #e05d5d to match the light blue background
    fg="#196f3d"
)
result_label.pack(pady=5)


# Create the footer frame
footer_frame = tk.Frame(
    root,
    bg="#abebc6",
    height=60,
    relief="groove",
    bd=2
)
footer_frame.pack(fill="x", padx=10, pady=10)
footer_frame.pack_propagate(False)

# Add a close button inside the footer
close_button = tk.Button(
    footer_frame,
    text="Close Window",
    command=root.destroy
)
close_button.pack(pady=15)

root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
Syntax                                  Meaning

tk.Frame(root)                          Create a frame
tk.Frame(parent)                        Create a nested frame
bg="lightblue"                          Set background color
width=300, height=100                   Set frame dimensions
relief="raised"                         Create a raised border
relief="sunken"                         Create a sunken border
relief="groove"                         Create a grooved border
bd=3                                    Set border thickness
padx=10, pady=10                        Set internal padding
frame.pack()                            Display the frame
frame.pack(fill="x")                    Fill horizontally
frame.pack(fill="both", expand=True)    Fill available space
frame.pack_propagate(False)             Keep requested frame size
frame.grid(row=0, column=0)             Position frame using grid
frame.place(x=50, y=100)                Position frame using coordinates
tk.Frame(content_frame)                 Create a frame inside another frame

Important Rules:

1. Frames are containers for organizing widgets.
2. Place labels, buttons, and entries inside their parent frame.
3. Use nested frames to group related widgets.
4. Use pack_propagate(False) to prevent child widgets from
   determining the frame's requested size.
5. padx and pady in a Frame constructor provide internal padding.
6. padx and pady in pack() provide external spacing.
7. Frames can organize a window into header, content, and footer.
8. Use pack() and grid() in different parent containers,
   rather than mixing them within the same parent.
9. Frames make complex GUI applications easier to maintain.
10. root.mainloop() starts the GUI event loop.
"""
