import os
import re
import time
import sys
#import random

def timeStyle(): #默认返回20190202
    current_time = time.strftime('%Y%m%d', time.localtime(time.time()))#设置时间格式
    return current_time

def count_files(path): #C:\Users\acer1\Desktop(\) 文件夹文件数量,文件名
    os.chdir(path) #设为当前目录
    files = os.listdir(path) #获取目录下的文件名
    return len(files),files

def creatTxt(files):  #默认输出filesNames文件夹
    name = input('文件名输入:\n')
    if not name:
        name = 'filesNames'
    with open(name + '.txt', 'wr') as f:
        f.write('\n'.join(files))
        f.close()
    print('Write Done!')

def oldFilesNames(files): #C:\\Users\\acer1\\Desktop存在问题wanzhengmulu
    oldFilesNames = [os.getcwd() + file for file in files]
    return oldFilesNames

def rename_files(count, files):
    scale, num = 50,0
    print("开 始".center(scale // 2, "-"))
    start = time.perf_counter()
    for file in files:
        os.rename(file, file[-10:])
        # os.rename(file, str(random.randint(20,300))+'.jpg')
        # print(file.strip('.jpg') + '-副本.jpg')
        # os.rename(file, file.strip('.jpg')+ '-副本.jpg')
        # os.rename(file, '({})'.format(num)+' '+file)
        num += 1
        a = '*' * num
        b = '.' * (count - num)
        c = (num / count) * 100
        dur = time.perf_counter() - start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')#count长度
        time.sleep(0.1)
    print("\n" + "结 束".center(scale // 2, '-'))

def main():
    path = input('输入路径:\n') #修改文件的路径
    count, files = count_files(path)#文件夹数量
    rename_files(count, files)#重命名文件

main()
