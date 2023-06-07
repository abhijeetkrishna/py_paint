import tkinter as tk

def record_position(event):
    x = event.x
    y = event.y
    positions.append((x, y))
    update_canvas()

def start_drawing(event):
    global positions
    positions = []
    canvas.bind('<B1-Motion>', record_position)

def stop_drawing(event):
    canvas.unbind('<B1-Motion>')

def update_canvas():
    canvas.delete('curve')
    for i in range(len(positions) - 1):
        x1, y1 = positions[i]
        x2, y2 = positions[i + 1]
        canvas.create_line(x1, y1, x2, y2, tags='curve')

def create_gui():
    global canvas
    root = tk.Tk()
    root.title("Curve Drawer")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    canvas.bind('<Button-1>', start_drawing)
    canvas.bind('<ButtonRelease-1>', stop_drawing)

    root.mainloop()

create_gui()
