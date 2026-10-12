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
root.mainloop()