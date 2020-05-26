# Amazon-Software-Deals-Scraper

I've always purchased my software products online from Amazon. I eventually got tired of looking for items in the later pages in Amazon.
Thus, I created a Python webscraper using Scrapy that scrapes the best selling software titles, prices, star rating and number of reviews
to make my online software shopping easier and more effective.

To run this scraper, you must have:
- Python 3
- Scrapy (just do *pip install scrapy* in your command prompt if you have Python)

Simply clone my repository in your personal computer, then use the command prompt to get to this directory. Then, run 
*scrapy crawl deal -o best_selling_software.csv* in your command prompt. This exports a csv file with the title, star rating, review number and price of the product.
Enjoy!
