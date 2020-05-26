# -*- coding: utf-8 -*-
import scrapy

class DealSpider(scrapy.Spider):
    name = 'deal'
    allowed_domains = ['https://www.amazon.ca/gp/goldbox?ref_=nav_cs_gb']
    start_urls = ['http://https://www.amazon.ca/gp/goldbox?ref_=nav_cs_gb/']
    page_number = 2

    def parse(self, response):
        
        # Output 
        for item in zip(title, description, review):
            # Create a dictionary to store the scraped info
            scraped_info = {
                'Title' : item[0],
                'Description' : item[1],
                'Review' : item[2]
            }

            # Yield or give the scraped info to scrapy
            yield scraped_info

            # Next search results
            next_page = 'https://www.amazon.ca/s?k=bike&page=' + str(DealSpider.page_number) + '&ref=nb_sb_noss_2'

            if DealSpider.page_number <= 20:
                # Increment page number
                DealSpider.page_number += 1
                yield response.follow(next_page, callback = self.parse)
