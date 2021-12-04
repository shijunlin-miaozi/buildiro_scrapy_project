import scrapy
# from scrapy.loader import ItemLoader
# from lightscraper.items import LightscraperItem
# from scrapy_splash import SplashRequest #todo remove scrapy_splash from requirement
# from scrapy.http import Request

# scrapy crawl lights_co_uk
# start_urls = ['https://www.lights.co.uk/philips-hue-whitel-color-impress-led-pillar-light.html'] # 404 error - webpage blocked my scraper
# scrapy shell 'http://localhost:8050/render.html?url=   [http://xxxx.html]   &timeout=10&wait=0.5'


class LightSpider(scrapy.Spider):
    name = 'lights_co_uk'
    start_urls = ['https://www.lights.co.uk/philips-hue-white-color-impress-led-path-light.html']

    #! splash does not help. video & pdf files are requested (xhr) upon click event
    # def start_requests(self):
    #     url = 'https://www.lights.co.uk/philips-hue-white-color-impress-led-path-light.html'
    #     yield SplashRequest(url)


    def parse(self, response):
        # file_urls = ['https://www.lights.co.uk/media/catalog/downloads/datenblatt_extern/e/f/1/5/ef156d749c74.pdf',
        #             'https://es29.mycliplister.com/cls/stream/2da2e25dc76f25760871dac0dea9ffe6da82e7b2ff6eeaca215f658b1c4c4701fdab4ce6c12f81bbb1657e78211c3b4a887ff8101d1e23d7aadca9195fa8417f'
        #         ]

        # item = LightscraperItem()
        # item['file_urls'] = file_urls
        # yield item

        file_urls = ['https://mycliplister.com/vx/87003/1f4d67595cc2e5f33c6bcdd99bd4d1107ee0b4a5ab7411ae1fc5c97233888b8ac2e52fe22f0b2b8ec2e6af894d662dadb664272d786d9d35c72a48e5ffe4cb4aa_x4c002731b13c1f45b3e232a7d57a46cb136ae0d8048003374d7a135d765a8c63d6ffaa4f54aa5e818aad9c6892b2be28ef03d0d1baf356eb0ab63cb3d3f42637']

        # image_urls = ['https://lw-cdn.com/images/BC8AB72A1104/k_3b7cc359fb89dab5a68af93a0f034e3c;w_535;h_535;q_70/philips-hue-white-color-impress-led-path-light.webp']

        # images_selector = response.xpath('//*[contains(@class, "gallery-image")]')
        # image_urls = []
        # for img in images_selector:
        #     try:
        #         image_urls.append(img.attrib['data-src'])
        #     except KeyError:
        #         pass

        yield {
            # 'image_urls' : image_urls,
            'file_urls': file_urls,
        }
        

