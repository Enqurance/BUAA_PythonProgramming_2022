import tkinter

root = tkinter.Tk()
label_title = tkinter.Label(root, text="1、你对本课程的评价是？")
label_title.pack(anchor=tkinter.W)  # 左对齐

# 采用for循环创建4个radiobutton
buttons = ["好", "较好", "差", "极差"]
for i in buttons:
    R = tkinter.Radiobutton(root, text=i)
    R.pack(anchor=tkinter.W, padx=20)  # 左对齐，与顶层窗口的左边框相距20个像素
root.mainloop()  # event循环
