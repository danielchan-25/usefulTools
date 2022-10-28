import os,time,ffmpy3
from cv2 import split
from re import U

def check(video_path):
    if os.path.exists(video_path + 'title.mp4'):
        print('已检测到片头视频文件')
    else:
        print('[ERROR] 检测不到片头视频文件，或者将片头视频文件重命名为：title.mp4')
        os._exit()
    if os.path.exists(video_path + 'video'):
        print('已检测到 video/ 目录')
    else:
        print('未检测到 video/ 目录，请创建该目录，并将需要处理的视频存放进去')
        os._exit()
    if os.path.exists(video_path + 'tmp_video'):
        print('已检测到 tmp_video/ 目录')
    else:
        print('未检测到 tmp_video/ 目录，正在创建')
        os.mkdir(video_path + 'tmp_video/')
    if os.path.exists(video_path + 'done_video'):
        print('已检测到 done_video/ 目录')
    else:
        print('未检测到 done_video/ 目录，正在创建')
        os.mkdir(video_path + 'done_video/')

def make_title(video_path):
    # 片头视频URL地址
    title_video_path = video_path + 'title.mp4'
    title_video_translate_path = video_path + 'title.ts'
    # 转码为 title.ts
    transcode_title = 'ffmpeg -i\t' + title_video_path + '\t'+ title_video_translate_path
    os.system(transcode_title)

def add_pink(video_path):
    # 视频URL地址
    tmp_video = input_path + 'tmp_video/'
    video_path = video_path + 'video/'
    video_list = os.listdir(video_path)
    # 添加粉边，并转码为ts文件
    for i in video_list:
        video_url = video_path + i
        transcode_add_pink = 'ffmpeg -i\t' + video_url + "\t-vf 'scale=1408:1056,pad=1920:1080:256:12:#fcccd4'\t" + tmp_video + i + '.ts'
        print(transcode_add_pink)
        os.system(transcode_add_pink)

def merge_video(video_path):
    # 合并两个ts文件
    title_video_path = input_path + 'title.ts'
    tmp_path = os.listdir(input_path + 'tmp_video/')
    done_path = input_path + 'done_video/'
    for i in tmp_path:
        video_url = input_path + 'tmp_video/' + i
        merge = 'ffmpeg -i "concat:' + title_video_path + '|' + video_url + '" -c copy\t' + done_path + i + '.mp4'
        os.system(merge)

input_path = input('输入视频目录的地址：')
check(video_path=input_path)
make_title(video_path=input_path)
add_pink(video_path=input_path)
merge_video(video_path=input_path)