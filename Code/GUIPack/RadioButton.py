import tkinter as tk

window = tk.Tk()
window.title("Bonjour")
window.geometry("400x300")

var = tk.StringVar()
l = tk.Label(window, textvariable=var, background="white", width=10)
l.pack()


def print_selection():
    var.get()


r1 = tk.Radiobutton(window, text="Beijing", value="Beijing",
                    variable=var, command=print_selection)
r2 = tk.Radiobutton(window, text="Shanghai", value="Shanghai",
                    variable=var, command=print_selection)
r3 = tk.Radiobutton(window, text="Guangzhou", value="Guangzhou",
                    variable=var, command=print_selection)
r1.pack()
r2.pack()
r3.pack()

window.mainloop()
