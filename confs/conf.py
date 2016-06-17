# -*- coding: utf-8 -*-
#全部投资公司
conf = {
	'name':'innotree',
    'allowed_domains':["innotree.cn"],
    'start_urls':(
        'http://www.innotree.cn/ajax/projectrank/2/getFilterInvestors?page=[1-461]&size=15&industry=&period=<{period}>&type=-1&keyword=&sort=',
    ),
	'csvpath':'data/',
	'sqlitedb':{
		'dbname':'db/innotree.db'
	},
	#匹配要采集的从列表分析出的连接，以下任选一种//div[@id="project_page"]/span/a/text()
	'list_rule':{
        'rule_xpath':'kkk',
        'rule_reg':r'"id":([1-9]+),"industry"',
        'rule_css':'',
	},
	#拼接列表中获取的url
	'list_url_join':'http://www.innotree.cn/user?utype=1&id=<{0}>',
	'list_interval_time':2,
	'content_interval_time':2,
	
	'index':{
        'period':['种子轮','天使轮','Pre-A轮','A轮','A+轮','B轮','B+轮','C轮','C+轮','D轮','E轮','F轮','G轮','IPO上市及以后','并购','战略投资','未透露']
        
	},
	'isindex':1
}