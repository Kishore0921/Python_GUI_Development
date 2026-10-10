
"""
Topic: Tkinter Basics
File: 01_Tkinter_Basics.py
Purpose: Understand Tkinter and create a basic GUI window
         using Python.
"""

# ============================================================
# 1. SHORT THEORY
# ============================================================

"""
Tkinter is Python's standard library for developing
Graphical User Interface (GUI) applications.

It allows developers to create desktop applications
with windows and interactive graphical components.

Why is Tkinter used?
- To develop desktop GUI applications.
- To create graphical interfaces instead of terminal-based
  interfaces.
- To build applications that run on supported desktop
  operating systems.

Important Terminology:
- GUI: Graphical User Interface.
- Window: The main visual area of an application.
- Root Window: The primary application window.
- Event Loop: Processes events and keeps the window responsive.
- Widget: A graphical component used in a GUI.

Advantages of Tkinter:
- Included with most standard Python installations.
- Easy to learn and beginner-friendly.
- Cross-platform support: Windows, macOS, and Linux.
- Supports interactive desktop application development.
- Provides built-in widgets for creating GUI components.

Common Uses:
- Calculator applications.
- Student management systems.
- Personal expense trackers.
- Data-entry forms.
- Small desktop productivity tools.

Basic Application Structure:
1. Import the Tkinter library.
2. Create the root window.
3. Configure the window properties.
4. Add widgets when required.
5. Start the event loop using mainloop().
"""


# ============================================================
# 2. IMPORTS
# ============================================================

import tkinter as tk

# tkinter: Python's standard GUI library.
# tk: Alias used to access Tkinter classes and methods.


# ============================================================
# 3. WORKING EXAMPLE — CREATE A BASIC WINDOW
# ============================================================

# Create the main application window.
root = tk.Tk()

# Set the window title.
root.title("My First Tkinter Window")

# Set the initial window size (width x height).
root.geometry("600x400")

# Set the background color.
root.configure(bg="lightblue")

# Set the minimum window dimensions.
root.minsize(300, 200)

# Set the maximum window dimensions.
root.maxsize(1000, 700)

# Start the event loop.
root.mainloop()


# ============================================================
# 4. IMPORTANT THINGS TO BE MEMORIZED
# ============================================================

"""
Syntax                      Meaning
------------------------------------------------------------
import tkinter as tk        Import the Tkinter library
tk.Tk()                     Create the root window
root.title()                Set the window title
root.geometry()             Set the initial window size
root.configure()            Configure window properties
root.minsize()              Set minimum window dimensions
root.maxsize()              Set maximum window dimensions
root.mainloop()             Start the GUI event loop

Important Rules:
1. Import Tkinter before using its classes.
2. Create the root window using tk.Tk().
3. Configure the window before starting the event loop.
4. Call mainloop() to keep the application responsive.
5. Use only one Tk() root window for a basic application.
"""
