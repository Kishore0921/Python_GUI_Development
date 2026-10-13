
"""
Topic: Tkinter Buttons
File: 04_Buttons.py
Purpose: Learn to create, customize, and control buttons
         and connect them to functions in Tkinter.
"""

# 1. SHORT THEORY

"""
A Button is a Tkinter widget that allows users to perform
an action by clicking it.

Buttons make GUI applications interactive by connecting
user actions to Python functions.

Important Concepts:
- Button: A clickable GUI widget.
- command: Connects a button to a function.
- Callback Function: A function executed by an event.
- width and height: Specify button dimensions.
- font: Sets the font family, size, and style.
- fg and bg: Control text and background colors.
- state: Controls whether a button is enabled or disabled.
- activebackground: Sets the background color when active.
- activeforeground: Sets the text color when active.
- config(): Updates button properties.
- invoke(): Executes the button's command programmatically.

Important Rules:
- Use command=function_name without parentheses.
- Use command=function_name() only when you intentionally
  want to call the function immediately, which is usually
  incorrect when assigning a button callback.
- Entry.get() retrieves text entered by the user.
- A button can update another widget using config().
- A disabled button cannot be activated through normal
  user interaction.
"""

# 2. IMPORTS

import tkinter as tk

# 3. WORKING PROGRAM — BUTTON MANAGEMENT

root = tk.Tk()
root.title("Tkinter Buttons")
root.geometry("500x500")
root.configure(bg="lightblue")

def update_label():
    result_label.config(text="Button Clicked Successfully!")

def greet_user():
    name = name_entry.get().strip()
    if name:
        result_label.config(text=f"Hello, {name}!")
    else:
        result_label.config(text="Please enter your name.")

def disable_button():
    action_button.config(state="disabled")
    result_label.config(text="Action button disabled.")

def enable_button():
    action_button.config(state="normal")
    result_label.config(text="Action button enabled.")

def update_button():
    action_button.config(
        text="Updated Button",
        bg="purple",
        fg="white",
        font=("Arial", 12, "bold")
    )
    result_label.config(text="Button properties updated.")

heading = tk.Label(
    root,
    text="Tkinter Button Demonstration",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
heading.pack(pady=15)

name_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25
)
name_entry.pack(pady=5)

result_label = tk.Label(
    root,
    text="Welcome!",
    font=("Arial", 12),
    bg="lightblue",
    fg="darkblue"
)
result_label.pack(pady=10)

action_button = tk.Button(
    root,
    text="Click Me",
    width=18,
    height=2,
    font=("Arial", 12, "bold"),
    fg="white",
    bg="blue",
    activebackground="green",
    activeforeground="white",
    state="normal",
    command=update_label
)
action_button.pack(pady=5)

greet_button = tk.Button(
    root,
    text="Greet User",
    command=greet_user
)
greet_button.pack(pady=5)

update_button_widget = tk.Button(
    root,
    text="Update Button",
    command=update_button
)
update_button_widget.pack(pady=5)

disable_button_widget = tk.Button(
    root,
    text="Disable Button",
    command=disable_button
)
disable_button_widget.pack(pady=5)

enable_button_widget = tk.Button(
    root,
    text="Enable Button",
    command=enable_button
)
enable_button_widget.pack(pady=5)

invoke_button = tk.Button(
    root,
    text="Invoke Action",
    command=action_button.invoke
)
invoke_button.pack(pady=5)

root.mainloop()

# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
Syntax                              Meaning

tk.Button(root, text="Click")        Create a button
text="Submit"                        Set button text
width=15, height=2                   Set button dimensions
command=function_name                Connect a callback function
font=("Arial", 12, "bold")           Set font family, size, style
fg="white"                           Set text color
bg="blue"                            Set background color
state="normal"                       Enable the button
state="disabled"                     Disable the button
activebackground="green"             Set active background color
activeforeground="white"              Set active text color
button.config(text="Updated")         Update button properties
entry.get()                          Retrieve input text
button.invoke()                      Execute the button command
button.pack()                        Display the button
root.mainloop()                      Start the event loop

Important Rules:
1. Use tk.Button() to create a button.
2. Use command=function_name to connect a callback.
3. Do not add parentheses to a callback reference.
4. Use config() to update button properties.
5. Use Entry.get() to retrieve user input.
6. Use state="disabled" to prevent normal user interaction.
7. Use state="normal" to enable the button.
8. invoke() executes the button's command programmatically.
9. A button can update labels and other widgets.
10. mainloop() keeps the GUI responsive.
"""
