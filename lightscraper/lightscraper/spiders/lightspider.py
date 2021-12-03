import scrapy


# scrapy crawl lights_co_uk

class LightSpider(scrapy.Spider):
    name = 'lights_co_uk'
    # start_urls = ['https://www.lights.co.uk/philips-hue-whitel-color-impress-led-pillar-light.html'] # 404 error - webpage blocked my scraper
    start_urls = ['https://www.lights.co.uk/philips-hue-white-color-impress-led-path-light.html']

    def parse(self, response):
        images_selector = response.xpath('//*[contains(@class, "gallery-image")]')
        image_urls = []
        for img in images_selector:
            try:
                image_urls.append(img.attrib['data-src'])
            except KeyError:
                pass

        yield {
            'image_urls' : image_urls
        }
        

