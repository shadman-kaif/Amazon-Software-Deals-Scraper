# -*- coding: utf-8 -*-
import scrapy

class DealSpider(scrapy.Spider):
    name = 'deal'
    start_urls = ['https://www.amazon.ca/gp/goldbox?ref_=nav_cs_gb&page=1']
    page_number = 2

    def parse(self, response):
        title = response.css('div::text').extract()
        stars = response.css('a.a-link-normal::attr(title)').extract()
        review = response.css("a.a-size-small.a-link-normal::text").extract()
        price = response.css('span.p13n-sc-price::text').extract()

        # Manipulating price extraction in order to get max and min price
        max_price = del price[0::2]
        min_price = del price[1::2]

        # Fixing the div extraction for title
        title = map(lambda s: s.strip(), title)
        title = [x for x in title if x]
        del title[0:3]
        title = title[:-4]

        # Output 
        for item in zip(title, stars, review, min_price, max_price):
            # Create a dictionary to store the scraped info
            scraped_info = {
                'Title' : item[0],
                'Stars' : item[1],
                'Review' : item[2],
                'Min Price' : item[3],
                'Max Price' : item[4]
            }

            # Yield or give the scraped info to scrapy
            yield scraped_info

            # Next search results
            next_page = 'https://www.amazon.ca/gp/goldbox?ref_=nav_cs_gb&page=' + str(DealSpider.page_number)

            if DealSpider.page_number <= 20:
                # Increment page number
                DealSpider.page_number += 1
                # Recursive callback
                yield response.follow(next_page, callback = self.parse)
