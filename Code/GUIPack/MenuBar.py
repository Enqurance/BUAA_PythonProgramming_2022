import tkinter as tk

window = tk.Tk()
window.title("Bonjour")
window.geometry("800x600")


def new_file():
    var1.set("Create a new file!")


var1 = tk.StringVar()
label1 = tk.Label(window, background="white", width=400, height=300, textvariable=var1)
menubar = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit())

menubar.add_cascade(label="Edit File", menu=file_menu)

label1.pack()

submenu = tk.Menu(file_menu)

window.config(menu=menubar)
window.mainloop()
