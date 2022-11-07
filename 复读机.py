import time
import pyautogui
import pyperclip

print('''
欢迎使用「复读机」
''')
text = input('请输入需要复读的文字：')
number = int(input('请输入要复读的次数：'))

i = 4
while i > 1:
    time.sleep(1)
    i = i - 1
    print(str(i) + '秒后开始执行')

pyperclip.copy(text=text)
for i in range(number):
    # Mac 系统使用：
    pyautogui.keyDown('command')
    pyautogui.keyDown('v')
    # Windows 系统使用：
    # pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(1)
print('''
复读完毕，已退出。
''')