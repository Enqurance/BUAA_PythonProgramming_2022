import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("Bonjour")
window.geometry("400x300")


def hit_me():
    # tk.messagebox.showinfo(title="Warning", message="Fuck you bitch")
    # tk.messagebox.showerror(title="Error", message="Fuck, your process is down")
    value = tk.messagebox.askquestion(title="asking")
    print(value)
    pass


b1 = tk.Button(window, text="Hit me", command=hit_me)

b1.pack()

window.mainloop()
