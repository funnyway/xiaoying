import scrapy 
from scrapy.http import Request 
from xiaoying.items import XiaoyingItem  # 引入item
class DoubanSpider(scrapy.Spider):	
	name = "xiaoying"  #这个name是你必须给它一个唯一的名字  后面我们执行文件时的名字

	start_urls = ["https://www.yingzt.com/invest/list"]	#这个列表中的url可以有多个，它会依次都执行，我们这里简单爬取一个	

	def parse(self,response):#默认函数parse		
		projects = response.xpath('//li[@class="clearfix invalid-project"]|//li[@class="clearfix "]')
		item = XiaoyingItem()  # 实例化item类
		for project in projects:
			item['project_name'] = project.xpath('.//div[@class="info-top"]/a/text()').extract()[0]
			item['project_id'] = item['project_name'].split('·')[1]
			item['year_rate'] = project.xpath('.//p[@class="light-txt"]/text()').extract()[0].split('%')[0]
			item['time_limit'] = project.xpath('.//p/span[@class="big-txt"]/text()').extract()[0]

			amount_p = project.xpath('.//p')[4]
			total_amount = amount_p.xpath('./span/text()').extract()[0].replace(',','')
			amount_unit = amount_p.xpath('./text()').extract()[0]
			if(amount_unit == '万元' ):
				total_amount = str(float(total_amount)*10000)
			item['total_amount'] = total_amount
			yield item
