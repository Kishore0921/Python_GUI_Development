
import tkinter as tk
from tkinter import ttk, messagebox

# 1. Main Window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("500x850")
root.configure(bg="lightgreen")
root.minsize(350, 600)

# 2. Scrollable Area
canvas = tk.Canvas(root, bg="lightgreen", highlightthickness=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

main_frame = tk.Frame(canvas, bg="lightgreen")
frame_window = canvas.create_window((0, 0), window=main_frame, anchor="nw")

main_frame.bind(
    "<Configure>",
    lambda event: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.bind(
    "<Configure>",
    lambda event: canvas.itemconfig(frame_window, width=event.width)
)

canvas.bind_all(
    "<MouseWheel>",
    lambda event: canvas.yview_scroll(int(-event.delta / 120), "units")
)

# 3. Header
header_frame = tk.Frame(main_frame, bg="lightgreen")
header_frame.pack(fill="x", padx=10, pady=5)

tk.Label(
    header_frame,
    text="Python GUI Calculator",
    font=("Arial", 20, "bold"),
    fg="#154360",
    bg="lightgreen",
    padx=10,
    pady=10
).pack(pady=5)

description_label = tk.Label(
    header_frame,
    text="Enter two numbers and select an operation.",
    font=("Times New Roman", 12),
    fg="#212f3c",
    bg="white",
    relief="sunken",
    bd=2,
    padx=10,
    pady=5
)
description_label.pack(pady=5)

# 4. Input Fields
input_frame = tk.Frame(main_frame, bg="lightgreen", padx=10, pady=5)
input_frame.pack(pady=5)

tk.Label(
    input_frame,
    text="First Number:",
    font=("Arial", 11),
    bg="lightgreen"
).grid(row=0, column=0, padx=5, pady=5, sticky="w")

first_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=25,
    justify="center"
)
first_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(
    input_frame,
    text="Second Number:",
    font=("Arial", 11),
    bg="lightgreen"
).grid(row=1, column=0, padx=5, pady=5, sticky="w")

second_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=25,
    justify="center"
)
second_entry.grid(row=1, column=1, padx=5, pady=5)

# 5. Operation Dropdown
operations = [
    "Addition (+)",
    "Subtraction (-)",
    "Multiplication (×)",
    "Division (÷)"
]

operation_combo = ttk.Combobox(
    main_frame,
    values=operations,
    font=("Arial", 10),
    width=25,
    state="readonly"
)
operation_combo.pack(pady=10)
operation_combo.current(0)

# 6. Checkbuttons
options_frame = tk.Frame(main_frame, bg="lightgreen")
options_frame.pack(pady=5)

round_var = tk.BooleanVar()
details_var = tk.BooleanVar()

tk.Checkbutton(
    options_frame,
    text="Round Result",
    variable=round_var,
    bg="lightgreen"
).pack(side="left", padx=5)

tk.Checkbutton(
    options_frame,
    text="Show Calculation",
    variable=details_var,
    bg="lightgreen"
).pack(side="left", padx=5)

# 7. Scale - Result Precision
precision_var = tk.IntVar(value=2)

precision_label = tk.Label(
    main_frame,
    text="Decimal Places: 2",
    bg="lightgreen",
    font=("Arial", 11, "bold")
)
precision_label.pack(pady=5)

def update_precision(value):
    precision_label.config(
        text=f"Decimal Places: {int(float(value))}"
    )

precision_scale = tk.Scale(
    main_frame,
    from_=0,
    to=5,
    orient=tk.HORIZONTAL,
    resolution=1,
    variable=precision_var,
    command=update_precision,
    length=250,
    bg="lightgreen",
    highlightthickness=0
)
precision_scale.pack(pady=5)

# 8. Result
result_label = tk.Label(
    main_frame,
    text="Result:",
    font=("Arial", 14, "bold"),
    fg="#196f3d",
    bg="white",
    width=35,
    height=2,
    relief="ridge",
    bd=2
)
result_label.pack(pady=10)

# 9. Calculation History
history_frame = tk.Frame(main_frame, bg="lightgreen")
history_frame.pack(padx=20, pady=5, fill="x")

tk.Label(
    history_frame,
    text="Calculation History",
    font=("Arial", 12, "bold"),
    bg="lightgreen"
).pack(pady=5)

history_listbox = tk.Listbox(
    history_frame,
    width=45,
    height=5,
    font=("Arial", 10)
)
history_listbox.pack(pady=5)

def show_history(event):
    selected = history_listbox.curselection()

    if selected:
        result_label.config(
            text=history_listbox.get(selected[0]),
            fg="#196f3d"
        )

history_listbox.bind("<<ListboxSelect>>", show_history)

# 10. Calculator Function
def calculate():
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())

        selected = operation_combo.get()

        if selected == "Addition (+)":
            symbol = "+"
            answer = num1 + num2

        elif selected == "Subtraction (-)":
            symbol = "-"
            answer = num1 - num2

        elif selected == "Multiplication (×)":
            symbol = "*"
            answer = num1 * num2

        elif selected == "Division (÷)":
            symbol = "/"

            if num2 == 0:
                messagebox.showerror(
                    "Division Error",
                    "Cannot divide by zero!"
                )
                result_label.config(
                    text="Cannot divide by zero",
                    fg="red"
                )
                return

            answer = num1 / num2

        else:
            messagebox.showwarning(
                "Operation",
                "Please select an operation."
            )
            return

        if round_var.get():
            answer = round(answer, precision_var.get())

        calculation = f"{num1:g} {symbol} {num2:g} = {answer:g}"

        if details_var.get():
            result_label.config(
                text=calculation,
                fg="#196f3d"
            )
        else:
            result_label.config(
                text=f"Result: {answer:g}",
                fg="#196f3d"
            )

        history_listbox.insert(tk.END, calculation)

    except ValueError:
        result_label.config(
            text="Enter valid numbers",
            fg="red"
        )

        retry = messagebox.askretrycancel(
            "Invalid Input",
            "Please enter valid numbers. Would you like to try again?"
        )

        if retry:
            first_entry.focus_set()

# 11. Clear Calculator Fields
def clear_fields():
    answer = messagebox.askyesno(
        "Clear Calculator",
        "Do you want to clear all calculator fields?"
    )

    if answer:
        first_entry.delete(0, tk.END)
        second_entry.delete(0, tk.END)

        operation_combo.current(0)
        round_var.set(False)
        details_var.set(False)
        precision_scale.set(2)

        result_label.config(
            text="Result:",
            fg="#196f3d"
        )

        description_label.config(
            text="Enter two numbers and select an operation."
        )

        messagebox.showinfo(
            "Cleared",
            "Calculator fields cleared successfully!"
        )

# 12. History Functions
def remove_history():
    selected = history_listbox.curselection()

    if not selected:
        messagebox.showwarning(
            "No Selection",
            "Please select a history item to remove."
        )
        return

    answer = messagebox.askyesno(
        "Remove History",
        "Do you want to remove the selected calculation?"
    )

    if answer:
        for index in reversed(selected):
            history_listbox.delete(index)

        result_label.config(text="Result:", fg="#196f3d")
        messagebox.showinfo("Removed", "Selected history removed.")

def clear_history():
    if history_listbox.size() == 0:
        messagebox.showinfo("History", "There is no history to clear.")
        return

    answer = messagebox.askokcancel(
        "Clear History",
        "Do you want to delete all calculation history?"
    )

    if answer:
        history_listbox.delete(0, tk.END)
        result_label.config(text="Result:", fg="#196f3d")
        messagebox.showinfo("Cleared", "Calculation history cleared.")

# 13. Calculator Buttons
button_frame = tk.Frame(main_frame, bg="lightgreen")
button_frame.pack(pady=5)

tk.Button(
    button_frame,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="lightblue",
    command=calculate
).pack(side="left", padx=10)

tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 11),
    bg="orange",
    command=clear_fields
).pack(side="left", padx=10)

# 14. History Buttons
history_button_frame = tk.Frame(main_frame, bg="lightgreen")
history_button_frame.pack(pady=5)

tk.Button(
    history_button_frame,
    text="Remove Selected",
    command=remove_history
).pack(side="left", padx=5)

tk.Button(
    history_button_frame,
    text="Clear History",
    command=clear_history
).pack(side="left", padx=5)

# 15. Notes Editor
notes_frame = tk.Frame(
    main_frame,
    bg="lightgreen",
    relief="groove",
    bd=2,
    padx=10,
    pady=5
)
notes_frame.pack(padx=20, pady=5, fill="x")

tk.Label(
    notes_frame,
    text="Notes Editor",
    font=("Arial", 12, "bold"),
    bg="lightgreen"
).pack(pady=5)

notes_text = tk.Text(
    notes_frame,
    width=45,
    height=5,
    font=("Arial", 10),
    bg="white",
    fg="black",
    wrap=tk.WORD
)
notes_text.pack(pady=5)

# Notes Functions
def save_notes():
    content = notes_text.get("1.0", "end-1c")

    if not content.strip():
        messagebox.showwarning(
            "Empty Notes",
            "Please enter some notes before saving."
        )
        return

    messagebox.showinfo(
        "Notes Saved",
        "Your notes have been saved successfully!"
    )

def clear_notes():
    answer = messagebox.askyesno(
        "Clear Notes",
        "Do you want to delete all notes?"
    )

    if answer:
        notes_text.config(state=tk.NORMAL)
        notes_text.delete("1.0", tk.END)
        messagebox.showinfo("Cleared", "Notes cleared successfully.")

def lock_notes():
    notes_text.config(state=tk.DISABLED)
    messagebox.showinfo("Notes Locked", "Editing is now disabled.")

def unlock_notes():
    notes_text.config(state=tk.NORMAL)
    messagebox.showinfo("Notes Unlocked", "You can now edit your notes.")

# Notes Buttons
notes_button_frame = tk.Frame(notes_frame, bg="lightgreen")
notes_button_frame.pack(pady=5)

tk.Button(
    notes_button_frame,
    text="Save Notes",
    command=save_notes
).pack(side="left", padx=5)

tk.Button(
    notes_button_frame,
    text="Clear Notes",
    command=clear_notes
).pack(side="left", padx=5)

tk.Button(
    notes_button_frame,
    text="Lock",
    command=lock_notes
).pack(side="left", padx=5)

tk.Button(
    notes_button_frame,
    text="Unlock",
    command=unlock_notes
).pack(side="left", padx=5)

# 16. Footer and Exit Confirmation
def close_calculator():
    answer = messagebox.askokcancel(
        "Exit Calculator",
        "Are you sure you want to close the calculator?"
    )

    if answer:
        root.destroy()

footer_frame = tk.Frame(main_frame, bg="lightgreen")
footer_frame.pack(pady=10)

tk.Button(
    footer_frame,
    text="Close Calculator",
    font=("Arial", 11),
    bg="tomato",
    command=close_calculator
).pack(padx=10)

# 17. Event Loop
root.mainloop()
