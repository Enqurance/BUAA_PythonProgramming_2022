import tkinter as tk

window = tk.Tk()
window.title("Bonjour")
window.geometry("400x300")
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.StringVar()
var3.set("I don't like either of them")

l = tk.Label(window, background="white", width=30, textvariable=var3)
l.pack()


def print_selection():
    if (var1.get() == 0) & (var2.get() == 0):
        var3.set("I don't like either of them")
    elif (var1.get() == 1) & (var2.get() == 0):
        var3.set("I love C++")
    elif (var1.get() == 0) & (var2.get() == 1):
        var3.set("I love Python")
    else:
        var3.set("I love both of them")


b1 = tk.Checkbutton(window, text="C++", command=print_selection, variable=var1,
                    onvalue=1, offvalue=0)
b2 = tk.Checkbutton(window, text="Python", command=print_selection, variable=var2,
                    onvalue=1, offvalue=0)
b1.pack()
b2.pack()

window.mainloop()
