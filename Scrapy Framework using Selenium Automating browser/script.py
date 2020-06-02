## Initializing Selenium webdriver using Chrome, Login Internshala.com website using username and password.
## Searching Job via category mention in paramaters.py file and selector from Parsel library 
# extracts all urls of searched job type category. Further we process all collected urls to extract data points.
from time import sleep

import paramaters

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from parsel import Selector

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

# Dumping driver page_source to the selectors, Here we import Selector from Parsel library where
# it has same functionality as of scrapy.selector.
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

print("Internship URL's", job_url)

driver.quit()
