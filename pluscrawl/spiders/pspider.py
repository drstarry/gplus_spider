from scrapy.spider import BaseSpider
from scrapy.http import FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.shell import inspect_response
from scrapy.http import Request
from time import sleep
import re
from pluscrawl.items import *
from pluscrawl.settings import *
from selenium import webdriver
# from ..items import PluscrawlItem

class LoginSpider(BaseSpider):
    page_incr=0
    rank=0
    end_flag=0

    name = 'pspider'
    # g_ = open('id_lists.dat', 'r')
    start_urls = ['https://plus.google.com/109481621097422977856/about?hl=en']
    # for e in g_:
    #     start_urls.append('https://plus.google.com/'+e.strip()+'/about?hl=en')

    def getFriends(self,hxs):
        friends = []
        results=hxs.select('//div[@class="Ucb  lic d-k-l"]')
        for res in results:
            friendid = res.select('//div@oid').extract()[0]
            friendname = res.select('//div[@clas="o0b"]/a/text()').extract()[0]
            friends.append({'id':friendid,'name':friendname})
        return friends

    def get_id(self, url):
        find_index = url.find("plus.google.com/")
        if find_index >= 0:
            x = url[find_index:].split("/")
            print x[1]
            return x[1]
        return None

    # def get_page(self)
    def parse(self, response):
        print self.URL," ",self.eid
        print "starting phantomjs"

        item = PluscrawlItem()

        dr=webdriver.PhantomJS('/usr/bin/phantomjs')

        #click outfriends list
        dr.get(self.URL)
        while(True):
            try:
                dr.find_element_by_xpath("//span[@class='d-s r5a']").click()
                sleep(10)
            except:
                break

        sou=dr.page_source
        sou2=sou.encode('ascii','ignore')
        hxs = HtmlXPathSelector(text=sou2)
        outfriends = self.getFriends(hxs)
        print outfriends
        # item['outfriends'] = outfriends

        #close outfriends list
        while(True):
            try:
                dr.find_element_by_xpath("//button[@class='d-Cb-Ba d-Cb-U']").click()
                sleep(10)
            except:
                break

        #click infriends list
        while(True):
            try:
                dr.find_element_by_xpath("//span[@class='d-s o5a']").click()
                sleep(10)
            except:
                break

        sou=dr.page_source
        sou2=sou.encode('ascii','ignore')
        hxs = HtmlXPathSelector(text=sou2)
        infriends = self.getFriends(hxs)
        print infriends
        # item['infriends'] = infriends

        #close out friends list
        while(True):
            try:
                dr.find_element_by_xpath("//button[@class='d-Cb-Ba d-Cb-U']").click()
                sleep(10)
            except:
                break


        # item['_id'] = self.get_id(response.url)
        # item['name'] = res.select('//div[@guidedhelpid = "profile_name"]/text()').extract()[0]



        #work
        work_part = res.select('//div[@class = "wna"]')
        for x in work_part:
            if x.select('//div[@class = Cr]/text()').extract() == "Occupation":
                work = x.select('//div[@class = Cr]/text()').extract()
                print work
                # item['work'] = {"privite":"true","Occupation":work}
            else:
                print 'work:privite'
                # item['work'] = {"privite":"false","Occupation":''}

        #edu
        edu_part = res.select('//div[@class = "Ee h5a vna Jqc"]')
        for x in edu_part:
            try:
                edu =  x.select('//div[@class = "PLa"]/text()').extract()
            except:
                print 'edu:privite'
                # item['edu'] = {"privite":"false","edu":[]}
            else:
                item['edu'] = {"privite":"false","edu":edu}

        #links:hard to get......cry~












