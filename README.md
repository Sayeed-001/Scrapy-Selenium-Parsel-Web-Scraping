
InternshalaBot
This is a Scrapy project to scrape data points of internship jobs opening from https://internshala.com .
This project is only meant for educational purposes.

Extracted data
This project extracts Internship job data, combined with the respective Company name, Job location, duration, stipend, Last date to apply for a job and extracted url for the job. The extracted data looks like this sample:

{
Job Title : Market Research & Analysis Internship in Bangalore at HR Smartstorey
Company Name : HR Smartstorey
Start Date : Immediately
Job Location : Bangalore
Job Duration : 3 Month
Stipend :  3000 /month
Last Date To Apply : 30 Jun' 20
Url : https://internshala.com/internship/detail/market-research-analysis-internship-in-bangalore-at-hr-smartstorey1591093447 
}

Spiders
This project contains two different programs with different implementation of python libraries such as Scrapy, Parsel and Selenium used for automating the python code. And both the scripts produces same output as shown above. In root directory you will find two folders with name:

1. selenium_parsel_internshala: In this program, employs the code with libraries:
Parsel and selenium
2. selenium_scrapy_internshala: In this program, scrapy framework is implemented to scrap the data and selenium is used to automate the web browser for Login and authentication of webpage.

Both programs extract the same data from the same website and employs with Xpath expressions.
You can learn more about the spiders by going through the Scrapy Tutorial.
NOTE: Before execution of both programs, please make changes in paramates.py file where you need to mention your chromedriver path, your internshala username, internshala password to attempt a login to website with your credentials and at last you have to mention the job_category which you want to search for a job details. 

Running the spiders from selenium_parsel_internshala
You can run a script.py in folder selenium_parsel_internshala by simply run in command line tool:
$ python script.py
Scraped data will be saved to a file in csv format in the same folder:

Running the spiders from selenium_scrapy_internshala
You can run a spider using the scrapy crawl command, such as:
$ scrapy crawl internshala
If you want to save the scraped data to a file, you can pass the -o option:
$ scrapy crawl internshala -o results.csv

