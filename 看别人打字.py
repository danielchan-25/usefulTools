import pyautogui
import time
import random

txt = input('请输入文章的地址：')
with open(file=txt,mode='r',encoding='utf-8') as f:
    text = f.readlines()

i = 4
while i > 0:
    i = i - 1
    print(str(i) + '秒后开始')
    time.sleep(1)

while True:
    pyautogui.typewrite(random.choice(text),interval=0.05)
    time.sleep(2)