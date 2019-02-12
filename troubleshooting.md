## 安装软件
  1. 安装scrapy  
    `pip install Scrapy`

## 安装环境和编码过程中遇到的问题和解决办法

 1. error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools  
    > 解决办法： 根据自己的机器安装 Twisted-18.9.0-cp36-cp36m-win_amd64.whl
    > 参考网址： https://segmentfault.com/a/1190000014782698
 2. ModuleNotFoundError: No module named 'win32api'  
    > download whl file from url:https://pypi.org/project/pypiwin32/#files
    > pip install the whl file
 