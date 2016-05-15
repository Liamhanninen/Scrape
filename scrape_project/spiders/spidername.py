# -*- coding: utf-8 -*-
import scrapy


class SpidernameSpider(scrapy.Spider):
    name = "spidername"
    allowed_domains = ["websitehere.com"]
    start_urls = (
        'http://www.websitehere.com/',
    )

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
    	pass
    	# Scrape site here
    	# response.body is a result of render.html call; it
        # contains HTML processed by a browser.
    	