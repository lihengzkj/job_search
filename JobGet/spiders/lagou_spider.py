

from scrapy.spiders import Spider
from scrapy import FormRequest
from scrapy.selector import Selector
from JobGet.items import JobgetItem

class LagouSpider(Spider):
    #爬虫名称，执行爬虫时使用
    name = 'lagou'

    headers = {
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.lagou.com/jobs/list_%E5%A4%A7%E6%95%B0%E6%8D%AE?px=default&city=%E6%88%90%E9%83%BD#filterBox'
    }
    allow_domains = ['lagou.com']
    url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%88%90%E9%83%BD&needAddtionalResult=false"
    page = 1
    all_page = 0

    def start_requests(self):
        yield FormRequest(self.url,headers=self.headers,
                          formdata={
                              'first':'false',
                              'pn': str(self.page),
                              'kd': '大数据'
                          }, callback=self.parse)

    def parse(self, response):

        item = JobgetItem()

