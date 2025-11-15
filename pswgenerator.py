import random
import string
import tkinter as tk
from tkinter import messagebox

# Generate Password
def generate_password():
    size = 12 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(size))
    entry_password.delete(0, tk.END)   
    entry_password.insert(0, password) 

# Window
window = tk.Tk()
window.title("Password Generator")
window.geometry("200x200")  # largura x altura

# Entry
entry_password = tk.Entry(window, width=30)
entry_password.pack(pady=10)

# Button
button = tk.Button(window, text='Generate Password', command=generate_password)
button.pack(pady=20)

# Run the GUI
window.mainloop()

