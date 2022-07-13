import tkinter

# (1)生成窗体
root = tkinter.Tk()
# (2)生成主菜单
menubar = tkinter.Menu(root)
# (3)生成子菜单
filemenu = tkinter.Menu(menubar)  # 创建子菜单，其父组件为主菜单
for item in ['Python', 'C', 'C++', 'C#']:
    filemenu.add_command(label=item)
    filemenu.add_separator()  # 添加分隔线

# （4）指定主菜单与子菜单的级联关系
# 将menubar的menu attribute指定为filemenu，即filemenu为menubar的下拉菜单
menubar.add_cascade(label='Language', menu=filemenu)  # 指定级联关系
root['menu'] = menubar  # 将父窗口的menu attribute设置为menubar，即指定顶级菜单

root.mainloop()  # event循环
