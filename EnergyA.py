# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import scrapy



class Energy(scrapy.Spider):
    name = 'EnergyArticles'
    pages = 4
    start_urls = []
    for page in range(0,pages):
        url = "https://www.energy.gov/listings/energy-news?page=" + str(page) + "/"
        start_urls.append(url)
    def parse(self, response):
        response.selector.remove_namespaces()
        dates=response.css('.date::text').extract()
        desc=response.css('.title-link::text').extract()
        de=response.xpath('.//div[@class="field-item odd"]/text()').extract()
        link=response.css('.title-link::attr(href)').extract()
        for item in zip(dates,desc,de,link):
            scraped_info = {
                'article_date' : item[0],
                'article_title':item[1],
                'article_description':item[2],
                'article_url':item[3],
            }
            yield scraped_info