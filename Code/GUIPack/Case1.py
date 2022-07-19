import tkinter as tk
from time import strftime

window = tk.Tk()
window.title("Bonjour")
window.geometry("500x350")

label1 = tk.Label(window, font=("Times New Roman", 50, "bold"),
                  bg="white", )
label1.place(x=250, y=150, anchor="center")

mode = "time"


def showtime():
    if mode == "time":
        string = strftime("%H:%M:%S %p")
    else:
        string = strftime("%Y-%m-%d")
    label1.config(text=string)
    label1.after(100, showtime)


def mouse_click(event):
    global mode
    if mode == "time":
        mode = "date"
    else:
        mode = "time"


# 'bind' is used to response to mouse clicks
label1.bind("<Button-1>", mouse_click)
showtime()
window.mainloop()
