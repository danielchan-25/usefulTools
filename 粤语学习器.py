import pyttsx3,time

engine = pyttsx3.init()
engine.setProperty('rate',100)
engine.setProperty('volume',0.6)
engine.setProperty('voice', "com.apple.speech.synthesis.voice.sin-ji")


while True:
    text = input('请输入需要翻译的文字：')
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(1)