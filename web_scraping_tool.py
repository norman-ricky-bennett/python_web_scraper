#! python3 
#  Simple web scraping tool that searches a specific website for job postings,
# and selects only job postings made within a specific timeframe

# using BeautifulSoup to search HTML
from bs4 import BeautifulSoup
import requests
import time

print('Enter a skill that you are unfamiliar with')

unfamiliar_skill = input('>')

print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    # GET request to timesjob to provide HTML
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=C%23+Developer&txtLocation=').text

    # Setting variable for Beautiful Soup
    soup = BeautifulSoup(html_text, 'lxml')

    # Finding jobs
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    # Loop through job postings
    for index, job in enumerate(jobs):

        # Locating published date
        published_date = job.find('span', class_ = 'sim-posted').span.text

        # If statement to isolate recent job postings
        if 'few' in published_date: 

            # Locating only company name within HTML elements, replacing white space 
            # to beautify terminal results
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace('  ', '')

            # Locating skills text
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')

            # Include link in results
            more_info = job.header.h2.a['href']
            
            # Filter all postings which include unfamiliar skill
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Skills Required: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f'File Saved: {index}')
    
if __name__ == '__main__':
    while True:
        find_jobs()

        # Run program every 10 minutes
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

