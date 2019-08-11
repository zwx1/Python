import requests
import os
from urllib import request
from lxml import etree
import re
from multiprocessing import Process
q = ["李四","王五","张三","赵六","张五","石榴"]
def name(start,end):
#     q = ["李四","王五","张三","赵六","张五","石榴"]
    for i in q:
        url = 'https://www.baidu.com/s?wd=%s&rsv_iqid=0x82c3e88e000bae65&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=12&rsv_sug1=2&rsv_sug7=100&rsv_sug2=0&inputT=3064&rsv_sug4=4964'%i
        response = requests.get(url)
        response.encoding = 'gbk'
        qwe = response.text
        print(qwe)
def main():

    p1 = Process(target=name, args=("李四","张三"))
    p2 = Process(target=name, args=("赵六","石榴"))
    # 获取进程号

    # 启动进程
    p1.start()
    p2.start()

    ##############
    # 进程阻塞.
    p1.join()
    p2.join()
main()



