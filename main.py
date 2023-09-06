import requests
import re
import json
import io
from DrissionPage import WebPage, ChromiumPage
from DrissionPage import ChromiumOptions
from selenium import webdriver

headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
     "referer": "https://message.bilibili.com/"}

headers1 = {"User-Agent":'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}

def get_url_html(url):
    req=requests.get(url,headers=headers)
    htmltext=req.text
    get_json(htmltext, url)

def get_url_audio(url):
    options = ChromiumOptions().set_user_agent(headers1["User-Agent"])
    options.set_headless(True)
    page = ChromiumPage(addr_driver_opts=options)
    page.get(url)
    htmltext = page.html
    with open("test.txt","w",encoding="utf-8") as f:
        f.write(htmltext)
    page.quit()
    get_json1(htmltext, url)

def get_json(htmltxt, url):
    '''with open("test1.txt","r",encoding="utf-8") as f:
        htmltxt=f.read()'''
    r=re.findall(r'<script>window.__playinfo__=(.*?)</script>',htmltxt)[0]
    print(r)
    js=json.loads(r)
    audiourl=js["data"]["dash"]["audio"][0]["base_url"]
    videourl=js["data"]["dash"]["video"][0]["base_url"]
    exit(0)
    download(audiourl,videourl, url)

def get_json1(htmltxt, url):
    r=re.findall(r'window.__INITIAL_STATE__ = (.*)};',htmltxt)
    print("输出完毕:",r[0],sep="")
    print("输出完毕:",type(r))
    js=json.loads(r[0]+"}")
    audiourl=js["reduxAsyncConnect"]["audioInfo"]["urls"][0]
    download1(audiourl, url)

def download(audiourl,videourl, url):
    res=requests.get(url=audiourl,headers=headers)
    print('爬取中，等待....')
    with open(url[url.find("o/")+2:]+".mp3","wb") as f:
         f.write(res.content)
    print('爬取完毕！')

def download1(audiourl, url1):
    res=requests.get(url=audiourl,headers=headers1)
    print('爬取中，等待....')
    with open(url1[url1.find("o/")+2:]+".mp3","wb") as f:
         f.write(res.content)
    print('爬取完毕！')

if __name__=="__main__":
    str1=input("输入BV号或au号(区分大小写)：")
    if str1[0:2]=="BV":
        str2='https://www.bilibili.com/video/'+str1
        get_url_html(str2)
    elif str1[0:2]=="au":
        str2='https://www.bilibili.com/audio/'+str1
        get_url_audio(str2)
    else:
        print("请检查输入是否正确并重启程序")