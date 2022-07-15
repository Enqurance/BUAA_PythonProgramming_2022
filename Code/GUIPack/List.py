import tkinter as tk

window = tk.Tk()
window.title("Bonjour")
window.geometry("400x400")


def print_selection():
    l.mainloop()


options = tk.OptionMenu(1, 2, 3, 4, 5)
l = tk.Listbox(options)
l.pack()

b = tk.Button(window, text="Print selection", command=print_selection)

window.mainloop()
