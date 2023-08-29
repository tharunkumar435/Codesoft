import tkinter as tk
import random
import string

def generate_password():
    username = username_entry.get()
    password_length = int(length_entry.get())
    
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    
    generated_password_entry.delete(0, tk.END)  # Clear previous content
    generated_password_entry.insert(0, generated_password)

def reset_password():
    generated_password_entry.delete(0, tk.END)

def accept_password():
    accepted_password = generated_password_entry.get()
    print("Accepted Password:", accepted_password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")

# Set the title heading with black font color
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), fg="black")
title_label.pack(pady=10)

# Create and place widgets
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password",bg="light blue", command=generate_password)
generate_button.pack()

# Entry widget to display the generated password
generated_password_entry = tk.Entry(root)
generated_password_entry.pack()

# Create "Reset" and "Accept" buttons
button_frame = tk.Frame(root)
reset_button = tk.Button(button_frame, text="Reset", command=reset_password)
accept_button = tk.Button(button_frame, text="Accept", command=accept_password)

reset_button.pack(side=tk.LEFT, padx=10)
accept_button.pack(side=tk.LEFT)

button_frame.pack()

# Start the GUI event loop
root.mainloop()
