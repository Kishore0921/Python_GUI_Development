
import tkinter as tk

# 1. Create and configure the main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("500x550")
root.configure(bg="lightgreen")
root.resizable(True, False)
root.minsize(350, 450)
root.maxsize(800, 800)
root.state("normal")

print("Current window state:", root.state())


# 2. Create the title label
title_label = tk.Label(
    root,
    text="Python GUI Calculator",
    font=("Arial", 20, "bold"),
    fg="#154360",
    bg="lightgreen",
    padx=10,
    pady=10
)
title_label.pack(pady=10)


# 3. Create the description label
description_label = tk.Label(
    root,
    text="Enter two numbers and select an operation.",
    font=("Times New Roman", 12),
    fg="#212f3c",
    bg="white",
    width=40,
    height=2,
    relief="sunken",
    bd=2,
    wraplength=350,
    padx=10,
    pady=5
)
description_label.pack(pady=5)


# 4. Create the entry fields
tk.Label(
    root,
    text="First Number:",
    font=("Arial", 11),
    bg="lightgreen"
).pack(pady=(10, 2))

first_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    justify="center"
)
first_entry.pack(pady=5)

tk.Label(
    root,
    text="Second Number:",
    font=("Arial", 11),
    bg="lightgreen"
).pack(pady=(5, 2))

second_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    justify="center"
)
second_entry.pack(pady=5)


# 5. Create the result label
result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 14, "bold"),
    fg="#196f3d",
    bg="white",
    width=30,
    height=2,
    relief="ridge",
    bd=2
)
result_label.pack(pady=12)


# 6. Define the calculator function
def calculate(operation):
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(
                    text="Error: Cannot divide by zero",
                    fg="red"
                )
                return
            result = num1 / num2

        result_label.config(
            text=f"Result: {result:g}",
            fg="#196f3d"
        )

    except ValueError:
        result_label.config(
            text="Please enter valid numbers",
            fg="red"
        )


# 7. Define the clear function
def clear_fields():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    result_label.config(text="Result: ", fg="#196f3d")
    description_label.config(
        text="Enter two numbers and select an operation."
    )


# 8. Create operation buttons using grid()
button_frame = tk.Frame(root, bg="lightgreen")
button_frame.pack(pady=5)

operations = [
    ("+", lambda: calculate("+")),
    ("-", lambda: calculate("-")),
    ("×", lambda: calculate("*")),
    ("÷", lambda: calculate("/"))
]

for column, (symbol, action) in enumerate(operations):
    tk.Button(
        button_frame,
        text=symbol,
        font=("Arial", 14, "bold"),
        width=5,
        bg="lightblue",
        command=action
    ).grid(row=0, column=column, padx=5, pady=5)

# Clear button
clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 11, "bold"),
    bg="orange",
    command=clear_fields
)
clear_button.pack(pady=5)

# Close button
close_button = tk.Button(
    root,
    text="Close Calculator",
    font=("Arial", 11),
    bg="tomato",
    command=root.destroy
)
close_button.pack(pady=5)


# 9. Start the Tkinter event loop
root.mainloop()
