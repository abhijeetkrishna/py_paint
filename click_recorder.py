import tkinter as tk

def record_position(event):
    x = event.x
    y = event.y
    print(f"Clicked at position ({x}, {y})")

def create_gui():
    root = tk.Tk()
    root.title("Click Recorder")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    canvas.bind("<Button-1>", record_position)

    root.mainloop()

create_gui()
