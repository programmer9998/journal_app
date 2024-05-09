import os
import tkinter as tk
from tkinter import scrolledtext, Listbox, END, Toplevel, Label, Entry, Button

current_file = None

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
    global current_file
    if file_list.curselection():
        selected_file = file_list.get(file_list.curselection())
        current_file = os.path.join(entry.get(), selected_file)
        with open(current_file, 'r') as file:
            content = file.read()
            result_text.delete(1.0, tk.END)  # Clear old content
            result_text.insert(tk.END, content)
            result_text.config(state=tk.DISABLED)  # Disable editing initially

def edit_file():
    result_text.config(state=tk.NORMAL)  # Enable editing
    edit_button.config(state=tk.DISABLED)
    save_button.config(state=tk.NORMAL)

def save_file():
    content = result_text.get(1.0, tk.END)
    with open(current_file, 'w') as file:
        file.write(content)
    result_text.config(state=tk.DISABLED)  # Disable editing
    edit_button.config(state=tk.NORMAL)
    save_button.config(state=tk.DISABLED)

def create_new_file_window():
    new_file_window = Toplevel(window)
    new_file_window.title("Create New File")

    def save_new_file():
        new_file_name = new_file_entry.get()
        new_file_content = new_file_text.get(1.0, tk.END)
        with open(os.path.join(entry.get(), new_file_name + ".txt"), 'w') as file:
            file.write(new_file_content)
        new_file_window.destroy()
        list_files()

    new_file_label = Label(new_file_window, text="File Name:")
    new_file_label.pack()

    new_file_entry = Entry(new_file_window, width=30)
    new_file_entry.pack()

    new_file_text = scrolledtext.ScrolledText(new_file_window, width=50, height=20)
    new_file_text.pack()

    save_button = Button(new_file_window, text="Save", command=save_new_file)
    save_button.pack()

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
file_list.bind('<ButtonRelease-1>', show_file_content)

# Create a scrolled text widget to display the file content
result_text = scrolledtext.ScrolledText(window, width=50, height=20)
result_text.pack()

# Create an Edit button
edit_button = tk.Button(window, text="Edit", command=edit_file)
edit_button.pack()

# Create a Save button
save_button = tk.Button(window, text="Save", command=save_file, state=tk.DISABLED)
save_button.pack()

# Create a New File button
new_file_button = tk.Button(window, text="New File", command=create_new_file_window)
new_file_button.pack()

# Start the GUI event loop
window.mainloop()
