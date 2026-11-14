
"""
Topic: Events
File: 18_Events.py
Purpose: Understand event-driven programming and handle mouse,
keyboard, and focus events using Tkinter's bind() method.
"""

# 1. SHORT THEORY

"""
Event-driven programming:
The application responds to user actions such as clicks and key presses.

bind():
Connects an event to a function.

Common events:
<Button-1>       : Left mouse click
<Button-3>       : Right mouse click
<Double-Button-1>: Double left click
<Motion>         : Mouse movement
<KeyPress>       : Key pressed
<KeyRelease>     : Key released
<FocusIn>        : Widget receives focus
<FocusOut>       : Widget loses focus

Event object:
event.x      : Mouse X coordinate
event.y      : Mouse Y coordinate
event.keysym : Keyboard key name
event.widget : Widget where the event occurred
"""

# 2. IMPORTS

import tkinter as tk

# 3. MAIN WINDOW

root = tk.Tk()
root.title("Tkinter Events")
root.geometry("500x450")
root.configure(bg="lightblue")

# 4. EVENT FUNCTIONS

def mouse_click(event):
    event_label.config(
        text=f"Mouse Click: X={event.x}, Y={event.y}"
    )


def double_click(event):
    event_label.config(text="Double Click Detected!")


def mouse_move(event):
    event_label.config(
        text=f"Mouse Position: X={event.x}, Y={event.y}"
    )


def key_press(event):
    event_label.config(
        text=f"Key Pressed: {event.keysym}"
    )


def key_release(event):
    event_label.config(
        text=f"Key Released: {event.keysym}"
    )


def focus_in(event):
    event_label.config(text="Widget Received Focus")


def focus_out(event):
    event_label.config(text="Widget Lost Focus")


# 5. WIDGETS

tk.Label(
    root,
    text="Tkinter Event Handling",
    font=("Arial", 18, "bold"),
    bg="lightblue"
).pack(pady=15)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=15)

event_label = tk.Label(
    root,
    text="Perform an event",
    font=("Arial", 12),
    bg="white",
    width=40,
    height=3
)
event_label.pack(pady=20)

# 6. MOUSE EVENTS

root.bind("<Button-1>", mouse_click)
root.bind("<Double-Button-1>", double_click)
root.bind("<Motion>", mouse_move)

# 7. KEYBOARD EVENTS

entry.bind("<KeyPress>", key_press)
entry.bind("<KeyRelease>", key_release)

# 8. FOCUS EVENTS

entry.bind("<FocusIn>", focus_in)
entry.bind("<FocusOut>", focus_out)

# 9. EVENT LOOP

root.mainloop()
