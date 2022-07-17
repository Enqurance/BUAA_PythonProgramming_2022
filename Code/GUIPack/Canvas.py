import tkinter as tk

window = tk.Tk()
window.title("Bonjour")
window.geometry("800x600")


def move_down():
    c.move(oval, 0, 10)


def move_up():
    c.move(oval, 0, -10)


c = tk.Canvas(window, background="white", width=400, height=300)
b1 = tk.Button(window, text="Move Down", command=move_down)
b2 = tk.Button(window, text="Move Up", command=move_up)

image1 = tk.PhotoImage(file="Images/Pic.png")
image = c.create_image(200, 150, image=image1, anchor="center")

x0, y0, x1, y1 = 10, 20, 30, 40
line = c.create_line(x0, y0, x1, y1)
oval = c.create_oval(x0, y0, x1, y1, fill="green")

c.pack()
b1.pack(), b2.pack()

window.mainloop()
