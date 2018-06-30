#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 9:05
# @Author  : Shao
# @File    : requests_1.py
# @Desc    :


import sys
import requests
import json


# 输入测试网站，返回结果json串
class TLogin:  # 注意若类名中出现test则pycharm会识别为在执行单元测试
    def __init__(self, url, headers, data):
        self.url = url
        self.headers = headers
        self.data = data

    def get_back(self):
        r = requests.post(self.url, headers=self.headers, data=self.data)
        return r.json()


# 读取本地json文件，返回一个账号密码组合列表
class ReadFile:
    def __init__(self, f_path):
        self.__f_path = f_path

    # def read_file(self):
    #     with open(self.__f_path, 'r', encoding='utf-8') as f:


    def read_file(self):
        with open(self.__f_path, "r", encoding='utf-8') as f:
            f_list = json.load(f)
            f_key = list(f_list.keys())
            f_vlaues = f_list[f_key[0]]  # 第一组
            data = []  # 存储账号名和密码的组合
            for i in f_vlaues:
                for j in f_vlaues:
                    data_item = {
                        "username": i,
                        "password": j
                    }
                    data.append(data_item)
        return data


# 将返回列表保存为文件
class SaveFile:
    pass


if __name__ == '__main__':
    url = "http://localhost:3000/login/loginSub"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "http://localhost:3000/"
    }
    f = ReadFile("D:/projects/python36/Tool-Set/1.json")
    ok_num = 0  # 成功用例计数
    fail_num = 0  # 失败用例计数
    ok_list = []  # 成功用例列表，若为字典的话因为值不同导致被覆盖
    fail_list = []  # 失败用例列表
    data = f.read_file()  # data为账号密码的组合
    for i in data:
        try:
            test_login = TLogin(url, headers, i)
            t_req = test_login.get_back()
            item = dict(t_req, **i)  # 由于字典的键为code 所以会不断进行覆盖，变成了更新而不是拼接
            if t_req["code"] == "200":
                ok_num += 1
                ok_list.append(item)
                # print(item)
            else:
                fail_num += 1
                fail_list.append(item)
                # print(item)
        except:
            print("连接错误！", sys.exc_info()[0])
    print("共测试", ok_num + fail_num, "个用例，其中成功", ok_num, "个，失败", fail_num, "个")
    print("成功的用例为：", ok_list)