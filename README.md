# usefulTools

> 个人开发“非常有用”的 Python 小工具 🛠

## Media

用于存放图片素材，测试文字等。

## 🖼 图片转字符画

开发中。

## 🖨 复读机


众所周知，人类的三大本质之一：**复读机**

人类热爱玩梗跟风，虽然不明其意也要赶潮流的本质。

在网上做复读机的时候，避免不了需要一直打同一段文字。

虽说复制粘贴过程中，只需要按两次键盘，但累计次数多了，手也会累的。

所以我写了一个小工具：**「复读机」**，可以让你在做复读机的同时，还能兼顾其它事情。

<img src="https://github.com/danielchan-25/usefulTools/blob/main/Media/Repeater.gif?raw=true" alt="show" />

**使用说明：**

1. 运行程序：`python 复读机.py`
2. 输入需要复读的内容、次数。
3. 点击输入框，等待 3 秒后即开始复读。

## 🗣 我来帮你说

日常生活中，经常会遇到一些说出来令人尴尬，但很想告诉他/她的事情。

如：你有口臭/狐臭，你裤链没拉，你打游戏好菜，你唱歌好难听等...

这些事情，让我来帮你说。

通过可爱有趣的举牌小人，将这件难以启齿的事情，轻松幽默地告诉他/她。

<img src="https://github.com/danielchan-25/usefulTools/blob/main/Media/upuptoyou.png?raw=true" alt="show" />

**使用说明：**

1. 运行程序：`python 我来帮你说.py`
2. 输入需要我帮你说的事。
3. 会在本地生成一张 `upuptoyou.png`，大胆发给他/她。

## 🍉 水果鉴定器

众所周知，水果有非常多的品种，有苹果、香蕉、西瓜、葡萄等。但你知道水果可以分为六大类吗？

例如苹果属于蔷薇科，香蕉属于芭蕉科，西瓜属于葫芦科，葡萄属于葡萄科。

由于品种过于繁多，难区分种类，所以我做了一个「水果鉴定器」。

**使用说明：**

1. 运行程序：`python 水果鉴定器.py`
2. 在输入框中输入需要鉴定的水果名称。
3. 点击检测。

## 🤷🏻‍♂️ 猜你姓氏

开发中。

## 👤 生成个人信息

网上冲浪时，总会有些流氓网站要求你提交个人信息（姓名/地址/公司名/邮箱等）

填吧，自己的身份信息泄漏了；不填吧，它还要求你不得不填。

这时可以使用该工具，用于一键生成虚拟个人信息。（暂只支持中国）

包含有：姓名、身份证号、出生年月、城市、详细街道、经纬度、银行卡号、公司名、电子邮箱、手机号码等。

<img src="https://github.com/danielchan-25/usefulTools/blob/main/Media/Generate_Personal_Information.png?raw=true" alt="show" />

**使用说明：**

1. `python 生成个人信息.py`

## ⌨️ 看程序打字

有时候看程序打字，也是一种享受。

<img src="https://github.com/danielchan-25/usefulTools/blob/main/Media/typing.gif?raw=true" alt="show" />

**使用说明：**

1. 提前准备好一篇文章（英文），越长越好，一定要分行，可参考：`Media/Test_Text.txt`
1. 将输入法调整为：**英文**。
1. 新建一个文本编辑器用于查看程序打字。
1. 执行程序：`python 看程序打字.py`
1. 输入文章的绝对路径地址，如：`/Users/xx/Desktop/xx/abc.txt`
1. 鼠标光标点击该编辑器，等待程序自动打字，静静欣赏即可。
1. 该程序不会停止，如要退出，直接退出终端即可。

> 如要修改打字速度，修改：interval=()，数值越小越快，反之。

## ♨️ 真香

众所周知，人类的三大本质之一：**真香**

道破人类总爱放狠话，之后又自己打脸的本质。

## 🔧 粤语学习器

对于出生在非粤语地区的小伙伴，想学习粤语是一件挺难的事情。

一来是环境因素，身边很少人说粤语，自然也很难学会。

二是常用字非常复杂，普通话上很少用字在粤语里是常用的，例如：“睇”、“嘅”、“唔”、“係”等。

三是发音特别多样，普通话有四种音调，粤语有九种音调，与普通话差异太大。

所以我写了一个「粤语学习器」，虽说没有日常

## 📚 背书小工具

背书是一件很难很坚持的事情，所以我做了一个「背书小工具」。

这个工具一旦开启就无法停止，只能背诵完毕后才自动停止。

程序里使用了《出师表》这一篇文章，朗诵的语言为普通话版本，当然也可以使用粤语版（见使用说明）。

程序背诵完毕后，将会在程序目录下生成一个 `./背诵文章.mp3` 文件，用于课后复习。

**使用说明：**

`python 背书小工具.py`

> 如要修改背诵的内容，打开：`背书小工具.py`，修改 `content = ` 后的内容。
>
> 如要修改保存的文件名，修改 `engine.save_to_file` 后的名称即可。 
>
> 如要朗诵粤语版，将程序内的第九行取消注释即可。

## 🐦 鸽

众所周知，人类的三大本质之一：**鸽**

日常生活中总有些不想参加的聚会/团建，但经常苦恼于不知如何说出口。

使用该工具生成一个 txt 给他，打开就能领悟你的意思。

<img src="https://gitee.com/daniel_lee25/usefulTools/raw/main/Media/Dove_str.png" alt="show" />

**使用说明：**

1. 运行程序：`python 鸽.py Media/dove.png`
2. 打印一个 **鸽子的字符串图片**，并在该目录下生成该图片：`dove.txt`
3. 发送给朋友即可。
