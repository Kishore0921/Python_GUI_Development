import tkinter as tk

root = tk.Tk()
root.title("Calculator window")
root.geometry("500x500")
root.configure(bg="lightgreen")
root.resizable(True, False)  # Allow resizing in width only.)
root.minsize(300, 300)
root.maxsize(800, 800)
root.state("normal")  # Start in the normal window state.
print("Current window state:", root.state())  # Print the current window state in the terminal in the opening state.
description_label = tk.Label(
    root,
    text="Calculator window with resizable width and fixed height.\n",
    font=("Times New Roman", 20, "bold"),
    fg="#212f3c",
    bg="white",
    width=55,   
    height=4,
    anchor="w",
    justify="center",
    wraplength=500,
    padx=15,
    pady=10,
    relief="sunken",
    bd=2
)
description_label.pack(pady=10)
root.mainloop()