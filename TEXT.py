import os
from traceback import print_tb 
input_path = input('path:')
if os.path.exists(input_path + '/TEXT.py'):
    print('目录存在')
else:
    print('不存在')
