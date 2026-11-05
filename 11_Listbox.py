"""
Topic: Tkinter Listbox
File: 11_Listbox.py
Purpose: Learn to create listboxes, add and remove items,
         select single or multiple items, retrieve selections,
         and update GUI labels.
"""

# 1. SHORT THEORY

"""
A Listbox is a Tkinter widget used to display a list of items
from which users can select one or multiple options.

1. tk.Listbox() creates a listbox widget.
2. insert() adds items to the listbox.
3. tk.END inserts an item at the end of the list.
4. curselection() retrieves the indexes of selected items.
5. get() retrieves an item using its index.
6. delete() removes items from the listbox.
7. selection_set() selects an item using its index.
8. selection_clear() clears selected items.
9. selectmode controls single or multiple selection.
10. size() returns the number of items in the listbox.
11. activate() sets the active item using its index.
12. A Listbox can be used with buttons to add, remove,
    and display selected items.

Listboxes are commonly used for selecting courses, subjects,
departments, files, products, and other items.
"""


# 2. IMPORTS

import tkinter as tk


# 3. WORKING PROGRAM — LISTBOX MANAGEMENT

root = tk.Tk()
root.title("Tkinter Listbox")
root.geometry("500x550")
root.configure(bg="#eaf2f8")

# Create the title label
title_label = tk.Label(
    root,
    text="Select Your Courses",
    font=("Arial", 18, "bold"),
    fg="#154360",
    bg="#eaf2f8"
)
title_label.pack(pady=15)

# Create a frame for the listbox
list_frame = tk.Frame(
    root,
    bg="white",
    padx=20,
    pady=15,
    relief="groove",
    bd=2
)
list_frame.pack(padx=20, pady=10)

# Create the instruction label
instruction_label = tk.Label(
    list_frame,
    text="Available Courses:",
    font=("Arial", 12, "bold"),
    bg="white"
)
instruction_label.pack(pady=5)

# Create the Listbox
course_listbox = tk.Listbox(
    list_frame,
    width=30,
    height=8,
    font=("Arial", 11),
    selectmode=tk.MULTIPLE,
    selectbackground="#3498db",
    selectforeground="white"
)
course_listbox.pack(pady=10)

# Define available courses
courses = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "Data Science",
    "Machine Learning"
]

# Add courses to the Listbox
for course in courses:
    course_listbox.insert(tk.END, course)


# Define the submit function
def submit_action():
    selected_indexes = course_listbox.curselection()

    selected_courses = [
        course_listbox.get(index)
        for index in selected_indexes
    ]

    if selected_courses:
        result_label.config(
            text="Selected Courses: " + ", ".join(selected_courses)
        )
    else:
        result_label.config(text="No courses selected")


# Define the add function
def add_course():
    new_course = course_entry.get().strip()

    if new_course:
        course_listbox.insert(tk.END, new_course)
        course_entry.delete(0, tk.END)


# Define the remove function
def remove_course():
    selected_indexes = course_listbox.curselection()

    for index in reversed(selected_indexes):
        course_listbox.delete(index)

    result_label.config(text="Selected Courses: None")


# Define the select first item function
def select_first():
    if course_listbox.size() > 0:
        course_listbox.selection_clear(0, tk.END)
        course_listbox.selection_set(0)
        course_listbox.activate(0)


# Create an entry field to add courses
course_entry = tk.Entry(
    root,
    font=("Arial", 11),
    width=25
)
course_entry.pack(pady=10)

# Create a frame for buttons
button_frame = tk.Frame(root, bg="#eaf2f8")
button_frame.pack(pady=10)

# Create the submit button
submit_button = tk.Button(
    button_frame,
    text="Submit",
    command=submit_action
)
submit_button.pack(side="left", padx=5)

# Create the add button
add_button = tk.Button(
    button_frame,
    text="Add Course",
    command=add_course
)
add_button.pack(side="left", padx=5)

# Create the remove button
remove_button = tk.Button(
    button_frame,
    text="Remove Selected",
    command=remove_course
)
remove_button.pack(side="left", padx=5)

# Create the select first button
select_button = tk.Button(
    root,
    text="Select First Course",
    command=select_first
)
select_button.pack(pady=5)

# Create a label to display selected courses
result_label = tk.Label(
    root,
    text="Selected Courses: None",
    font=("Arial", 11, "bold"),
    fg="#196f3d",
    bg="#eaf2f8",
    wraplength=420
)
result_label.pack(pady=15)

root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
Syntax                                  Meaning

tk.Listbox(root)                        Create a listbox
listbox.insert(tk.END, "Python")        Add an item at the end
listbox.get(0)                          Retrieve item at index 0
listbox.curselection()                  Get selected item indexes
listbox.delete(0)                       Delete item at index 0
listbox.delete(0, tk.END)               Delete all items
listbox.selection_set(0)                Select item at index 0
listbox.selection_clear(0, tk.END)      Clear all selections
listbox.size()                          Get the number of items
listbox.activate(0)                     Activate item at index 0
selectmode=tk.SINGLE                    Allow one selection
selectmode=tk.MULTIPLE                  Allow multiple selections
listbox.pack()                          Display the listbox

Important Rules:

1. Listbox displays a collection of selectable items.
2. insert() adds items to the listbox.
3. tk.END adds an item at the end.
4. curselection() returns selected item indexes.
5. get(index) retrieves an item using its index.
6. delete() removes items from the listbox.
7. selection_set() selects items.
8. selection_clear() clears selected items.
9. selectmode=tk.SINGLE allows one selection.
10. selectmode=tk.MULTIPLE allows multiple selections.
11. size() returns the total number of items.
12. activate() sets the active item.
13. Indexing starts from 0.
14. Delete multiple selected items in reverse index order.
15. root.mainloop() starts the GUI event loop.
"""