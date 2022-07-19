import tkinter as tk

window = tk.Tk()
window.title("Sign In")
window.geometry("600x400")

canvas1 = tk.Canvas(window, height=800, width=600)
image_file1 = tk.PhotoImage(file="Pics/Welcome.png")
image1 = canvas1.create_image(200, 0, anchor="nw", image=image_file1)
canvas1.pack(side="top")

l1 = tk.Label(window, text="User name:")
l1.place(x=150, y=200)
l2 = tk.Label(window, text="Password:")
l2.place(x=200, y=200)

window.mainloop()
