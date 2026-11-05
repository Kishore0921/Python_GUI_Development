import tkinter as tk
from tkinter import ttk

# 1. Create and configure the main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("500x750")
root.configure(bg="lightgreen")
root.resizable(True, False)
root.minsize(350, 600)
root.maxsize(800, 900)
root.state("normal")

print("Current window state:", root.state())


# 2. Create the header frame
header_frame = tk.Frame(root, bg="lightgreen")
header_frame.pack(fill="x", padx=10, pady=5)

# Create the title label
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

# Create the description label
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


# 3. Create the input frame
input_frame = tk.Frame(
    root,
    bg="lightgreen",
    padx=10,
    pady=5
)
input_frame.pack(pady=5)

# First number label and entry field
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

# Second number label and entry field
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


# 4. Create the dropdown operation frame
operation_frame = tk.Frame(
    root,
    bg="lightgreen",
    relief="groove",
    bd=2,
    padx=10,
    pady=10
)
operation_frame.pack(pady=5)

# Create the operation label
tk.Label(
    operation_frame,
    text="Select Operation:",
    font=("Arial", 11, "bold"),
    bg="lightgreen"
).pack(pady=5)

# Define dropdown operation values
operations = [
    "Addition (+)",
    "Subtraction (-)",
    "Multiplication (×)",
    "Division (÷)"
]

# Create the Combobox
operation_combo = ttk.Combobox(
    operation_frame,
    values=operations,
    font=("Arial", 10),
    width=25,
    state="readonly"
)
operation_combo.pack(pady=5)

# Select Addition by default
operation_combo.current(0)


# 5. Create the checkbutton frame
options_frame = tk.Frame(root, bg="lightgreen")
options_frame.pack(pady=5)

# Create Boolean variables
round_var = tk.BooleanVar()
details_var = tk.BooleanVar()

# Create Round Result checkbutton
tk.Checkbutton(
    options_frame,
    text="Round Result",
    variable=round_var,
    bg="lightgreen",
    font=("Arial", 10)
).pack(side="left", padx=10)

# Create Show Calculation checkbutton
tk.Checkbutton(
    options_frame,
    text="Show Calculation",
    variable=details_var,
    bg="lightgreen",
    font=("Arial", 10)
).pack(side="left", padx=10)


# 6. Create the result label
result_label = tk.Label(
    root,
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


# 7. Create the calculation history Listbox
history_frame = tk.Frame(
    root,
    bg="lightgreen",
    relief="groove",
    bd=2,
    padx=10,
    pady=5
)
history_frame.pack(padx=20, pady=5, fill="x")

# Create history label
tk.Label(
    history_frame,
    text="Calculation History",
    font=("Arial", 12, "bold"),
    bg="lightgreen"
).pack(pady=5)

# Create Listbox
history_listbox = tk.Listbox(
    history_frame,
    width=45,
    height=5,
    font=("Arial", 10),
    selectmode=tk.SINGLE
)
history_listbox.pack(pady=5)


# Define function to display selected history
def show_history(event):
    selected_indexes = history_listbox.curselection()

    if selected_indexes:
        selected_calculation = history_listbox.get(selected_indexes[0])

        result_label.config(
            text=selected_calculation,
            fg="#196f3d"
        )


# Connect Listbox selection event
history_listbox.bind(
    "<<ListboxSelect>>",
    show_history
)


# 8. Define the calculator function
def calculate():
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())

        # Retrieve selected operation from dropdown
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

        # Round the result if selected
        if round_var.get():
            result = round(result, 2)

        # Create calculation text
        calculation = f"{num1:g} {operation} {num2:g} = {result:g}"

        # Display the calculation if selected
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

        # Add calculation to history
        history_listbox.insert(tk.END, calculation)

    except ValueError:
        result_label.config(
            text="Enter valid numbers",
            fg="red"
        )


# 9. Define the clear function
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


# Define function to remove selected history
def remove_history():
    selected_indexes = history_listbox.curselection()

    for index in reversed(selected_indexes):
        history_listbox.delete(index)

    result_label.config(
        text="Result:",
        fg="#196f3d"
    )


# Define function to clear all history
def clear_history():
    history_listbox.delete(0, tk.END)

    result_label.config(
        text="Result:",
        fg="#196f3d"
    )


# 10. Create the button frame
button_frame = tk.Frame(root, bg="lightgreen")
button_frame.pack(pady=5)

# Create the Calculate button
calculate_button = tk.Button(
    button_frame,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="lightblue",
    command=calculate
)
calculate_button.pack(side="left", padx=10)

# Create the Clear button
clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 11),
    bg="orange",
    command=clear_fields
)
clear_button.pack(side="left", padx=10)


# 11. Create the history button frame
history_button_frame = tk.Frame(root, bg="lightgreen")
history_button_frame.pack(pady=5)

# Create the remove history button
remove_button = tk.Button(
    history_button_frame,
    text="Remove Selected",
    font=("Arial", 10),
    command=remove_history
)
remove_button.pack(side="left", padx=5)

# Create the clear history button
clear_history_button = tk.Button(
    history_button_frame,
    text="Clear History",
    font=("Arial", 10),
    command=clear_history
)
clear_history_button.pack(side="left", padx=5)


# 12. Create the footer frame
footer_frame = tk.Frame(root, bg="lightgreen")
footer_frame.pack(pady=5)

# Create the Close button
close_button = tk.Button(
    footer_frame,
    text="Close Calculator",
    font=("Arial", 11),
    bg="tomato",
    command=root.destroy
)
close_button.pack(padx=10)


# 13. Start the Tkinter event loop
root.mainloop()