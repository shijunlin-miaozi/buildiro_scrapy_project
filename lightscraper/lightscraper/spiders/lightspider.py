import scrapy
from scrapy.utils.project import get_project_settings
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# scrapy crawl lights_co_uk
# start_urls = ['https://www.lights.co.uk/philips-hue-whitel-color-impress-led-pillar-light.html'] # 404 error - webpage blocked my scraper


# driver = Chrome(service = Service('/Applications/driver/chromedriver')) # options = options
# driver.get('https://www.lights.co.uk/philips-hue-white-color-impress-led-path-light.html')

# play_btn = driver.find_element(By.XPATH, '//*[@id="controls"]/div/div/div[1]')
# pause_btn = driver.find_element(By.XPATH, '//*[@id="controls"]/div/div/div[2]')
# pdf = driver.find_element(By.CLASS_NAME, 'download-file__link')

# play_btn.click()
# driver.implicitly_wait(1)
# pause_btn.click()
# pdf.click()

# driver.close()


class LightSpider(scrapy.Spider):
    name = 'lights_co_uk'
    # start_urls = ['https://www.lights.co.uk/philips-hue-white-color-impress-led-path-light.html']
    start_urls = ['https://www.lights.co.uk/philips-hue-white-color-econic-led-path-light.html']

    def __init__(self):
        settings = get_project_settings()
        s = Service(settings.get('CHROME_DRIVER_PATH'))
        # options = ChromeOptions()
        # options.headless = True
        self.driver = Chrome(service = s) # options = options

    def parse(self, response):
        file_urls, image_urls = [], []

        self.driver.get(response.url)

        play_btn = self.driver.find_element(By.XPATH, '//*[@id="controls"]/div/div/div[1]')
        pause_btn = self.driver.find_element(By.XPATH, '//*[@id="controls"]/div/div/div[2]')
        pdf = self.driver.find_element(By.CLASS_NAME, 'download-file__link')
        video = self.driver.find_element(By.TAG_NAME, 'video')

        play_btn.click()
        self.driver.implicitly_wait(1)
        pause_btn.click()
        pdf.click()

        file_urls.append(pdf.get_attribute('href'))
        file_urls.append(video.get_attribute('src'))

        self.driver.close()

        images_selector = response.xpath('//*[contains(@class, "gallery-image")]')
        for img in images_selector:
            try:
                image_urls.append(img.attrib['data-src'])
            except KeyError:
                pass

        yield {
            'file_urls': file_urls,
            'image_urls' : image_urls,
        }
        

