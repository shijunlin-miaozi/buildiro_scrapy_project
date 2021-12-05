import scrapy
from scrapy.utils.project import get_project_settings
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LightSpider(scrapy.Spider):
    name = 'lights_co_uk'
    # start_urls = ['https://www.lights.co.uk/philips-hue-whitel-color-impress-led-pillar-light.html'] # scraper blocked, cannot test result
    start_urls = ['https://www.lights.co.uk/philips-hue-white-color-impress-led-path-light.html'] # video & pdf
    # start_urls = ['https://www.lights.co.uk/klemens-path-light-with-motion-detector-65-cm.html'] # no video
    # start_urls = ['https://www.lights.co.uk/eve-flare-smart-led-light-for-indoors-and-out.html'] # no video, no pdf

    def parse(self, response):
        file_urls, image_urls = [], []

        settings = get_project_settings()
        s = Service(settings.get('CHROME_DRIVER_PATH'))
        driver = Chrome(service = s)
        driver.get(response.url)

        try: 
            video = driver.find_element(By.TAG_NAME, 'video')
        except:
            video = []
        try:
            pdf = driver.find_element(By.CLASS_NAME, 'download-file__link')
        except:
            pdf = []

        if video:
            play_btn = driver.find_element(By.XPATH, '//*[@id="controls"]/div/div/div[1]')
            pause_btn = driver.find_element(By.XPATH, '//*[@id="controls"]/div/div/div[2]')
            play_btn.click()
            driver.implicitly_wait(1)
            pause_btn.click()
            file_urls.append(video.get_attribute('src'))

        if pdf:
            pdf.click()
            file_urls.append(pdf.get_attribute('href'))

        driver.close()

        image_selectors = response.xpath('//*[contains(@class, "gallery-image")]')
        if image_selectors:
            for img in image_selectors:
                try:
                    image_urls.append(img.attrib['data-src'])
                except KeyError:
                    pass

        yield {
            'file_urls': file_urls,
            'image_urls' : image_urls,
        }
        

