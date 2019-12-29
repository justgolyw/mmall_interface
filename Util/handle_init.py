#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys, os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)

class HandleInit:
     # 加载配置文件
     def load_init(self):
         # os.path.abspath(os.path.join(base_path,'..'))获取上级目录
        file_path = os.path.abspath(os.path.join(base_path,'..')) + "/Config/server.ini"
        cf = configparser.ConfigParser()
        # 读取配置文件
        cf.read(file_path, encoding="utf-8")
        return cf

     # 获取ini文件里面的值
     def get_value(self, key, node=None):
        if node == None:
            node = "server"
        cf = self.load_init()
        try:
            data = cf.get(node, key)
        except Exception:
            print("没有获取到值")
            data = None
        return data

handle_init = HandleInit()
if __name__ == '__main__':
    print(handle_init.get_value("host"))


