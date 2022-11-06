import pyautogui
import time
import random

with open('text.txt',mode='r',encoding='utf-8') as f:
    text = f.readlines()
time.sleep(3)

while True:
    pyautogui.typewrite(random.choice(text),interval=0.15)
    time.sleep(2)