from tkinter import *
import tkinter
import tkinter as tk


# 全局设置
window = Tk()
window.geometry('400x300+300+100')
window.config(background="#FFFFFF")
window.title('粤语学习器')
text_title = tk.Label(window,text='欢迎使用：水果种类鉴定器',bg='#000000',font=('Arial',12),width=60,height=3,fg='#CCCCCC')
text_title.pack()