# -*- coding: utf-8 -*-
import scrapy

class DealSpider(scrapy.Spider):
    name = 'deal'
    start_urls = ['https://www.amazon.ca/Best-Sellers-Software/zgbs/software/ref=zg_bs_software_home_all?pf_rd_p=d8978078-43b5-4da2-9cfc-1b5da282df98&pf_rd_s=center-4&pf_rd_t=2101&pf_rd_i=home&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_r=BMFGPEZYJ6K2YB85C5ZF&pf_rd_r=BMFGPEZYJ6K2YB85C5ZF&pf_rd_p=d8978078-43b5-4da2-9cfc-1b5da282df98&page=1']
    page_number = 2

    def parse(self, response):
        title = response.css('div::text').extract()
        stars = response.css('a.a-link-normal::attr(title)').extract()
        review = response.css("a.a-size-small.a-link-normal::text").extract()
        price = response.css('span.p13n-sc-price::text').extract()

        # Manipulating price extraction in order to get max and min price
        #max_price = [v for i, v in enumerate(price) if i % 2 == 1]
        #min_price = [v for i, v in enumerate(price) if i % 2 == 0]

        # Fixing the div extraction for title
        title = map(lambda s: s.strip(), title)
        title = [x for x in title if x]
        del title[0:3]
        title = title[:-4]

        if len(title) == 0:
            title = [""]

        if len(price) == 0:
            price = [""]

        if len(review) == 0:
            review = [""]  

        if len(stars) == 0:
            stars = [""]  

        # Output 
        for item in zip(title, stars, review, price):
            # Create a dictionary to store the scraped info
            scraped_info = {
                'Title' : item[0],
                'Stars' : item[1],
                'Review' : item[2],
                'Price' : item[3]
            }

            # Yield or give the scraped info to scrapy
            yield scraped_info

            # Next search results
            next_page = 'https://www.amazon.ca/Best-Sellers-Software/zgbs/software/ref=zg_bs_software_home_all?pf_rd_p=d8978078-43b5-4da2-9cfc-1b5da282df98&pf_rd_s=center-4&pf_rd_t=2101&pf_rd_i=home&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_r=BMFGPEZYJ6K2YB85C5ZF&pf_rd_r=BMFGPEZYJ6K2YB85C5ZF&pf_rd_p=d8978078-43b5-4da2-9cfc-1b5da282df98&page=' + str(DealSpider.page_number)

            if DealSpider.page_number <= 3:
                # Increment page number
                DealSpider.page_number += 1
                # Recursive callback
                yield response.follow(next_page, callback = self.parse)
