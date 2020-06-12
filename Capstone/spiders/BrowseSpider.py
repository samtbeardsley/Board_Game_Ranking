import scrapy
from Capstone.items import BrowseItem
import requests

class BrowseSpider(scrapy.Spider):
	name = "browse"

	def start_requests(self):
		urls = ['https://boardgamegeek.com/browse/boardgame/page/1']
		
		npages = 1
		
		for i in range(1, npages):
			urls.append("https://boardgamegeek.com/browse/boardgame/page/"+str(i+1)+"")
			
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
			n = 0
			y = 0
			while n < 100:
				for sel in response.xpath('//table'):
					item = BrowseItem()
					item['board_game_rank'] = response.xpath('//tr/td/a[@name]')[n].extract()
					item['title'] = response.xpath('//tr/td/div/a[@href]/text()')[n].extract()
					item['game_sub_url'] = response.xpath('//tr/td/div/a/@href')[n].extract()
					item['geek_rating'] = response.xpath('//tr/td[contains(@class,"collection_bggrating")]/text()')[y].extract()
					item['avg_rating'] = response.xpath('//tr/td[contains(@class,"collection_bggrating")]/text()')[y+1].extract()
					item['num_voters'] = response.xpath('//tr/td[contains(@class,"collection_bggrating")]/text()')[y+2].extract()
					n += 1
					y += 3
					yield item
           