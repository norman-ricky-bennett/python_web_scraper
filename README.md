# Python Web Scraper

Using BeautifulSoup, this web scraper extracts HTML text from a job search on timesjobs.com to provide the most up-to-date results that meet the specified criteria of the person searching. 

## How to use this web scraper

1. Make sure you have python3 installed on your system
2. Install BeautifulSoup4 and lxml on your system 
    - Once python3 is installed, run *pip install bs4*
    - Run the command *pip install lxml*
3. Clone this repository into a local directory
4. Create an empty directory in the Web Scraper directory called *index* (this is where the results of the program will be stored, once you run it)
5. You can change the desired page you would like to scrape by changing the timesjobs.com URL to another URL located on that website, and pasting it in the requests.get part of the code
6. Run the program using the command *python3 .\web_scraping_tool.py* 