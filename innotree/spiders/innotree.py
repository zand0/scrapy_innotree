# -*- coding: utf-8 -*-
import scrapy
import os
import re
import time
from confs.conf import conf
from lib.SQLHelper import Sqlite3Helper
from lib import util

class InnotreeSpider(scrapy.Spider):
    name = conf['name']
    allowed_domains = conf['allowed_domains']
    start_urls = util.parseListUrl(conf['start_urls'])
    #pagefile = []
    #csvpath = conf['csvpath']+'page.csv'
    sqlite = ''
    sqlhelper = ''
    def __init__(self):
        self.sqlite = Sqlite3Helper()
        self.sqlhelper = self.sqlite

    def parse(self, response):
        print 'start get list url...'
        print response.url
        match = re.findall(conf['list_rule']['rule_reg'],response.body,re.M|re.I)
        for i in match:
            time.sleep(conf['list_interval_time'])
            #print i
            self.getListUrl(i)
            #yield scrapy.Request()
        '''r = self.sqlite.fetchall("select id,url from pre_list where status=0")
        print 'start get detail content...'
        for i in r:
            time.sleep(conf['content_interval_time'])
            yield scrapy.Request(url=str(i[1]), callback=self.parse_contents)
            #break'''
 
    def parse_contents(self,response):
        url = response.url
        html = response.body
        if url and html:
            print url
            self.sqlite.execute("insert into pre_html (html,from_url)values(?,?)",(unicode(html,'utf-8'),unicode(url,'utf-8')))
            self.sqlite.execute("update pre_list set status=1 where url=?",(unicode(url,'utf-8'),))

    def getListUrl(self,val):
            url =  conf['list_url_join'].replace('<{0}>',val)
            print url
            #print self.sqlite.fetch("select id from pre_list where url='"+url+"'")
            if self.sqlite.fetch("select id from pre_list where url='"+url+"'")==None:
                self.sqlite.execute("insert into pre_list ('url','status') values ('"+url+"',0)")
