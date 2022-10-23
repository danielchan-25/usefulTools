from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter

# 众所周知，水果有非常多的品种，有苹果、香蕉、西瓜、葡萄等。
# 但你知道水果可以分为六个大类吗？
# 例如苹果属于蔷薇科，香蕉属于芭蕉科，西瓜属于葫芦科，葡萄属于葡萄科。
# 由于品种过于繁多，难以区分种类，所以我做了一个水果鉴定器，用于鉴定水果的种类

# 全局设置
window = Tk()
window.geometry('400x300+300+100')
window.config(background="#FFFFFF")
window.title('水果种类鉴定器')
text_title = tk.Label(window,text='欢迎使用：水果种类鉴定器',bg='#000000',font=('Arial',12),width=60,height=3,fg='#CCCCCC')
text_title.pack()

# 文本框
bg_text = tk.Label(window,text='请在下面方框中输入水果名称\n如：苹果')
bg_text.place(x=20,y=95,width=200,height=50)

# 输入框
input_frame = tk.Entry(window,fg='#000000',font=('Arial',14))
input_frame.place(x=20,y=180,width=200,height=50)

# 按钮
def button_show():
    messagebox.showinfo(title='检测成功！',message='这是一种水果')
button = tk.Button(window,command=button_show,text='检测',font=('宋体',40)).place(x=270,y=90,width=100,height=150)

window.mainloop()