
import tkinter as tk
from tkinter import ttk

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
tk.Label(
    main_frame,
    text="Python GUI Calculator",
    font=("Arial", 20, "bold"),
    fg="#154360",
    bg="lightgreen"
).pack(pady=10)

tk.Label(
    main_frame,
    text="Enter numbers and select an operation.",
    bg="white",
    font=("Arial", 11),
    padx=10,
    pady=5
).pack(pady=5)

# 4. Input Fields
input_frame = tk.Frame(main_frame, bg="lightgreen")
input_frame.pack(pady=10)

tk.Label(input_frame, text="First Number:", bg="lightgreen").grid(
    row=0, column=0, padx=5, pady=5
)

first_entry = tk.Entry(input_frame, width=25, justify="center")
first_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Second Number:", bg="lightgreen").grid(
    row=1, column=0, padx=5, pady=5
)

second_entry = tk.Entry(input_frame, width=25, justify="center")
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
    state="readonly",
    width=25
)
operation_combo.pack(pady=10)
operation_combo.current(0)

# 6. Quantity Spinbox
tk.Label(
    main_frame,
    text="Select Quantity:",
    bg="lightgreen",
    font=("Arial", 11, "bold")
).pack(pady=5)

quantity_var = tk.StringVar(value="1")

quantity_spinbox = tk.Spinbox(
    main_frame,
    from_=1,
    to=20,
    increment=1,
    textvariable=quantity_var,
    width=10
)
quantity_spinbox.pack(pady=5)

# 7. Checkbuttons
round_var = tk.BooleanVar()
details_var = tk.BooleanVar()

options_frame = tk.Frame(main_frame, bg="lightgreen")
options_frame.pack(pady=5)

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

# 8. Result
result_label = tk.Label(
    main_frame,
    text="Result:",
    font=("Arial", 14, "bold"),
    fg="#196f3d",
    bg="white",
    width=35,
    height=2,
    relief="ridge"
)
result_label.pack(pady=10)

# 9. Calculation History
tk.Label(
    main_frame,
    text="Calculation History",
    font=("Arial", 12, "bold"),
    bg="lightgreen"
).pack(pady=5)

history_listbox = tk.Listbox(
    main_frame,
    width=45,
    height=5
)
history_listbox.pack(pady=5)

def show_history(event):
    selected = history_listbox.curselection()

    if selected:
        result_label.config(
            text=history_listbox.get(selected[0])
        )

history_listbox.bind("<<ListboxSelect>>", show_history)

# 10. Calculator Function
def calculate():
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())
        quantity = int(quantity_spinbox.get())

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
                result_label.config(text="Cannot divide by zero", fg="red")
                return

            answer = num1 / num2

        else:
            result_label.config(text="Select an operation", fg="red")
            return

        answer *= quantity

        if round_var.get():
            answer = round(answer, 2)

        calculation = (
            f"({num1:g} {symbol} {num2:g}) × {quantity} = {answer:g}"
        )

        if details_var.get():
            result_label.config(text=calculation, fg="#196f3d")
        else:
            result_label.config(text=f"Result: {answer:g}", fg="#196f3d")

        history_listbox.insert(tk.END, calculation)

    except ValueError:
        result_label.config(text="Enter valid values", fg="red")

# 11. Clear Functions
def clear_fields():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)

    operation_combo.current(0)
    quantity_var.set("1")
    round_var.set(False)
    details_var.set(False)

    result_label.config(text="Result:", fg="#196f3d")

def remove_history():
    for index in reversed(history_listbox.curselection()):
        history_listbox.delete(index)

def clear_history():
    history_listbox.delete(0, tk.END)

# 12. Calculator Buttons
button_frame = tk.Frame(main_frame, bg="lightgreen")
button_frame.pack(pady=5)

tk.Button(
    button_frame,
    text="Calculate",
    command=calculate,
    bg="lightblue"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    bg="orange"
).pack(side="left", padx=5)

history_buttons = tk.Frame(main_frame, bg="lightgreen")
history_buttons.pack(pady=5)

tk.Button(
    history_buttons,
    text="Remove Selected",
    command=remove_history
).pack(side="left", padx=5)

tk.Button(
    history_buttons,
    text="Clear History",
    command=clear_history
).pack(side="left", padx=5)

# 13. Notes Editor
tk.Label(
    main_frame,
    text="Notes Editor",
    font=("Arial", 12, "bold"),
    bg="lightgreen"
).pack(pady=5)

notes_text = tk.Text(
    main_frame,
    width=45,
    height=5,
    wrap=tk.WORD,
    font=("Arial", 10)
)
notes_text.pack(pady=5)

def save_notes():
    content = notes_text.get("1.0", "end-1c")
    result_label.config(text="Notes saved!", fg="#196f3d")

def clear_notes():
    notes_text.config(state=tk.NORMAL)
    notes_text.delete("1.0", tk.END)

def lock_notes():
    notes_text.config(state=tk.DISABLED)

def unlock_notes():
    notes_text.config(state=tk.NORMAL)

notes_buttons = tk.Frame(main_frame, bg="lightgreen")
notes_buttons.pack(pady=5)

tk.Button(notes_buttons, text="Save", command=save_notes).pack(side="left", padx=3)
tk.Button(notes_buttons, text="Clear", command=clear_notes).pack(side="left", padx=3)
tk.Button(notes_buttons, text="Lock", command=lock_notes).pack(side="left", padx=3)
tk.Button(notes_buttons, text="Unlock", command=unlock_notes).pack(side="left", padx=3)

# 14. Footer
tk.Button(
    main_frame,
    text="Close Calculator",
    bg="tomato",
    command=root.destroy
).pack(pady=15)

# 15. Event Loop
root.mainloop()
