
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

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

# 3. Calculator and Menu Functions

def new_calculation():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    operation_combo.current(0)
    quantity_var.set("1")
    round_var.set(False)
    details_var.set(False)
    precision_scale.set(2)
    result_label.config(text="Result:", fg="#196f3d")


def open_notes():
    file_path = filedialog.askopenfilename(
        title="Open Notes",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        notes_text.config(state=tk.NORMAL)
        notes_text.delete("1.0", tk.END)
        notes_text.insert("1.0", content)

        messagebox.showinfo("Opened", "Notes opened successfully.")

    except OSError as error:
        messagebox.showerror("Open Error", str(error))


def save_notes():
    content = notes_text.get("1.0", "end-1c")

    if not content.strip():
        messagebox.showwarning("Empty Notes", "Enter notes before saving.")
        return

    file_path = filedialog.asksaveasfilename(
        title="Save Notes",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        messagebox.showinfo("Saved", "Notes saved successfully.")

    except OSError as error:
        messagebox.showerror("Save Error", str(error))


def select_folder():
    folder_path = filedialog.askdirectory(
        title="Select a Folder"
    )

    if folder_path:
        messagebox.showinfo("Selected Folder", folder_path)


def select_all():
    notes_text.tag_add("sel", "1.0", "end-1c")
    notes_text.mark_set("insert", "1.0")
    notes_text.focus_set()


def cut_text():
    notes_text.event_generate("<<Cut>>")


def copy_text():
    notes_text.event_generate("<<Copy>>")


def paste_text():
    notes_text.event_generate("<<Paste>>")


def clear_history():
    if history_listbox.size() == 0:
        messagebox.showinfo("History", "No history to clear.")
        return

    if messagebox.askyesno("Clear History", "Delete all calculation history?"):
        history_listbox.delete(0, tk.END)


def close_calculator():
    if messagebox.askyesno("Exit", "Do you want to close the calculator?"):
        root.destroy()


# 4. Menu Bar

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File Menu

file_menu = tk.Menu(menu_bar, tearoff=0)

file_menu.add_command(
    label="New Calculation",
    command=new_calculation,
    accelerator="Ctrl+N"
)

file_menu.add_command(
    label="Open Notes",
    command=open_notes,
    accelerator="Ctrl+O"
)

file_menu.add_command(
    label="Save Notes",
    command=save_notes,
    accelerator="Ctrl+S"
)

file_menu.add_command(
    label="Select Folder",
    command=select_folder
)

file_menu.add_separator()

# Export Submenu

export_menu = tk.Menu(file_menu, tearoff=0)

export_menu.add_command(
    label="Export Notes",
    command=save_notes
)

file_menu.add_cascade(label="Export", menu=export_menu)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=close_calculator)

menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu

edit_menu = tk.Menu(menu_bar, tearoff=0)

edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")

edit_menu.add_separator()

edit_menu.add_command(
    label="Select All",
    command=select_all,
    accelerator="Ctrl+A"
)

menu_bar.add_cascade(label="Edit", menu=edit_menu)

# View Menu

view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Clear History", command=clear_history)

menu_bar.add_cascade(label="View", menu=view_menu)

# Help Menu

help_menu = tk.Menu(menu_bar, tearoff=0)

help_menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo(
        "About",
        "Python GUI Calculator\nBuilt using Tkinter."
    )
)

menu_bar.add_cascade(label="Help", menu=help_menu)

# Keyboard Shortcuts

root.bind("<Control-n>", lambda event: new_calculation())
root.bind("<Control-o>", lambda event: open_notes())
root.bind("<Control-s>", lambda event: save_notes())
root.bind("<Control-x>", lambda event: cut_text())
root.bind("<Control-c>", lambda event: copy_text())
root.bind("<Control-v>", lambda event: paste_text())
root.bind("<Control-a>", lambda event: select_all())

# 5. Header

header_frame = tk.Frame(main_frame, bg="lightgreen")
header_frame.pack(fill="x", padx=10, pady=5)

tk.Label(
    header_frame,
    text="Python GUI Calculator",
    font=("Arial", 20, "bold"),
    fg="#154360",
    bg="lightgreen"
).pack(pady=10)

description_label = tk.Label(
    header_frame,
    text="Enter two numbers and select an operation.",
    bg="white",
    font=("Arial", 11),
    padx=10,
    pady=5
)
description_label.pack(pady=5)

# 6. Input Fields

input_frame = tk.Frame(main_frame, bg="lightgreen")
input_frame.pack(pady=10)

tk.Label(
    input_frame,
    text="First Number:",
    bg="lightgreen"
).grid(row=0, column=0, padx=5, pady=5)

first_entry = tk.Entry(input_frame, width=25, justify="center")
first_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(
    input_frame,
    text="Second Number:",
    bg="lightgreen"
).grid(row=1, column=0, padx=5, pady=5)

second_entry = tk.Entry(input_frame, width=25, justify="center")
second_entry.grid(row=1, column=1, padx=5, pady=5)

# 7. Operation Dropdown

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

# 8. Spinbox - Quantity

tk.Label(
    main_frame,
    text="Select Quantity:",
    bg="lightgreen"
).pack(pady=5)

quantity_var = tk.StringVar(value="1")

quantity_spinbox = tk.Spinbox(
    main_frame,
    from_=1,
    to=20,
    textvariable=quantity_var,
    width=10
)
quantity_spinbox.pack(pady=5)

# 9. Checkbuttons

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

# 10. Scale - Precision

precision_var = tk.IntVar(value=2)

precision_label = tk.Label(
    main_frame,
    text="Decimal Places: 2",
    bg="lightgreen"
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

# 11. Result

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

# 12. Calculation History

tk.Label(
    main_frame,
    text="Calculation History",
    font=("Arial", 12, "bold"),
    bg="lightgreen"
).pack(pady=5)

history_listbox = tk.Listbox(main_frame, width=45, height=5)
history_listbox.pack(pady=5)


def show_history(event):
    selected = history_listbox.curselection()

    if selected:
        result_label.config(
            text=history_listbox.get(selected[0]),
            fg="#196f3d"
        )


history_listbox.bind("<<ListboxSelect>>", show_history)

# 13. Calculator Function

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
                messagebox.showerror("Error", "Cannot divide by zero!")
                return

            answer = num1 / num2

        else:
            messagebox.showwarning("Warning", "Select an operation.")
            return

        answer *= quantity

        if round_var.get():
            answer = round(answer, precision_var.get())

        calculation = (
            f"({num1:g} {symbol} {num2:g}) × {quantity} = {answer:g}"
        )

        if details_var.get():
            result_label.config(text=calculation, fg="#196f3d")
        else:
            result_label.config(
                text=f"Result: {answer:g}",
                fg="#196f3d"
            )

        history_listbox.insert(tk.END, calculation)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Enter valid numbers and quantity."
        )


# 14. Clear and History Functions

def clear_fields():
    if messagebox.askyesno("Clear", "Clear calculator fields?"):
        new_calculation()


def remove_history():
    selected = history_listbox.curselection()

    if not selected:
        messagebox.showwarning(
            "Selection",
            "Select a history item first."
        )
        return

    if messagebox.askyesno("Remove", "Remove selected calculation?"):
        for index in reversed(selected):
            history_listbox.delete(index)


# 15. Calculator Buttons

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

# 16. Notes Editor

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
    wrap=tk.WORD,
    font=("Arial", 10)
)
notes_text.pack(pady=5)


def clear_notes():
    if messagebox.askyesno("Clear Notes", "Delete all notes?"):
        notes_text.config(state=tk.NORMAL)
        notes_text.delete("1.0", tk.END)


def lock_notes():
    notes_text.config(state=tk.DISABLED)


def unlock_notes():
    notes_text.config(state=tk.NORMAL)


notes_buttons = tk.Frame(notes_frame, bg="lightgreen")
notes_buttons.pack(pady=5)

tk.Button(
    notes_buttons,
    text="Open Notes",
    command=open_notes
).pack(side="left", padx=3)

tk.Button(
    notes_buttons,
    text="Save Notes",
    command=save_notes
).pack(side="left", padx=3)

tk.Button(
    notes_buttons,
    text="Clear Notes",
    command=clear_notes
).pack(side="left", padx=3)

tk.Button(
    notes_buttons,
    text="Lock",
    command=lock_notes
).pack(side="left", padx=3)

tk.Button(
    notes_buttons,
    text="Unlock",
    command=unlock_notes
).pack(side="left", padx=3)

# 17. Footer

tk.Button(
    main_frame,
    text="Close Calculator",
    bg="tomato",
    command=close_calculator
).pack(pady=15)

# 18. Event Loop

root.mainloop()
