import tkinter as tk

window = tk.Tk()
window.title("Bonjour")
window.geometry("400x300")

tk.Label(window, text="On the window", bg="white").pack()

frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_l.pack(side="left")
frm_r.pack(side="right")

tk.Label(frm_l, text="Left_1").pack()
tk.Label(frm_l, text="Left_2").pack()
tk.Label(frm_r, text="Right").pack()
window.mainloop()
