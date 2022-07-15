import tkinter as tk

window = tk.Tk()
window.title("Hey bitch")
window.geometry("400x400")


def insert_forward():
    var = e.get()
    t.insert("insert", var)


def insert_end():
    var = e.get()
    t.insert("end", var)


e = tk.Entry(window)
e.pack()

b1 = tk.Button(window, text="InsertForward", command=insert_forward)
b2 = tk.Button(window, text="InsertEnd", command=insert_end)
b1.pack()
b2.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()
