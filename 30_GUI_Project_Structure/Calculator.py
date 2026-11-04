import tkinter as tk
from tkinter import ttk

# 1. Create and configure the main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("500x650")
root.configure(bg="lightgreen")
root.resizable(True, False)
root.minsize(350, 450)
root.maxsize(800, 800)
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


# 7. Define the calculator function
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

        # Display the calculation if selected
        if details_var.get():
            result_label.config(
                text=f"{num1:g} {operation} {num2:g} = {result:g}",
                fg="#196f3d"
            )
        else:
            result_label.config(
                text=f"Result: {result:g}",
                fg="#196f3d"
            )

    except ValueError:
        result_label.config(
            text="Enter valid numbers",
            fg="red"
        )


# 8. Define the clear function
def clear_fields():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)

    # Reset dropdown to Addition
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


# 9. Create the button frame
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
    font=("Arial", 11, "bold"),
    bg="orange",
    command=clear_fields
)
clear_button.pack(side="left", padx=10)


# 10. Create the footer frame
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


# 11. Start the Tkinter event loop
root.mainloop()