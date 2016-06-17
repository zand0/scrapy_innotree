# -*- coding: utf-8 -*-
import scrapy
import time
import urllib2
import os
from confs.conf1 import conf
from lib.SQLHelper import Sqlite3Helper
from lib import util

class SavehtmlSpider(scrapy.Spider):
    name = "savehtml"
    allowed_domains = ["innotree.cn"]
    start_urls = (
        'http://www.innotree.cn/',
    )
    flag='file'
    sqlite = ''
    sqlhelper = ''
    def __init__(self):
        self.sqlite = Sqlite3Helper()
        self.sqlhelper = self.sqlite

    def parse(self, response):
        r = self.sqlite.fetchall("select id,url from pre_list where status=0")
        for e in r:
            time.sleep(conf['content_interval_time'])
            if self.flag=='file':
                if os.path.exists('data/'+str(e[0])+'.html')!=True:
                    self.parse_content2('data/'+str(e[0])+'.html',e[1])
            else:
                yield scrapy.Request(url=str(e[1]), callback=self.parse_content)
        
    
    def parse_content(self,response):
        url = response.url
        html = response.body
        if url and html:
            print url
            html = unicode(html,'utf-8').lstrip()
            url = unicode(url,'utf-8')
            self.sqlite.execute("insert into pre_html (html,from_url)values(?,?)",(html,url))
            self.sqlite.execute("update pre_list set status=1 where url=?",(url,))

    def parse_content2(self,path,url):
        print url
        response = urllib2.urlopen(url) 
        html = response.read()
        f = open(path, 'w')
        f.writelines(html)
        f.close( )
        #url = unicode(url,'utf-8')
        self.sqlite.execute("update pre_list set status=1 where url=?",(url,))