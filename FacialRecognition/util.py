import tkinter as tk
from tkinter import messagebox

from tkinter import font

def get_button(window, text, color, command, fg='white'):
    button = tk.Button(
        window,
        text=text,
        activebackground="black",
        activeforeground="white",
        fg=fg,
        bg=color,
        command=command,
        height=2,
        width=20,
        font=('Helvetica bold', 18),
        relief="groove",  # Adds 3D-like effect
        borderwidth=3
    )
    return button


def get_img_label(window):
    label=tk.Label(window)
    label.grid(row=0, column=0)
    return label

def get_text_label(window, text):
    label = tk.Label(window, text=text, bg="#f0f0f0", fg="black")  # Light background, black text
    label.config(font=font.Font(family="Helvetica", size=20, weight="bold"), justify="left")
    return label

def get_entry_text(window):
    inputtxt = tk.Text(window,
                       height=2,
                       width=15,
                       font=("Helvetica", 28),  # Use a modern font style
                       bd=3,                    # Border for better visuals
                       relief="sunken")          # Creates a sunken effect for entry
    return inputtxt
def custom_msg_box(title, message):
    # Create a new Toplevel window
    msg_window = tk.Toplevel()
    msg_window.title(title)
    msg_window.geometry("300x150+500+300")
    msg_window.resizable(False, False)
    
    # Add label to display the message
    msg_label = tk.Label(msg_window, text=message, font=("Arial", 14), pady=20)
    msg_label.pack()

    # Add an "OK" button to close the message window
    ok_button = tk.Button(msg_window, text="OK", command=msg_window.destroy, font=("Helvetica", 12), width=10)
    ok_button.pack(pady=10)
    
    # Disable interaction with the parent window until the message window is closed
    msg_window.grab_set()

    # Keep the focus on the message window
    msg_window.focus_set()