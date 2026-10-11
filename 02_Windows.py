
"""
Topic: Tkinter Windows
File: 02_Windows.py
Purpose: Learn how to create, configure, resize, position,
         minimize, maximize, and close Tkinter windows.
"""

# ============================================================
# 1. SHORT THEORY
# ============================================================

"""
A window is the main visual container of a Tkinter application.
It provides the area where GUI components can be displayed.

Important Window Methods:

1. title()       - Sets the window title.
2. geometry()    - Sets window dimensions and screen position.
3. resizable()   - Controls whether the window can be resized.
4. minsize()     - Sets the minimum window dimensions.
5. maxsize()     - Sets the maximum window dimensions.
6. configure()   - Changes window properties.
7. config()      - Alternative name for configure().
8. state()       - Gets or changes the window's display state.
9. iconbitmap()  - Sets the window icon using an ICO file.
10. destroy()    - Closes and destroys the window.

Window States:
- normal: Window displayed normally.
- iconic: Window minimized.
- zoomed: Window maximized on supported platforms.
"""


# ============================================================
# 2. IMPORTS
# ============================================================

import tkinter as tk

# tkinter is Python's standard GUI library.
# tk is an alias used to access Tkinter classes and methods.


# ============================================================
# 3. WORKING EXAMPLE — WINDOW MANAGEMENT
# ============================================================

# Create the main application window.
root = tk.Tk()

# ------------------------------------------------------------
# A. TITLE
# ------------------------------------------------------------

root.title("Tkinter Window Management")

# ------------------------------------------------------------
# B. WIDTH, HEIGHT AND POSITION
# ------------------------------------------------------------

# Format: "widthxheight+x_position+y_position"
root.geometry("700x450+100+80")

# Width  = 700 pixels
# Height = 450 pixels
# X      = 100 pixels from the left of the screen
# Y      = 80 pixels from the top of the screen

# ------------------------------------------------------------
# C. RESIZABLE WINDOW
# ------------------------------------------------------------

# Allow resizing in both directions.
root.resizable(True, True)

# Other possible configurations:
# root.resizable(False, False)  # Disable all resizing
# root.resizable(True, False)   # Allow width resizing only
# root.resizable(False, True)   # Allow height resizing only

# ------------------------------------------------------------
# D. MINIMUM AND MAXIMUM WINDOW SIZE
# ------------------------------------------------------------

root.minsize(400, 300)
root.maxsize(1000, 700)

# The window cannot be manually resized below 400x300
# or above 1000x700 under normal window-manager behavior.

# ------------------------------------------------------------
# E. WINDOW BACKGROUND COLOR
# ------------------------------------------------------------

root.configure(bg="lightblue")

# config() is an alias for configure().
# Example: root.config(bg="lightyellow")

# ------------------------------------------------------------
# F. WINDOW ICON
# ------------------------------------------------------------

# To set a custom icon, place app.ico in the same directory
# and uncomment the following line:
# root.iconbitmap("app.ico")

# ------------------------------------------------------------
# G. WINDOW STATE
# ------------------------------------------------------------

# Start in the normal window state.
root.state("normal")

# Other states to test individually:
# root.state("iconic")  # Minimize
# root.state("zoomed")  # Maximize on supported platforms

# Print the current window state in the terminal.
print("Current window state:", root.state())

# ------------------------------------------------------------
# H. CLOSE THE WINDOW
# ------------------------------------------------------------

# Define a function to close the application.
def close_window():
    root.destroy()

# Close the application automatically after 30 seconds.
# Change or remove this line if you want the window to
# remain open until you close it manually.
root.after(30000, close_window)

# ------------------------------------------------------------
# I. START THE EVENT LOOP
# ------------------------------------------------------------

root.mainloop()


# ============================================================
# 4. IMPORTANT THINGS TO BE MEMORIZED
# ============================================================

"""
Syntax                              Meaning
------------------------------------------------------------
tk.Tk()                             Create the main window
root.title("My App")                Set the window title
root.geometry("700x450")            Set width and height
root.geometry("700x450+100+80")     Set size and position
root.resizable(False, False)        Disable resizing
root.minsize(400, 300)              Set minimum dimensions
root.maxsize(1000, 700)             Set maximum dimensions
root.configure(bg="lightblue")      Set background color
root.config(bg="lightyellow")       Alternative configuration
root.state()                        Get the current state
root.state("normal")                Normal window
root.state("iconic")                Minimized window
root.state("zoomed")                Maximized on supported platforms
root.iconbitmap("app.ico")          Set a custom window icon
root.destroy()                      Close and destroy the window
root.mainloop()                     Start the event loop

Important Rules:
1. geometry() follows WIDTHxHEIGHT+X+Y.
2. Width and height are measured in pixels.
3. X and Y define the window's screen position.
4. resizable() controls width and height independently.
5. minsize() and maxsize() set dimension limits.
6. configure() and config() are equivalent methods.
7. Window state names can behave differently across platforms.
8. iconbitmap() requires a valid icon file.
9. destroy() closes the window and destroys its widgets.
10. mainloop() keeps the GUI responsive.
"""