# -*- coding: utf-8 -*-
import scrapy
import re,requests
from scrapy.http import Request
from lxml import etree
from bs4 import BeautifulSoup

class DingSpider(scrapy.Spider):
    name = 'ding'
    # allowed_domains = ['http://www.23us.com/class/']
    # bash_url="http://www.23us.com/class/"
    # # start_urls = ['http://http://www.23us.com//']
    # def start_requests(self):
    #     for i in range(1,11):
    #         url=self.bash_url+str(i)+'_1.html'
    #         yield Request(url,self.parse)
    # def parse(self, response):
    #     page_source=etree.HTML(response.text)
    #     title=page_source.xpath('//*[@id="left"]/div/div[2]/ul/li/a/text()')
    #     print(title)


    allowed_domains = ['23us.com']
    bash_url = "http://www.23us.com/"

    # start_urls = ['http://http://www.23us.com//']
    def start_requests(self):

        url = self.bash_url+ 'class/1_1.html'
        yield Request(url,self.parse)

    def parse(self, response):
        demo=BeautifulSoup(response.text,'lxml').find_all('tr',bgcolor="#FFFFFF")
        for i in demo:
            title=i.find_all('a')[1]
            print(title)
            # yield Request(title,self.get_name,meta={'key':title})

    # def get_name(self,response):
    #     demo1=BeautifulSoup(response.text,'lxml').find_all('table',id="at")
    #     for a in demo1:
    #         zhangjie1=a.find_all('a')
    #         for b in zhangjie1:
    #             zhangjie=b['href']
    #             yield Request(response.meta['key']+zhangjie,self.contents)
    # def contents(self,response):
    #     demo2=re.compile('<dd id="contents".*?>(.*?)</dd>',re.S)
    #     lists=demo2.findall(response.text)
    #     for j in lists:
    #         content = j.replace('&nbsp;&nbsp;&nbsp;&nbsp;', '').replace('<br />', '')
    #         print(content)

        # demo=re.compile('<tr bgcolor="#FFFFFF">.*?<td.*?><a.*?>(.*?)</a><a.*?>(.*?)</a></td>.*?<td.*?><a.*?>(.*?)</a></td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</tr>',re.S)
        # lists=demo.findall(response.text)
        # for a,b,c,d,e,f,g in lists:
        #     print(a,b,c,d,e,f,g)


        # yuan = requests.get('http://www.23us.com/html/50/50005/').content.decode('gbk')
        # demo = re.compile('<td class="L"><a href="(.*?)">(.*?)</a></td>', re.S)
        # list = demo.findall(yuan)
        # for a, b in list:
        #     the_url = 'http://www.23us.com/html/50/50005/' + a
        #     yuan1 = requests.get(the_url).content.decode('gbk')
        #     demo = re.compile('<h1>(.*?)</h1>.*?<dd id="contents".*?>(.*?)</dd>', re.S)
        #     list1 = demo.findall(yuan1)
        #     for c, d in list1:
        #         contents = c + '\n' + d.replace('&nbsp;&nbsp;&nbsp;&nbsp;', '\t').replace('<br />', '\n')
        #         print(contents)
