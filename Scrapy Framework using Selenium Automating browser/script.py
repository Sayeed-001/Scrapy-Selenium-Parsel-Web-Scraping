## Initializing Selenium webdriver using Chrome, Login Internshala.com website using username and password.

from time import sleep

import paramaters

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# configure Chrome Webdriver
# Add additional Options to the webdriver
chrome_options = Options()
# add the argument and make the browser Headless.
#chrome_options.headless =True
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(executable_path=paramaters.chromedriver_path, options=chrome_options)
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

driver.quit()
