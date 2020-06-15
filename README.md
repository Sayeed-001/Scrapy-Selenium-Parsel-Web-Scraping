# Interns Job Crawler
This code example will scrape data points from internship jobs opening on https://internshala.com by using Selenium webdriver for automating the web browse. This website requires login credentials to make any search. Selenium is used here for login purpose and will navigate to target urls for data scraping. Parsel Library used Selectors for extracting data points urls from the web page. Both these packages work very smoothly and extracts clean data in csv format.

This project is only meant for educational purposes.

## Extracted data
This project extracts Internship job data, combined with the respective Company name, Job location, duration, stipend, Last date to apply for a job and extracted url for the job. The extracted data looks like this sample:
```
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
```
### Selenium_parsel_internshala: In this program, employs the code with libraries:
### Parsel and selenium

#### NOTE: 
Before execution of both programs, please make changes in paramates.py file where you need to mention your chromedriver path, your internshala username, internshala password to attempt a login to website with your credentials and at last you have to mention the job_category which you want to search for a job details. 
```
## Running the program from selenium_parsel_internshala
You can run a script.py in folder selenium_parsel_internshala by simply run in command line tool:
$ python script.py
Scraped data will be saved to a file in csv format in the same folder:
```
