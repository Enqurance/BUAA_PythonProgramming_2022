import tkinter  # 导入Tkinter库

root = tkinter.Tk()  # 创建一个顶层窗口
root.title('《大学计算机基础》课程问卷调查')  # 创建顶层窗口Name
# 添加label，显示提示信息
label1 = tkinter.Label(root, text="本调查问卷包括单选题和多选题，请认真作答，谢谢！")
label2 = tkinter.Label(root, text="1、你觉得《大学计算机基础》哪部分（或哪几部分）最难？")
# 将label显示到窗体中
label1.pack()  # 采用packMethod 进行组件布局，默认在父窗口中自顶向下添加组件
label2.pack()
root.mainloop()
