#导入tkinter库
from tkinter import *
#创建主窗口
def creatwindow():
    #新建窗口对象
    window = Tk()
    #设置窗口标题
    window.title('NO BOOL！')
    #设置窗口长宽
    window.geometry('500x300')
    #设置窗口图标
    window.iconbitmap("icon.ico")
    #返回一个窗口对象
    return window
#创建文本输入框
def entryCreat(root):
    entry = Entry(root)
    return entry
#创建一个文本部件
def labelCreat(root,var):
    label = Label(root,textvariable=var)
    return label
