import time
import pyautogui
import pyperclip

text = input('请输入需要复读的文字：')
number = int(input('请输入要复读的次数：'))

time.sleep(3)

pyperclip.copy(text=text)
for i in range(number):
    pyautogui.keyDown('command')
    pyautogui.keyDown('v')
    pyautogui.press('enter')
    time.sleep(1)