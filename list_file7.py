import tkinter as tk
from tkinter import filedialog, messagebox
import os
import random

class TextFileManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text File Manager")

        self.search_entry = tk.Entry(self.root, width=50)
        self.search_entry.pack()

        self.search_button = tk.Button(self.root, text="Search", command=self.search_files)
        self.search_button.pack()

        self.result_listbox = tk.Listbox(self.root, width=50)
        self.result_listbox.pack(side=tk.LEFT, fill=tk.Y)

        self.result_listbox.bind("<Double-Button-1>", self.load_search_result)

        self.text_editor = tk.Text(self.root, width=80, height=20)
        self.text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.load_files()

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New File", command=self.create_new_file)
        file_menu.add_command(label="Save Changes", command=self.save_changes)

    def load_files(self):
        self.result_listbox.delete(0, tk.END)
        for filename in os.listdir("."):
            if filename.endswith(".txt"):
                self.result_listbox.insert(tk.END, filename)

    def load_search_result(self, event):
        selected_file = self.result_listbox.get(self.result_listbox.curselection())
        with open(selected_file, "r") as file:
            content = file.read()
            self.text_editor.delete(1.0, tk.END)
            self.text_editor.insert(tk.END, content)

    def create_new_file(self):
        file_name = filedialog.asksaveasfilename(defaultextension=".txt",
                                                  filetypes=[("Text files", "*.txt")])
        if file_name:
            with open(file_name, "w") as file:
                file.write("")
            self.load_files()

    def save_changes(self):
        selected_file = self.result_listbox.get(self.result_listbox.curselection())
        content = self.text_editor.get(1.0, tk.END)
        with open(selected_file, "w") as file:
            file.write(content)
        messagebox.showinfo("Save Changes", "Changes saved successfully.")

    def search_files(self):
        query = self.search_entry.get().lower()
        self.result_listbox.delete(0, tk.END)
        for filename in os.listdir("."):
            if filename.endswith(".txt"):
                with open(filename, "r") as file:
                    content = file.read().lower()
                    if query in filename.lower() or query in content:
                        self.result_listbox.insert(tk.END, filename)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    TextFileManager().run()
