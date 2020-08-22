# save below into CreditSpider.py

import scrapy
from Capstone.items import CreditItem
import requests
import re
import pandas as pd

min_players_pattern = r'minplayers":"\d*'
max_players_pattern = r'maxplayers":"\d*'
min_play_time_pattern = r'minplaytime":"\d*'
max_play_time_pattern = r'maxplaytime":"\d*'
age_pattern = r'minage":"\d*'
weight_dec_pattern = r'"averageweight":\d\.\d*'
weight_pattern = r'"averageweight":\d'
#mechanisms_pattern = r'\\/boardgamemechanic\\/([^\"]+)'
#category_pattern = r'\\/boardgamecategory\\/([^\"]+)'
#family_pattern = r'\\/boardgamefamily\\/([^\"]+)'

df = pd.read_csv('browse_split1.csv')
# split browse data into 10 files to run in batches
s = df.full_game_url

class CreditSpider(scrapy.Spider):
    name = "credit"

    def start_requests(self):
        urls = s.tolist()
        
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
        if re.findall(weight_dec_pattern, response.text) != []:
            item['weight'] = re.findall(weight_dec_pattern, response.text)
        else:
            item['weight'] = re.findall(weight_pattern, response.text)
        #item['category'] = re.findall(category_pattern, response.text)
        #item['mechanisms'] = re.findall(mechanisms_pattern, response.text)
        #item['family'] = re.findall(family_pattern, response.text)
        yield item

# use this command to execute this spider in the command line and save data to csv
#scrapy crawl credit -o credit.csv
