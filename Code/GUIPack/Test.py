import tkinter as tk

window = tk.Tk()
window.title("Son of bitch")
window.geometry("200x100")

var = tk.StringVar()
l1 = tk.Label(window, textvariable=var)
l1.pack()

hit = False


def hit_me():
    global hit
    if not hit:
        var.set("Ouch!Hurt!")
        hit = True
    else:
        var.set("")
        hit = False


b = tk.Button(window, text="hit me bitch", width=15, height=2, command=hit_me)
b.pack()
window.mainloop()
