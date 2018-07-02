import tkinter as tk
import tkinter.ttk as ttk
import sys
import tkinter.filedialog
import json

if __name__ == '__main__':
    main()


class Tools:

    # def __init__(sel 
    # 文件选择，更新选择按钮前的Entry内的内容，传入的en为
    def selectPath(en):
            path = tkinter.filedialog.askopenfilename()
            en.set(path)


    # def read_file(self):
    #     with open(self.__f_path, 'r', encoding='utf-8') as f:
    # 传入一个json格式路径，以列表形式返回该文件
    def returnJson2List(file_path):
        try:
            with open(file_path, "r", encoding='utf-8') as f:
                f_list = json.load(f)
                f_key = list(f_list.keys())
                f_vlaues = f_list[f_key[0]]  # 第一组
                data = []  # 存储账号名和密码的组合
                for i in f_vlaues:
                    data.append(i)
            return data
        except:
            print("文件读取错误！0")