import os
import re
import random

def rename_file(path):
    os.chdir(path) #设为当前目录
    files = os.listdir(path) #获取目录下的文件
    for file in files:
        filePath = path + '\\' + file
        print(filePath)
        os.rename(file, str(random.randint(20,300))+'.jpg')
#    print(os.getcwd())

def main():
    path = input('输入路径:\n') #修改文件的路径
    rename_file(path)

main()
