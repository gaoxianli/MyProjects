#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: spider_framework.py
#Author: kernellmd 
#Created Time: 2018-05-31 22:21:29
############################  

import requests
import traceback

def getHTMLText(url):
    #网络连接容易出现异常，需要进行异常处理
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  #如果状态不是200，引发HTTPError异常
        #此处解析文档的编码方式要花费大量时间，定向爬虫可以用手工方式，
        #先获得网站的编码方式，然后直接赋值到enconding属性
        r.encoding = r.apparent_encoding
        return r.text
    except Exception:
        #return repr(e)
        print("爬取失败")
        traceback.print_exc()

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))