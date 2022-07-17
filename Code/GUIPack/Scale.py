import tkinter as tk

window = tk.Tk()
window.title("Bonjour")
window.geometry("400x300")

var = tk.StringVar()
l = tk.Label(window, background="white", width=30)
l.pack()


def print_value(v):
    l.config(text="Number is : " + v)


s = tk.Scale(window, label="Try me", from_=0, to=4, orient=tk.HORIZONTAL,
             length=200, showvalue=True, tickinterval=1, resolution=0.01,
             command=print_value)
# In Scale, command has a default argument that is the value of the Scale
s.pack()

window.mainloop()
