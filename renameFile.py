import os
import re
import time
import sys
#import random

def time_style():
    current_time = time.strftime('%Y%m%d', time.localtime(time.time()))#设置时间格式
    return current_time

def count_files(path):
    os.chdir(path) #设为当前目录
    files = os.listdir(path) #获取目录下的文件
    print(len(files)) #文件夹文件数量
    return files

def rename_files(files):
    path = os.getcwd()
    for file in files:
        filePath = path.strip('\\') + '\\' + file #空盘符下会出现\\strip()
        print(filePath)#输出原文件名
        #os.rename(file, file[-10:])
        #os.rename(file, str(random.randint(20,300))+'.jpg')

def ielts_process(file_name):
    current_time = time_style()
    file_call = file_name.split('\\')[-1]
    current_path = '\\'.join(file_name.split('\\')[:-1])
#    print(current_path)
    os.chdir(current_path)
#    print(os.getcwd())
    new_file = current_time + '_' + file_call
    print(new_file)
    with open(file_name, 'r') as f:
        lines = f.read().split('\n\n')
        f.close()

    with open(new_file, 'w') as g:
        g.write('\n'.join(lines))
        g.close()
    print('JobDone!')

def ielts_web(lines):#去除多行输入的空行
    current_time = time_style()
    creat_file = 'C:\\Users\\acer1\Desktop\\' + current_time + '_ielts.txt'  # 文件保存目录
    # os.path.normpath(creat_file) 路径示例C:\Users
    new_lines = [line for line in lines if not line is '\n']#去除单个'\n'元素
    with open(creat_file, 'w') as f:#保存至桌面文件
        f.write(''.join(new_lines))
        f.close()
    print('JobDone!')

def main():
    path = input('输入路径:\n') #修改文件的路径
    #lines = sys.stdin.readlines()#多行输入ctrlD结束
    #ielts_web(lines)
    files = count_files(path)#文件夹数量
    #rename_files(files)#重命名文件
    #ielts_web(txt)

main()
