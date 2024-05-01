import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Container Example")

# Create a container frame
container = tk.Frame(root, padx=10, pady=10)
container.pack()

# Create widgets inside the container
label = tk.Label(container, text="This is inside the container")
label.pack()

button = tk.Button(container, text="Click me")
button.pack()

# Start the main event loop
root.mainloop()
