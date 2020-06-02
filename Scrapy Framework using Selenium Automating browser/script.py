## Initializing Selenium webdriver using Chrome, Login Internshala.com website using username and password.

from time import sleep

import paramaters

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=paramaters.chromedriver_path)
driver.maximize_window()
driver.get(paramaters.base_url)
sleep(5)

# Login tab click
login_button = driver.find_element_by_xpath('//*[@class="nav-item"]/button')
login_button.click()
sleep(1)

# Enter Username/Email ID
user_email = driver.find_element_by_id('modal_email')
user_email.send_keys(paramaters.internshala_user)
sleep(1)

# Enter user password
user_password = driver.find_element_by_id('modal_password')
user_password.send_keys(paramaters.user_password)
sleep(1)

# Sign in click
sign_in_button = driver.find_element_by_id('modal_login_submit')
sign_in_button.click()
sleep(10)

driver.quit()
