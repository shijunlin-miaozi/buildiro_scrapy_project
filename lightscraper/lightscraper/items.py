import scrapy


class LightscraperItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
