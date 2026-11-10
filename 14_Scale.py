
"""
Topic: Tkinter Scale
File: 14_Scale.py
Purpose: Learn Scale widget and create a volume controller.
"""

# 1. SHORT THEORY

"""
Scale creates a slider for selecting numeric values.

Important options:
from_     - Starting value
to        - Ending value
orient    - Horizontal or vertical
resolution - Step between values
variable  - Connects a Tkinter variable
command   - Calls a function when the slider changes
length    - Controls slider length
"""

# 2. IMPORTS

import tkinter as tk

# 3. WORKING PROGRAM

root = tk.Tk()
root.title("Tkinter Scale")
root.geometry("400x450")

# Create a variable
volume_var = tk.IntVar(value=50)

# Display current value
value_label = tk.Label(
    root,
    text="Volume: 50%",
    font=("Arial", 14)
)
value_label.pack(pady=10)

# Update label when slider changes
def update_volume(value):
    value_label.config(text=f"Volume: {int(float(value))}%")

# Create horizontal Scale
volume_scale = tk.Scale(
    root,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    resolution=5,
    variable=volume_var,
    command=update_volume,
    length=250,
    sliderlength=20,
    troughcolor="lightblue",
    fg="black",
    bg="white"
)
volume_scale.pack(pady=10)

# Create vertical Scale
brightness_scale = tk.Scale(
    root,
    from_=0,
    to=100,
    orient=tk.VERTICAL,
    resolution=10,
    length=200,
    label="Brightness"
)
brightness_scale.pack(pady=10)

# Read current value
def show_values():
    result.config(
        text=f"Volume: {volume_scale.get()}%\n"
             f"Brightness: {brightness_scale.get()}%"
    )

# Set slider value
def reset_values():
    volume_scale.set(50)
    brightness_scale.set(50)

# Buttons
tk.Button(root, text="Show Values", command=show_values).pack(pady=5)
tk.Button(root, text="Reset", command=reset_values).pack(pady=5)

result = tk.Label(root, text="Adjust the sliders")
result.pack(pady=10)

root.mainloop()


# 4. IMPORTANT THINGS TO BE MEMORIZED

"""
1. tk.Scale() creates a slider.
2. from_ defines the minimum value.
3. to defines the maximum value.
4. orient=tk.HORIZONTAL creates a horizontal slider.
5. orient=tk.VERTICAL creates a vertical slider.
6. resolution defines the step size.
7. get() reads the current value.
8. set() changes the slider value.
9. variable connects a Tkinter variable.
10. command calls a function when the slider changes.
11. length controls the slider length.
12. sliderlength controls the slider handle size.
"""