"""
Topic: Tkinter Text Widget
File: 12_Text_Box.py
Purpose: Learn multiline text input and create a simple Notes Editor.
"""

# 1. SHORT THEORY

"""
The Text widget allows users to enter and edit multiple lines of text.

Entry: Used for single-line input.
Text: Used for multiline input.

Important methods:
insert() - Insert text
get()    - Read text
delete() - Delete text

Text indexes:
1.0 = First line, first character
end = End of text
"""

# 2. IMPORTS

import tkinter as tk

# 3. WORKING PROGRAM

root = tk.Tk()
root.title("Notes Editor")
root.geometry("500x450")

# Create Text Widget
text_box = tk.Text(
    root,
    width=45,
    height=12,
    wrap=tk.WORD,
    font=("Arial", 12),
    bg="white",
    fg="black"
)
text_box.pack(pady=15)

# Insert Text
text_box.insert("1.0", "Write your notes here...")

# Read Text
def save_notes():
    content = text_box.get("1.0", "end-1c")
    result.config(text="Notes saved!")

# Delete Text
def clear_notes():
    text_box.delete("1.0", tk.END)
    result.config(text="Notes cleared!")

# Disable Editing
def lock_notes():
    text_box.config(state=tk.DISABLED)

# Enable Editing
def unlock_notes():
    text_box.config(state=tk.NORMAL)

# Buttons
tk.Button(root, text="Save", command=save_notes).pack(pady=5)
tk.Button(root, text="Clear", command=clear_notes).pack(pady=5)
tk.Button(root, text="Lock", command=lock_notes).pack(pady=5)
tk.Button(root, text="Unlock", command=unlock_notes).pack(pady=5)

result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()

# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
1. tk.Text() creates a multiline text widget.
2. Entry is for single-line input; Text is for multiline input.
3. insert("1.0", text) inserts text at the beginning.
4. get("1.0", "end-1c") reads text without the final newline.
5. delete("1.0", tk.END) removes all text.
6. width and height control widget dimensions.
7. wrap=tk.WORD wraps text at word boundaries.
8. wrap=tk.CHAR wraps text at character boundaries.
9. state=tk.DISABLED prevents editing.
10. state=tk.NORMAL allows editing.
11. "1.0" means line 1, character 0.
12. tk.END represents the end of the text.
"""