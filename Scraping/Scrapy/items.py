# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BrowseItem(scrapy.Item):
	board_game_rank = scrapy.Field()
	title = scrapy.Field()
	game_sub_url = scrapy.Field()
	geek_rating = scrapy.Field()
	avg_rating = scrapy.Field()
	num_voters = scrapy.Field()
	pass

class CreditItem(scrapy.Item):
	url = scrapy.Field()
	min_players = scrapy.Field()
	max_players = scrapy.Field()
	min_play_time = scrapy.Field()
	max_play_time = scrapy.Field()
	age = scrapy.Field()
	weight = scrapy.Field()
	#category = scrapy.Field()
	#mechanisms = scrapy.Field()
	#family = scrapy.Field()
	pass