import tkinter as tk
from tkinter import filedialog, messagebox
import os
import random

class TextFileManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text File Manager")

        # Set window size to cover the entire screen
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        self.new_file_button = tk.Button(button_frame, text="New File", command=self.create_new_file)
        self.new_file_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_changes_button = tk.Button(button_frame, text="Save Changes", command=self.save_changes)
        self.save_changes_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_file_button = tk.Button(button_frame, text="Delete File", command=self.confirm_delete_file)
        self.delete_file_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.search_button = tk.Button(button_frame, text="Search", command=self.search_files)
        self.search_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.search_entry = tk.Entry(button_frame, width=50)
        self.search_entry.pack(side=tk.RIGHT, padx=5, pady=5)
        self.search_entry.bind("<Return>", lambda event: self.search_files())

        self.result_listbox = tk.Listbox(self.root, width=50)
        self.result_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.result_listbox.bind("<ButtonRelease-1>", self.load_search_result)

        self.result_scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.result_listbox.yview)
        self.result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_listbox.config(yscrollcommand=self.result_scrollbar.set)

        self.text_editor = tk.Text(self.root, width=80, height=20, font=("TkDefaultFont", 10))
        self.text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.text_editor.bind("<Control-MouseWheel>", self.change_font_size)

        self.text_scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.text_editor.yview)
        self.text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_editor.config(yscrollcommand=self.text_scrollbar.set)

        self.load_files(random_highlight=True)

    def load_files(self, random_highlight=False):
        self.result_listbox.delete(0, tk.END)
        files = [filename for filename in os.listdir(".") if filename.endswith(".txt")]
        if random_highlight and files:
            random_file = random.choice(files)
            self.result_listbox.insert(tk.END, random_file)
            self.result_listbox.selection_set(tk.END)  # Highlight the random file
            self.load_selected_file(random_file)
        else:
            for filename in files:
                self.result_listbox.insert(tk.END, filename)

    def load_selected_file(self, filename):
        with open(filename, "r") as file:
            content = file.read()
            self.text_editor.delete(1.0, tk.END)
            self.text_editor.insert(tk.END, content)

    def load_search_result(self, event):
        selected_file = self.result_listbox.get(self.result_listbox.curselection())
        self.load_selected_file(selected_file)

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

    def confirm_delete_file(self):
        selected_file = self.result_listbox.get(self.result_listbox.curselection())
        confirmation = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {selected_file}?")
        if confirmation:
            self.delete_file(selected_file)

    def delete_file(self, file_path):
        os.remove(file_path)
        self.load_files()

    def search_files(self):
        query = self.search_entry.get().lower()
        self.result_listbox.delete(0, tk.END)
        for filename in os.listdir("."):
            if filename.endswith(".txt"):
                with open(filename, "r") as file:
                    content = file.read().lower()
                    if query in filename.lower() or query in content:
                        self.result_listbox.insert(tk.END, filename)

    def change_font_size(self, event):
        font = self.text_editor.cget("font")
        font_family, _, font_size = font.partition(" ")
        font_size = int(font_size)  # Convert font size to an integer

        # Get the current vertical scroll position
        scroll_pos = self.text_editor.yview()[0]

        if event.delta > 0:
            # Increase font size with Ctrl key
            font_size += 1
        elif event.delta < 0:
            # Decrease font size with Ctrl key
            if font_size > 1:
                font_size -= 1

        self.text_editor.configure(font=(font_family, font_size))

        # Set the vertical scroll position back to what it was
        self.text_editor.yview_moveto(scroll_pos)

        # Prevent further propagation of the event
        return "break"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    TextFileManager().run()
