
import tkinter as tk

root = tk.Tk()
root.title("Calculator window")
root.geometry("500x500")
root.configure(bg="lightgreen")

root.resizable(True, False)  # Allow resizing in width only
root.minsize(300, 300)
root.maxsize(800, 800)
root.state("normal")

print("Current window state:", root.state())

description_label = tk.Label(
    root,
    text="Calculator window with resizable width and fixed height.",
    font=("Times New Roman", 16, "bold"),
    fg="#212f3c",
    bg="white",
    width=40,
    height=4,
    anchor="w",
    justify="center",
    wraplength=400,
    padx=15,
    pady=10,
    relief="sunken",
    bd=2
)
description_label.pack(pady=10)


# Function to change the label text
def change_text():
    description_label.config(text="Welcome to Python GUI Development!")


# Function to reset the label text
def reset_text():
    description_label.config(
        text="Calculator window with resizable width and fixed height."
    )


# Create a button to change the text
change_button = tk.Button(
    root,
    text="Change Text",
    font=("Arial", 12, "bold"),
    bg="lightblue",
    command=change_text
)
change_button.pack(pady=5)

# Create a button to reset the text
reset_button = tk.Button(
    root,
    text="Reset Text",
    font=("Arial", 12),
    command=reset_text
)
reset_button.pack(pady=5)

# Create a button to close the window
close_button = tk.Button(
    root,
    text="Close Window",
    font=("Arial", 12),
    bg="tomato",
    command=root.destroy
)
close_button.pack(pady=5)

root.mainloop()
