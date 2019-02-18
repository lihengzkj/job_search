## 安装软件
  1. 安装scrapy  
    `pip install Scrapy`
  2. 开启虚拟环境的Python(windows)  
     `cd /path/to/venv/Script/Activate.bat`

## 参考文章链接
   1. https://oner-wv.gitbooks.io/scrapy_zh/content/%E7%AC%AC%E4%B8%80%E6%AD%A5/scrapy%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B.html
   2. https://blog.csdn.net/mr_blued/article/details/79534731
   3. https://blog.csdn.net/qq_33850908/article/details/79120203
   4. https://github.com/fengyuwusong/lagou-scrapy/blob/master/lagou/spiders/lagouSpider.py
   5. https://www.lagou.com/jobs/list_%E5%A4%A7%E6%95%B0%E6%8D%AE?px=default&city=%E6%88%90%E9%83%BD#filterBox
   
## 安装环境和编码过程中遇到的问题和解决办法

 1. error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools  
    > 解决办法： 根据自己的机器安装 Twisted-18.9.0-cp36-cp36m-win_amd64.whl
    > 参考网址： https://segmentfault.com/a/1190000014782698
 2. ModuleNotFoundError: No module named 'win32api'  
    > download whl file from url:https://pypi.org/project/pypiwin32/#files
    > pip install the whl file
 