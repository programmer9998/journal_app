import os
import tkinter as tk
from tkinter import scrolledtext, Listbox, END

# edited using the app
def list_files():
    folder_path = entry.get()
    if not os.path.isdir(folder_path):
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a valid folder path.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    file_list.delete(0, tk.END)
    for file_name in files:
        file_list.insert(tk.END, file_name)

def show_file_content(event):
    selected_file = file_list.get(file_list.curselection())
    with open(os.path.join(entry.get(), selected_file), 'r') as file:
        content = file.read()
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, content)

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

# Create a listbox to display file names
file_list = Listbox(window, width=50, height=10)
file_list.pack()
file_list.bind('<Double-Button-1>', show_file_content)

# Create a scrolled text widget to display the file content
result_text = scrolledtext.ScrolledText(window, width=50, height=20)
result_text.pack()

# Start the GUI event loop
window.mainloop()

