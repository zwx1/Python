import re
import requests
from urllib import error
import os
 
num = 0
numPicture = 0
file = ''
List = []
  
def Find(url):
    global List
    #print('正在检测图片总数，请稍等.....')
    t = 0
    i = 1
    s = 0
    while t < 100:
        Url = url + str(t)
        try:
            Result = requests.get(Url, timeout=7)
        except BaseException:
            t = t + 60
            continue
        else:
            result = Result.text
            '''
            findall()方法返回结果是包含一个元素的列表
            find()方法直接返回结果

            findall()方法没有找到目标是返回空列表，find方法找不到目标返回的是none
            '''

            pic_url = re.findall('"objURL":"(.*?)",', result, re.S)  # 先利用正则表达式找到图片url
            s += len(pic_url)
            if len(pic_url) == 0:
                break
            else:
                List.append(pic_url)
                t = t + 60
    return s
  
def dowmloadPicture(html, keyword):
    global num
    # t =0
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url
    print('找到关键词:' + keyword + '的图片，即将开始下载图片')
    for each in pic_url:
        print('正在下载第' + str(num + 1)+ '张图片，' )# 图片地址:' + str(each)
        try:
            if each is not None:
                pic = requests.get(each, timeout=7) # 超时 
            else:
                continue
        except BaseException:
            print('错误，当前图片无法下载')
            continue
        else:
            string = keyword + '_' + str(num) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            num += 1
        if num >= numPicture:
            return
 
 
if __name__ == '__main__':  # 主函数入口
    word = input("请输入搜索关键词: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
    tot = Find(url)
    print('经过检测%s类图片共有%d张' % (word, tot))
    numPicture = int(input('请输入想要下载的图片数量 '))
   
    t = 0
    tmp = url
    while t < numPicture:
        try:
            url = tmp + str(t)
            result = requests.get(url, timeout=10)
            print(url)
        except error.HTTPError as e:
            print('网络错误，请调整网络后重试')
            t = t+60
        else:
            dowmloadPicture(result.text, word)
            t = t + 60
 
    print('当前搜索结束')
 