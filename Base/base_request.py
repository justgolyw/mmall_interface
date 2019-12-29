#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import sys, os
import requests
from Util.handle_init import handle_init

base_path = os.getcwd()
sys.path.append(base_path)

class BaseRequest:

    # post请求
    def send_post(self, url, data):
        response = requests.post(url=url, data=data)
        res = response.text
        return res

    # get请求
    def send_get(self,url, data):
        response = requests.get(url=url, params=data)
        res = response.text
        return res


    def run_main(self, method, url, data):
        base_url = handle_init.get_value("host")
        if "http" not in url:
            url = base_url + url
            print(url)

        if method == "get":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        # str类型的数据转成dict
        res = json.loads(res)
        return res

request = BaseRequest()

if __name__ == '__main__':
    res = request.run_main('post', "/user/login.do", {"username":"admin","password":"admin"})
    print(res["status"])



