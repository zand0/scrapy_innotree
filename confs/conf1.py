# -*- coding: utf-8 -*-
#全部创业公司
conf = {
	'name':'innotree',
    'allowed_domains':["innotree.cn"],
    'start_urls':(
        'http://www.innotree.cn/ajax/projectrank/2/getFilterProjects?page=[1-300]&size=15&industry=&period=<{period}>&area=&keyword=&sort=',
    ),
	'csvpath':'data/',
	'sqlitedb':{
		'dbname':'db/innotree.db'
	},
	#匹配要采集的从列表分析出的连接，以下任选一种//div[@id="project_page"]/span/a/text()
	'list_rule':{
        'rule_xpath':'kkk',
        'rule_reg':r'"],"id":([0-9]+),"industry":"',
        'rule_css':'',
	},
	#拼接列表中获取的url
	'list_url_join':'http://www.innotree.cn/project_extra/detail/<{0}>.html',
	'list_interval_time':2,
	'content_interval_time':2,
	
	'index':{
        'period':['种子轮','天使轮','Pre-A轮','A轮','A+轮','B轮','B+轮','C轮','C+轮','D轮','E轮','F轮','G轮','IPO上市及以后','并购','战略投资','未透露','未融资']
        
	},
	'isindex':1
}