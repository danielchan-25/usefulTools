import requests

word = input('输入需要我帮你说的事：')
url = "https://www.jiuwa.net/tools/jupai/index.php"
resp = requests.post(url,data={'t':word})
photo_url = f'https://www.jiuwa.net/{resp.content.decode("utf-8")}'

with open('upuptoyou.png',mode='wb') as f:
    f.write(requests.get(photo_url).content)
print('图片生成完成。')