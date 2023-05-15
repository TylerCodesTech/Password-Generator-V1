import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=10, use_custom_parameters=False, custom_word=''):
    if use_custom_parameters:
        characters = custom_word
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_clicked():
    length = int(length_entry.get())
    use_custom_parameters = custom_params_var.get()
    custom_word = custom_word_entry.get()

    if use_custom_parameters and not custom_word:
        messagebox.showerror("Error", "Please enter a custom word.")
        return

    password = generate_password(length, use_custom_parameters, custom_word)
    password_result_label.config(text="Generated Password: " + password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Length label and entry
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Custom parameters checkbox
custom_params_var = tk.BooleanVar()
custom_params_checkbox = tk.Checkbutton(window, text="Use Custom Parameters", variable=custom_params_var)
custom_params_checkbox.pack()

# Custom word entry (visible when custom parameters are selected)
custom_word_label = tk.Label(window, text="Custom Word:")
custom_word_entry = tk.Entry(window)
custom_word_label.pack()
custom_word_entry.pack()

# Generate password button
generate_button = tk.Button(window, text="Generate Password", command=generate_password_button_clicked)
generate_button.pack()

# Generated password label
password_result_label = tk.Label(window, text="Generated Password: ")
password_result_label.pack()

# Start the main event loop
window.mainloop()
