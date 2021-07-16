#导入tkinter库
from tkinter import *
#导入功能性库func
from rootCreat import *
#——————分割线——————
#窗口创建
def buttonCreat(root):
    button = Button(root,text="识别",command=analize)
    return button
#分析输入框中的内容并显示结果
def analize():
    boolean = wt[0].get()
    try:
        lastbool = eval(boolean)
        lastbool = str(lastbool)
    except:
        lastbool = "不是布尔式"
    var.set(lastbool)
#——————分割线——————
#使用func里的函数创建一个窗口
window = creatwindow()
var = StringVar()
#新建一个列表，用来存储窗口部件信息
wt = []
#新建一个输入部件并存储在列表中，显示
wt.append(entryCreat(window))
#新建一个按钮部件并存储在列表中，显示
wt.append(buttonCreat(window))
#新建一个文本部件并存储在列表中，显示
wt.append(labelCreat(window,var))
#全部pack()
for thing in wt:
    thing.pack()
#主循环
window.mainloop()