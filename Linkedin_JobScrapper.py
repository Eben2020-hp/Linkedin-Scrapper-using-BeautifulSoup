## Install necessary packages
# pip install beautifulsoup4
# pip install lxml
# pip install requests

## Import necessary packages
import requests                 ### Request information from a website
from bs4 import BeautifulSoup

## Request information from a website for a Particular Job and Location (Bangalore)
keyword = input("Enter your Job of Interest: ").lower()
location = "Bangalore Urban, Karnataka, India"          ### We will give the default location

html_text = requests.get(f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location={location}").text      ### Inorder to get the HTML text from the website.
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('div', class_='base-card base-card--link base-search-card base-search-card--link job-search-card')
for job in jobs:
    try:
        job_role = job.find('h3', class_='base-search-card__title').text.replace(' ','').strip('\n')     ### Remove white spaces and new lines.
        company_name = job.find('h4', class_='base-search-card__subtitle').text.replace(' ','').strip('\n')    
        more_info = job.find('a', class_='base-card__full-link')['href']
        post_time = job.find('time', class_=['job-search-card__listdate', 'job-search-card__listdate--new']).text.replace(' ','').strip('\n')
        if ('minutes' in post_time) or ('hour' in post_time) or ('day' in post_time):
            Preferred_post_time = post_time

    except Exception as e:
        pass

    else:
        print(f"Job Role: {job_role}, \n Company Name: {company_name}, \n Time of Post: {Preferred_post_time}, \n For more Info: {more_info}")
        print("\n")