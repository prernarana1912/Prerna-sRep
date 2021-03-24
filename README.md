# Web Scraping
Website used for scraping- https://www.energy.gov/listings/energy-news
## Question 1- using scrapy
* Used spyder to develop the necessary code. The trickiest part was to extract the HTML/XML elements properly. Used CSS and XPath both.
* Created a directory using Anaconda prompt and saved my spyder code in that directory as a .Py file
* Used 'scrapy crawl EnergyArticles' (name of my object) to check the functionality in Anaconda prompt
* Used 'scrapy crawl EnergyArticles -o filename.csv' to save the output in my directory as a csv file which I later converted to Excel file.

## Question 2- Using selenium
* It is easier to extract web elements using Selenium.
* Created a list called total[] to exctract data from first four pages.
