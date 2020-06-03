
# -*- coding: utf-8 -*-
from time import sleep

from internshala_crawl import paramaters
from internshala_crawl.items import InternshalaCrawlItem, validate_field

from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

		  
class InternshalaSpider(Spider):
	name = 'internshala'
	allowed_domains = ['internshala.com']


	def start_requests(self):

		# configure Chrome Webdriver
		# Add additional Options to the webdriver
		chrome_options = webdriver.ChromeOptions()
		# add the argument and make the browser Headless.
		#chrome_options.headless =True
		chrome_options.add_argument('--disable-gpu')
		chrome_options.add_argument("start-maximized")
		chrome_options.add_argument("--disable-extensions")

		self.driver = webdriver.Chrome(executable_path=paramaters.chromedriver_path,options=chrome_options)
		self.driver.implicitly_wait(6)
		self.driver.get(paramaters.url)
		
		login_button = self.driver.find_element_by_xpath('//*[@class="nav-item"]/button')
		login_button.click()
		sleep(2)
	
		user_email = self.driver.find_element_by_id('modal_email')
		user_email.send_keys(paramaters.internshala_user)
		sleep(2)
		
		user_password = self.driver.find_element_by_id('modal_password')
		user_password.send_keys(paramaters.user_password)
		sleep(2)
		
		sign_in_button = self.driver.find_element_by_id('modal_login_submit')
		sign_in_button.click()
		sleep(3)
		self.logger.info("User Successfully Login.")
	
		#Online_trainng_page = self.driver.find_element_by_xpath('//*[@id="dropdown"]/ul/li[2]/a')
		#Online_trainng_page.click()
	
		#uncheck_preferences = self.driver.find_element_by_xpath('//*[@id="matching_preference_label"]')
		#uncheck_preferences.click()

		# This gives the names of the categorys available to search a job. output of this command is given in paramaters.py file for reference 
		# available_categorys = sel.xpath('//*[@id="select_category_chosen"]/div/ul/li/text()').extract() 
		
		select_category = self.driver.find_element_by_xpath('//*[@id="select_category_chosen"]')
		select_category.click()
		sleep(2)
	
		enter_category = self.driver.find_element_by_xpath('//*[@id="select_category_chosen"]/ul/li/input')
		enter_category.send_keys(paramaters.JOB_CATEGORY, Keys.RETURN)
		sleep(2)
		self.logger.info("Category Searched Successfully.")

		sel = Selector(text=self.driver.page_source)

		urls = sel.xpath('//*[@class="heading_4_5 profile"]/a/@href').extract()
		for job in urls:
			absolute_job_url = paramaters.url + job
			yield Request(absolute_job_url, callback=self.parse_intern)
		
		next_page_link = None

		while not next_page_link:
			try:
				next_page_link = self.driver.find_element_by_xpath("//a[@id='next']")
				next_page_link.click()
				self.logger.info("Sleeping for 3 seconds.")
				sleep(3)

				sel = Selector(text=self.driver.page_source)
				urls = sel.xpath('//*[@class="heading_4_5 profile"]/a/@href').extract()
				for job in urls:
					absolute_job_url_two = paramaters.url + job
					yield Request(absolute_job_url_two, callback=self.parse_intern)
					self.logger.info('Job URLs Scraped Successfully.')
			except NoSuchElementException:
				self.logger.info("No more pages to load.")
				break

		self.driver.quit()
	
	def parse_intern(self, response):
		
		l = ItemLoader(item=InternshalaCrawlItem(), response=response)

		job_header =  response.xpath('normalize-space(//*[@id="details_container"]/div[2]/text())').extract_first()

		company_name = response.xpath('normalize-space(//*[@class="heading_6 company_name"]/a/text())').extract_first()

		start_date = response.xpath('//*[@class="start_immediately_desktop"]/text()').extract_first()

		job_location = response.xpath('//*[@class="location_link"]/text()').extract_first()

		job_duration = response.xpath('//*[@class="other_detail_item "]/div[2]/text()').extract()

		stipend = response.xpath('//*[@class="other_detail_item  stipend_container"]/div[2]/span/text()').extract_first()
	
		apply_by = response.xpath('//*[@class="other_detail_item  apply_by"]/div[2]/text()').extract_first()

		visited_url = response.url

		job_header = validate_field(job_header)
		company_name = validate_field(company_name)
		start_date = validate_field(start_date)
		job_location = validate_field(job_location)
		job_duration = validate_field(job_duration)
		stipend = validate_field(stipend)
		apply_by = validate_field(apply_by)
		visited_url = validate_field(visited_url)

		l.add_value('job_header', job_header)
		l.add_value('company_name', company_name)
		l.add_value('start_date', start_date)
		l.add_value('job_location', job_location)
		l.add_value('job_duration', job_duration)
		l.add_value('stipend', stipend)
		l.add_value('apply_by', apply_by)
		l.add_value('visited_url', visited_url)

		return l.load_item()