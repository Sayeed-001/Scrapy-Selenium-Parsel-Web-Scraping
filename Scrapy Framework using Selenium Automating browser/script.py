## Initializing Selenium webdriver using Chrome, Login Internshala.com website using username and password.

from time import sleep
import re

import paramaters

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from parsel import Selector

# Validating the extract data points, if the scrapped item is empty, then this fn will assign nan value.
def validate_field(field):
	if field:
		pass
	else:
		field = 'nan'
	return field

# configure Chrome Webdriver
# Add additional Options to the webdriver
chrome_options = Options()
# add the argument and make the browser Headless.
#chrome_options.headless =True
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(executable_path=paramaters.chromedriver_path,options=chrome_options)
driver.implicitly_wait(6)
driver.get(paramaters.base_url)
sleep(5)

# Login tab click
login_button = driver.find_element_by_xpath('//*[@class="nav-item"]/button')
login_button.click()
sleep(2)

# Enter Username/Email ID
user_email = driver.find_element_by_id('modal_email')
user_email.send_keys(paramaters.internshala_user)
sleep(2)

# Enter user password
user_password = driver.find_element_by_id('modal_password')
user_password.send_keys(paramaters.user_password)
sleep(2)

# Sign in click
sign_in_button = driver.find_element_by_id('modal_login_submit')
sign_in_button.click()
sleep(10)

# If you previously checked the preferences on filters section on webpage the uncomment me.
#uncheck_preferences = driver.find_element_by_xpath('//*[@id="matching_preference_label"]')
#uncheck_preferences.click()
#sleep(2)

# Selecting the job category, check and select the available jobs categorys from paramaters.py file
category_element = driver.find_element_by_xpath('//*[contains(@id,"select_category_chosen")]')
category_element.click()
sleep(2)
enter_category = driver.find_element_by_xpath('//*[@id="select_category_chosen"]/ul/li/input')
enter_category.send_keys(paramaters.JOB_CATEGORY, Keys.RETURN)
sleep(3)

# Dumping driver page_source to the selectors, Here we import Selector from Parsel library whereas same
# functionality as of scrapy.selector.
sel = Selector(text=driver.page_source)

# Extract 1st page job urls and save to job_url variable
urls = sel.xpath('//*[@class="heading_4_5 profile"]/a/@href').extract()[:5]
#for url in urls:
#	job_url = "https://internshala.com" + url
job_url = ['https://internshala.com'+url for url in urls]	

# navigate to next page
next_page = driver.find_element_by_xpath("//a[@id='next']")
next_page.click()
sleep(3)

# Extract next page job urls. 
urls = sel.xpath('//*[@class="heading_4_5 profile"]/a/@href').extract()[:3]
#for url in urls:
#	job_url = "https://internshala.com" + url
job_url_next_page = ['https://internshala.com'+url for url in urls]

job_url.extend(job_url_next_page)  # Here we append/extend all urls of next page to the variable name job_url


# Iterate over each url to extract data points from webpage.
for target_url in job_url:
	driver.get(target_url)
	sleep(3)

	sel = Selector(text=driver.page_source)  # Initializing the Selector from Parsel library shows same functionality as of scrapy.selector
	
	
	job_header =  sel.xpath('normalize-space(//*[@id="details_container"]/div[2]/text())').extract_first()  # Job Heading
	
	company_name = sel.xpath('normalize-space(//*[@class="heading_6 company_name"]/a/text())').extract_first()  # Company Name
	
	start_date = sel.xpath('//*[@class="start_immediately_desktop"]/text()').extract_first()  # Job Joining Date
	
	job_location = sel.xpath('//*[@class="location_link"]/text()').extract_first()  # Job Location
	
	
	job_duration = sel.xpath('//*[@class="other_detail_item "]/div[2]/text()').extract()  # Internship duration
	if job_duration:
		job_duration = ' '.join(job_duration).strip()
		job_duration = re.sub("s+"," ", job_duration)

	
	stipend = sel.xpath('//*[@class="other_detail_item  stipend_container"]/div[2]/span/text()').extract_first()   # Salary Offered
	
	apply_by = sel.xpath('//*[@class="other_detail_item  apply_by"]/div[2]/text()').extract_first()  # Last Date To Apply
	
	url = driver.current_url  # extracts the current URL of Job type
	
	# Here Validating each scraped item whether the field is empty or filled 
	job_header = validate_field(job_header)
	company_name = validate_field(company_name)
	start_date = validate_field(start_date)
	job_location = validate_field(job_location)
	job_duration = validate_field(job_duration)
	stipend = validate_field(stipend)
	apply_by = validate_field(apply_by)
	url = validate_field(url)
	
	# Printing the scraped variables, scraped items will be displayed on command line during execution of a program
	print('\n')
	print('Job Title :',  job_header)
	print('Company Name :',  company_name)
	print('Start Date :', start_date)
	print('Job Location :', job_location)
	print('Job Duration :', job_duration)
	print('Stipend :',  stipend)
	print('Last Date To Apply :', apply_by)
	print('Url :', url)
	print('\n')


driver.quit()
