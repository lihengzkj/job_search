'''

必须是scrapy.Spider的子类

'''

import scrapy

class QuotesSpider(scrapy.Spider):

    name = 'quotes'
    #start_requests()：必须返回一个可迭代的 Requests
    # （您可以返回一个 request 列表或写一个生成器函数），Spider将开始抓取。
    # 后续请求将从这些初始请求中连续生成。
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #parse()：被调用来处理 response 的方法， response 由每个 request 下载生成。
    # response 参数是一个 TextResponse 的实例，
    # 它保存页面内容，并具有更多有用的方法来处理它。
    # parse() 方法通常解析 response ，
    # 将抓取的数据提取为 dicts，并查找要跟进的新 URL 并从中创建新请求（Request）。
    def parse(self, response):
        page = response.url.split('/')[2]
        print('page:',page)

        file_name = 'quotes-%s.html' % page
        print('file_name:', file_name)

        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % file_name)
