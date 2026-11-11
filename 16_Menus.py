
"""
Topic: Tkinter Menus
File: 16_Menus.py
Purpose: Learn menu bars, menu commands, submenus and shortcuts.
"""

# 1. SHORT THEORY

"""
tk.Menu() creates a menu widget.

Important methods:
add_command()   - Adds a menu item.
add_cascade()   - Adds a submenu.
add_separator() - Adds a dividing line.
"""

# 2. IMPORTS

import tkinter as tk
from tkinter import messagebox

# 3. WORKING PROGRAM

root = tk.Tk()
root.title("Tkinter Menus")
root.geometry("500x400")

# Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Define functions
def new_file():
    messagebox.showinfo("New", "New file created!")

def open_file():
    messagebox.showinfo("Open", "Open file selected!")

def save_file():
    messagebox.showinfo("Save", "File saved!")

def exit_app():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()

def cut_text():
    root.focus_get().event_generate("<<Cut>>")

def copy_text():
    root.focus_get().event_generate("<<Copy>>")

def paste_text():
    root.focus_get().event_generate("<<Paste>>")

def select_all():
    text_box.tag_add("sel", "1.0", "end-1c")

def show_about():
    messagebox.showinfo("About", "Tkinter Menu Application")

# Create File menu
file_menu = tk.Menu(menu_bar, tearoff=0)

file_menu.add_command(
    label="New",
    command=new_file,
    accelerator="Ctrl+N"
)

file_menu.add_command(
    label="Open",
    command=open_file,
    accelerator="Ctrl+O"
)

file_menu.add_command(
    label="Save",
    command=save_file,
    accelerator="Ctrl+S"
)

file_menu.add_separator()

# Create submenu
export_menu = tk.Menu(file_menu, tearoff=0)

export_menu.add_command(
    label="Export as PDF",
    command=lambda: messagebox.showinfo("Export", "PDF selected")
)

export_menu.add_command(
    label="Export as Text",
    command=lambda: messagebox.showinfo("Export", "Text selected")
)

file_menu.add_cascade(
    label="Export",
    menu=export_menu
)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

# Create Edit menu
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

# Create Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)

help_menu.add_command(label="About", command=show_about)

menu_bar.add_cascade(label="Help", menu=help_menu)

# Create keyboard shortcuts
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-x>", lambda event: cut_text())
root.bind("<Control-c>", lambda event: copy_text())
root.bind("<Control-v>", lambda event: paste_text())
root.bind("<Control-a>", lambda event: select_all())

# Create text area
text_box = tk.Text(
    root,
    font=("Arial", 12),
    wrap=tk.WORD
)
text_box.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
1. tk.Menu() creates a menu.
2. root.config(menu=menu_bar) attaches the menu bar.
3. add_command() adds a menu item.
4. add_cascade() adds a submenu.
5. add_separator() creates a dividing line.
6. tearoff=0 removes the detachable menu option.
7. command connects a menu item to a function.
8. accelerator displays a keyboard shortcut.
9. bind() connects an actual keyboard shortcut.
10. Menu commands can call functions using command=.
"""
