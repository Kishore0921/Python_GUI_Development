
"""
Topic: Multiple Windows in Tkinter
File: 20_Multiple_Windows.py
Purpose: Create and manage secondary windows using Toplevel().
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

settings_window = None

# 1. FUNCTION TO OPEN SETTINGS WINDOW
def open_settings():
    global settings_window

    # Prevent duplicate windows
    if settings_window is not None and settings_window.winfo_exists():
        settings_window.lift()
        settings_window.focus_force()
        return

    # Create a child window
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("300x220")
    settings_window.resizable(False, False)

    # Make it behave like a dialog
    settings_window.transient(root)
    settings_window.grab_set()

    tk.Label(
        settings_window,
        text="Settings Window",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    # Data shared with the main window
    name_var = tk.StringVar(value=name_entry.get())

    tk.Label(settings_window, text="Enter your name:").pack()
    name_input = tk.Entry(settings_window, textvariable=name_var)
    name_input.pack(pady=5)

    # 2. PASS DATA BACK TO MAIN WINDOW
    def save_settings():
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name_var.get())

        close_settings()

    # 3. CLOSE SECONDARY WINDOW
    def close_settings():
        global settings_window
        settings_window.grab_release()
        settings_window.destroy()
        settings_window = None

    tk.Button(
        settings_window,
        text="Save",
        command=save_settings
    ).pack(pady=10)

    tk.Button(
        settings_window,
        text="Close",
        command=close_settings
    ).pack()

    settings_window.protocol("WM_DELETE_WINDOW", close_settings)


# 4. MAIN WINDOW WIDGETS
tk.Label(
    root,
    text="Main Application",
    font=("Arial", 18, "bold")
).pack(pady=20)

tk.Label(root, text="Your Name:").pack()

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Button(
    root,
    text="Open Settings",
    command=open_settings
).pack(pady=15)

root.mainloop()
