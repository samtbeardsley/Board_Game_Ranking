import scrapy
from Capstone.items import CreditItem
import requests
import re

min_players_pattern = r'minplayers":"\d*'
max_players_pattern = r'maxplayers":"\d*'
min_play_time_pattern = r'minplaytime":"\d*'
max_play_time_pattern = r'maxplaytime":"\d*'
age_pattern = r'minage":"\d*'
mechanisms_pattern = r'\\/boardgamemechanic\\/([^\"]+)'
category_pattern = r'\\/boardgamecategory\\/([^\"]+)'
family_pattern = r'\\/boardgamefamily\\/([^\"]+)'
weight_pattern = r'"averageweight":\d\.\d*'

class CreditSpider(scrapy.Spider):
    name = "credit"

    def start_requests(self):
        urls = ['https://boardgamegeek.com/boardgame/174430/gloomhaven/credits',
                'https://boardgamegeek.com/boardgame/174430/gloomhaven/credits',
                'https://boardgamegeek.com/boardgame/161936/pandemic-legacy-season-1/credits',
                'https://boardgamegeek.com/boardgame/38453/space-alert/credits',
                'https://boardgamegeek.com/boardgame/95064/ascension-return-fallen/credits',
                'https://boardgamegeek.com/boardgame/221965/fox-forest/credits'
               ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        item = CreditItem()
        item['url'] = response.url
        item['min_players'] = re.findall(min_players_pattern, response.text)
        item['max_players'] = re.findall(max_players_pattern, response.text)
        item['min_play_time'] = re.findall(min_play_time_pattern, response.text)
        item['max_play_time'] = re.findall(max_play_time_pattern, response.text)
        item['age'] = re.findall(age_pattern, response.text)
        item['weight'] = re.findall(weight_pattern, response.text)
        item['category'] = re.findall(category_pattern, response.text)
        item['mechanisms'] = re.findall(mechanisms_pattern, response.text)
        item['family'] = re.findall(family_pattern, response.text)
        yield item