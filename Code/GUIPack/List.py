import tkinter as tk

window = tk.Tk()
window.title("Bonjour")
window.geometry("400x400")

var1 = tk.StringVar()
var2 = tk.StringVar()
var2.set("1 2 3 4 5 a ab c")
l = tk.Label(window, background="yellow", width=4, textvariable=var1)
l.pack()

lb = tk.Listbox(window, listvariable=var2)
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert("end", item)
lb.insert(1, "first")
lb.insert(2, "second")
lb.delete(2)
lb.pack()


def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


b = tk.Button(window, text="Print selection", command=print_selection)
b.pack()
window.mainloop()
