import tkinter as tk





app = tk.Tk()
app.title("Journal - Note Management System")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# print(f"Screen Size: {screen_width}x{screen_height}")


def ignore_input(event):
    return "break"  # This stops the event from propagating further


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_area(event):
    frame2.pack(side="right", padx=10, pady=0)  # Fill both directions and expand


# Set initial window size
# window_width, window_height = 1000, 700
# window_width, window_height = int(screen_width // 2.4), int(screen_height // 1.9)
window_width, window_height = int(screen_width * 0.8), int(screen_height * 0.8)
app.resizable(False, False)  # Disable resizing by dragging

# Calculate x and y coordinates for the Tk root window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2) - 60
app.geometry(f"{window_width}x{window_height}+{x}+{y}")
# frame1 = tk.Frame(app, borderwidth=2, relief="sunken", bg='blue', height = 400, width = 400)
frame1 = tk.Frame(app, borderwidth=2, relief="sunken", height = window_height, width = window_width//4, bg='blue')
frame1.pack_propagate(False)  # Prevent the frame from resizing to fit its content
# frame1.place(x=10, y=0)  # Position at (150, 100) within the main window
frame1.pack(side="left", padx=10, pady=0)  # Fill both directions and expand

frame2 = tk.Frame(app, borderwidth=2, relief="sunken", height = window_height, width = window_width) # SET THE WIDTH TO BE LARGER THAN ALLOWED, SO IT FILLS THE REST OF THE SPACE
# frame2.place(x=430, y=0)  # Position at (150, 100) within the main window
frame2.pack(side="right", padx=10, pady=0)  # Fill both directions and expand
frame2.pack_propagate(False)  # Prevent the frame from resizing to fit its contents

frame5 = tk.Frame(frame1, borderwidth=2, relief="sunken", height = 50, bg='red')
# frame2.place(x=430, y=0)  # Position at (150, 100) within the main window
frame5.pack(side="top", fill="x", padx=0, pady=0)  # Fill both directions and expand
frame5.pack_propagate(False)  # Prevent the frame from resizing to fit its contents

frame3 = tk.Frame(frame1, borderwidth=2, relief="sunken", height = window_height, bg='yellow')
# frame2.place(x=430, y=0)  # Position at (150, 100) within the main window
frame3.pack(side="bottom", fill="x", padx=0, pady=0)  # Fill both directions and expand
frame3.pack_propagate(False)  # Prevent the frame from resizing to fit its contents

frame4 = tk.Frame(frame2, borderwidth=2, relief="sunken", height = window_height // 1.2, bg='pink')
# frame2.place(x=430, y=0)  # Position at (150, 100) within the main window
frame4.pack(side="top", fill="x", padx=0, pady=0)  # Fill both directions and expand
frame4.pack_propagate(False)  # Prevent the frame from resizing to fit its contents

frame6 = tk.Frame(frame2, borderwidth=2, relief="sunken", height = window_height // 1.2, bg='blue')
# frame2.place(x=430, y=0)  # Position at (150, 100) within the main window
frame6.pack(side="top", fill="x", padx=0, pady=0)  # Fill both directions and expand
frame6.pack_propagate(False)  # Prevent the frame from resizing to fit its contents

text_area1 = tk.Text(frame3, height = 15, bg='gold')
text_area1.pack(fill="x", side="top", padx=0, pady=0)  # fill="both" makes it expand both horizontally and vertically
text_area1.pack_propagate(False)  # Prevent the frame from resizing to fit its contents

# Bind keypress event to ignore_input function
text_area1.bind("<Key>", ignore_input)

text_area2 = tk.Text(frame1)
text_area2.pack(fill="both", side="top", padx=0, pady=0)  # fill="both" makes it expand both horizontally and vertically
text_area2.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
text_area2.bind("<Key>", ignore_input)

# text = "testing text."
# button1 = tk.Button(frame3, text="Start", command=lambda: write_text1(text))
'''
button1 = tk.Button(frame3, text="Start")
button1.pack(side="left", padx=10)
'''
button2 = tk.Button(frame3, text="End", command=lambda: kill_process_by_name('lily_window.exe'))
button2.pack(side="right", padx=10)
'''
button3 = tk.Button(frame2, text="Start", command=write_text)
button3.pack(side="left", padx=10)
button4 = tk.Button(frame2, text="End")
button4.pack(side="right", padx=10)
'''

# frame2.pack_forget()
app.bind("<Control-k>", show_area)



app.mainloop()