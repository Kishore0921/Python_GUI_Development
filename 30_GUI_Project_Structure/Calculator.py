
import tkinter as tk
from tkinter import ttk

# 1. Create and configure the main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("500x750")
root.configure(bg="lightgreen")
root.resizable(True, False)
root.minsize(350, 600)
root.maxsize(800, 1000)
root.state("normal")

print("Current window state:", root.state())


# 2. Create the scrollable main area
canvas = tk.Canvas(
    root,
    bg="lightgreen",
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    root,
    orient="vertical",
    command=canvas.yview
)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Create main frame inside canvas
main_frame = tk.Frame(canvas, bg="lightgreen")

frame_window = canvas.create_window(
    (0, 0),
    window=main_frame,
    anchor="nw"
)

# Update scrollable area
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

main_frame.bind("<Configure>", update_scrollregion)

# Adjust frame width
def update_frame_width(event):
    canvas.itemconfig(frame_window, width=event.width)

canvas.bind("<Configure>", update_frame_width)

# Mouse wheel scrolling
def mouse_scroll(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", mouse_scroll)


# 3. Create the header frame
header_frame = tk.Frame(main_frame, bg="lightgreen")
header_frame.pack(fill="x", padx=10, pady=5)

title_label = tk.Label(
    header_frame,
    text="Python GUI Calculator",
    font=("Arial", 20, "bold"),
    fg="#154360",
    bg="lightgreen",
    padx=10,
    pady=10
)
title_label.pack(pady=5)

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


# 4. Create the input frame
input_frame = tk.Frame(
    main_frame,
    bg="lightgreen",
    padx=10,
    pady=5
)
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


# 5. Create the dropdown operation frame
operation_frame = tk.Frame(
    main_frame,
    bg="lightgreen",
    relief="groove",
    bd=2,
    padx=10,
    pady=10
)
operation_frame.pack(pady=5)

tk.Label(
    operation_frame,
    text="Select Operation:",
    font=("Arial", 11, "bold"),
    bg="lightgreen"
).pack(pady=5)

operations = [
    "Addition (+)",
    "Subtraction (-)",
    "Multiplication (×)",
    "Division (÷)"
]

operation_combo = ttk.Combobox(
    operation_frame,
    values=operations,
    font=("Arial", 10),
    width=25,
    state="readonly"
)
operation_combo.pack(pady=5)
operation_combo.current(0)


# 6. Create the checkbutton frame
options_frame = tk.Frame(main_frame, bg="lightgreen")
options_frame.pack(pady=5)

round_var = tk.BooleanVar()
details_var = tk.BooleanVar()

tk.Checkbutton(
    options_frame,
    text="Round Result",
    variable=round_var,
    bg="lightgreen",
    font=("Arial", 10)
).pack(side="left", padx=10)

tk.Checkbutton(
    options_frame,
    text="Show Calculation",
    variable=details_var,
    bg="lightgreen",
    font=("Arial", 10)
).pack(side="left", padx=10)


# 7. Create the result label
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


# 8. Create the calculation history Listbox
history_frame = tk.Frame(
    main_frame,
    bg="lightgreen",
    relief="groove",
    bd=2,
    padx=10,
    pady=5
)
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
    font=("Arial", 10),
    selectmode=tk.SINGLE
)
history_listbox.pack(pady=5)


def show_history(event):
    selected_indexes = history_listbox.curselection()

    if selected_indexes:
        selected_calculation = history_listbox.get(selected_indexes[0])

        result_label.config(
            text=selected_calculation,
            fg="#196f3d"
        )


history_listbox.bind("<<ListboxSelect>>", show_history)


# 9. Define the calculator function
def calculate():
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())

        selected_operation = operation_combo.get()

        if selected_operation == "Addition (+)":
            operation = "+"
            result = num1 + num2

        elif selected_operation == "Subtraction (-)":
            operation = "-"
            result = num1 - num2

        elif selected_operation == "Multiplication (×)":
            operation = "*"
            result = num1 * num2

        elif selected_operation == "Division (÷)":
            operation = "/"

            if num2 == 0:
                result_label.config(
                    text="Cannot divide by zero",
                    fg="red"
                )
                return

            result = num1 / num2

        else:
            result_label.config(
                text="Please select an operation",
                fg="red"
            )
            return

        if round_var.get():
            result = round(result, 2)

        calculation = f"{num1:g} {operation} {num2:g} = {result:g}"

        if details_var.get():
            result_label.config(
                text=calculation,
                fg="#196f3d"
            )
        else:
            result_label.config(
                text=f"Result: {result:g}",
                fg="#196f3d"
            )

        history_listbox.insert(tk.END, calculation)

    except ValueError:
        result_label.config(
            text="Enter valid numbers",
            fg="red"
        )


# 10. Define the clear function
def clear_fields():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)

    operation_combo.current(0)

    round_var.set(False)
    details_var.set(False)

    result_label.config(
        text="Result:",
        fg="#196f3d"
    )

    description_label.config(
        text="Enter two numbers and select an operation."
    )


def remove_history():
    selected_indexes = history_listbox.curselection()

    for index in reversed(selected_indexes):
        history_listbox.delete(index)

    result_label.config(
        text="Result:",
        fg="#196f3d"
    )


def clear_history():
    history_listbox.delete(0, tk.END)

    result_label.config(
        text="Result:",
        fg="#196f3d"
    )


# 11. Create the button frame
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


# 12. Create the history button frame
history_button_frame = tk.Frame(main_frame, bg="lightgreen")
history_button_frame.pack(pady=5)

tk.Button(
    history_button_frame,
    text="Remove Selected",
    font=("Arial", 10),
    command=remove_history
).pack(side="left", padx=5)

tk.Button(
    history_button_frame,
    text="Clear History",
    font=("Arial", 10),
    command=clear_history
).pack(side="left", padx=5)


# 13. Create the Text Box Notes Editor
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

# Create Text Widget
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

    result_label.config(
        text="Notes saved!",
        fg="#196f3d"
    )


def clear_notes():
    notes_text.config(state=tk.NORMAL)
    notes_text.delete("1.0", tk.END)


def lock_notes():
    notes_text.config(state=tk.DISABLED)


def unlock_notes():
    notes_text.config(state=tk.NORMAL)


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


# 14. Create the footer frame
footer_frame = tk.Frame(main_frame, bg="lightgreen")
footer_frame.pack(pady=10)

tk.Button(
    footer_frame,
    text="Close Calculator",
    font=("Arial", 11),
    bg="tomato",
    command=root.destroy
).pack(padx=10)


# 15. Start the Tkinter event loop
root.mainloop()
