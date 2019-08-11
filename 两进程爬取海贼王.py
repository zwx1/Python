import requests
import os
from urllib import request
from lxml import etree
import re
from multiprocessing import Process
def seeking(start,end):
    for i in range(start,end):
        url = 'http://op.hanhande.net/shtml/op_wz/list_2602_%d.shtml'%i
        response = requests.get(url)
        response.encoding = 'gbk'
        qwe = response.text
        html = etree.HTML(qwe)
        #print(HTML)
        q = html.xpath('//*[@id="main"]/div[2]/div[2]/ul/li/a/img/@src')
        for i in q:
            print(i)
            r = requests.get(i)
            print(r)
            root = "/Users/zwx/ZWXX/python/python_胡/picture/"
            path=root+"海贼王"+ i.split('/')[-1]
            with open(path,'wb') as f:
                f.write(r.content)
def main():
    
    p1 = Process(target=seeking, args=(1,2))
    p2 = Process(target=seeking, args=(2,3))
    # 获取进程号

    # 启动进程
    p1.start()
    p2.start()

    ##############
    # 进程阻塞.
    p1.join()
    p2.join()
main()