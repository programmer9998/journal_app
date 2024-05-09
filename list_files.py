import os
import tkinter as tk
from tkinter import scrolledtext

def list_files():
    folder_path = entry.get()
    if not os.path.isdir(folder_path):
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a valid folder path.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "\n".join(files))

# Create the main window
window = tk.Tk()
window.title("List Files in Folder")

# Create a label and entry for entering folder path
label = tk.Label(window, text="Enter folder path:")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

# Create a button to list files
button = tk.Button(window, text="List Files", command=list_files)
button.pack()

# Create a scrolled text widget to display the result
result_text = scrolledtext.ScrolledText(window, width=50, height=20)
result_text.pack()

# Start the GUI event loop
window.mainloop()
