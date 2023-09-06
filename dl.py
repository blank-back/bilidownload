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

def get_url_html(url, ver=0):
    req=requests.get(url,headers=headers)
    htmltext=req.text
    get_json(htmltext, url, ver)

def get_url_audio(url):
    options = ChromiumOptions().set_user_agent(headers1["User-Agent"])
    options.set_headless(True)
    page = ChromiumPage(addr_driver_opts=options)
    page.get(url)
    htmltext = page.html
    page.quit()
    get_json1(htmltext, url)

def get_json(htmltxt, url, ver):
    r=re.findall(r'<script>window.__playinfo__=(.*?)</script>',htmltxt)[0]
    js=json.loads(r)
    audiourl=js["data"]["dash"]["audio"][0]["base_url"]
    videourl=js["data"]["dash"]["video"][0]["base_url"]
    download(audiourl,videourl, url, ver)

def get_json1(htmltxt, url):
    r=re.findall(r'window.__INITIAL_STATE__ = (.*)};',htmltxt)[0]
    js=json.loads(r+"}")
    audiourl=js["reduxAsyncConnect"]["audioInfo"]["urls"][0]
    download1(audiourl, url)

def download(audiourl,videourl, url, ver):
    if ver==0:
        res=requests.get(url=audiourl,headers=headers)
        namestr = url[url.find("o/") + 2:] + ".mp3"
    else:
        res=requests.get(url=videourl,headers=headers)
        namestr=url[url.find("o/")+2:]+".mp4"
    with open(namestr,"wb") as f:
         f.write(res.content)

def download1(audiourl, url1):
    res=requests.get(url=audiourl,headers=headers1)
    with open(url1[url1.find("o/")+2:]+".mp3","wb") as f:
         f.write(res.content)


