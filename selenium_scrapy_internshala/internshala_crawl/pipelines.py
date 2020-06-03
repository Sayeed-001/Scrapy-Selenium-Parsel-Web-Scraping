# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

class InternshalaCrawlPipeline:
	def process_item(self, item, spider):
		if item['job_duration']:
			item['job_duration'] = ' '.join(item['job_duration']).strip()
			item['job_duration'] = re.sub("s+"," ", item['job_duration'])
		return item
