# bilidownload
**本项目通过requests和DrissionPage实现对[bilibili](https://www.bilibili.com)的视频以及音频的获取**




## 主要运行环境
*python 3.8，drissionpage 3.2.31*
## 运行方法

*项目包含两个文件，即gui.py和dl.py，gui.py为主文件，运行后将在本地打开交互界面.*

## 说明
由于音频页面为动态页面，requests的方法无法获取到音频的源链接，故改用DrissionPage模拟移动端进行访问和源码获取.

## V 1.0
完成了主要功能的实现，包括获取视频和音频内容保存于本地，但目前得到的视频为无音轨的纯画面部分.

> 注：请勿使用VPN等工具，可能会引起错误
