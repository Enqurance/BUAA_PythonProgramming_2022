import tkinter

root = tkinter.Tk()
root.title('显示 PhotoImage和BitmapImage对象')  # 顶层窗口Name

tkinter.Label(root, text='error', compound='bottom', bitmap='error').pack()  # 图像居下
tkinter.Label(root, text='hourglass', compound='top', bitmap='hourglass').pack()  # 图像居上
tkinter.Label(root, text='info', compound='right', bitmap='info').pack()  # 图像居右
tkinter.Label(root, text='question', compound='left', bitmap='question').pack()  # 图像居左
tkinter.Label(root, text='warning', compound='center', bitmap='warning').pack()  # 文字覆盖在图像上
