import os
import re
import time
#import random

def count_files(path):#文件夹数量
    os.chdir(path) #设为当前目录
    files = os.listdir(path) #获取目录下的文件
    print(len(files)) #文件夹文件数量
    return files

def rename_files(files):
    path = os.getcwd()
    for file in files:
        filePath = path.strip('\\') + '\\' + file #空盘符下会出现\\
        print(filePath)#输出原文件名
        #os.rename(file, file[-10:])
        #os.rename(file, str(random.randint(20,300))+'.jpg')

def main():
    path = input('输入路径:\n') #修改文件的路径
    files = count_files(path)
    rename_files(files)
    #time.strftime('%Y%m%d',time.localtime(time.time())) 当前日期

main()
