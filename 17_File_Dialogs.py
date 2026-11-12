
"""
Topic: File Dialogs
File: 17_File_Dialogs.py
Purpose: Learn to open, save, and select files and folders using Tkinter.
"""

# 1. SHORT THEORY

"""
File dialogs allow users to select files and folders through
the operating system's file selection window.

Important functions:
- askopenfilename()      : Select an existing file.
- asksaveasfilename()    : Select a location and name for saving.
- askdirectory()         : Select a folder.

Important concepts:
- filetypes: Filters the files displayed in the dialog.
- defaultextension: Adds an extension if the user does not provide one.
- Initial directory: Sets the folder displayed when the dialog opens.
- Cancellation: Returns an empty string when the user cancels.
"""

# 2. IMPORTS

import tkinter as tk
from tkinter import filedialog, messagebox

# 3. MAIN WINDOW

root = tk.Tk()
root.title("Tkinter File Dialogs")
root.geometry("550x500")
root.configure(bg="lightblue")

# 4. FILE FUNCTIONS

def open_file():
    file_path = filedialog.askopenfilename(
        title="Open Text File",
        filetypes=[
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", content)
        path_label.config(text=f"Opened: {file_path}")

    except OSError as error:
        messagebox.showerror("Open Error", str(error))


def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Save Text File",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:
        content = text_area.get("1.0", "end-1c")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        path_label.config(text=f"Saved: {file_path}")
        messagebox.showinfo("Saved", "File saved successfully.")

    except OSError as error:
        messagebox.showerror("Save Error", str(error))


def select_folder():
    folder_path = filedialog.askdirectory(
        title="Select a Folder"
    )

    if folder_path:
        path_label.config(text=f"Folder: {folder_path}")


# 5. WIDGETS

tk.Label(
    root,
    text="File Dialog Example",
    font=("Arial", 18, "bold"),
    bg="lightblue"
).pack(pady=15)

button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Open File",
    command=open_file
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Save File",
    command=save_file
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Select Folder",
    command=select_folder
).pack(side="left", padx=5)

text_area = tk.Text(
    root,
    width=55,
    height=15,
    wrap=tk.WORD
)
text_area.pack(padx=15, pady=10)

path_label = tk.Label(
    root,
    text="No file selected",
    bg="lightblue",
    wraplength=500
)
path_label.pack(pady=5)

# 6. EVENT LOOP

root.mainloop()
