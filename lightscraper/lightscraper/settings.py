BOT_NAME = 'lightscraper'

SPIDER_MODULES = ['lightscraper.spiders']
NEWSPIDER_MODULE = 'lightscraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# to avoid 301 redirect error when downloading video
MEDIA_ALLOW_REDIRECTS = True

# used to setup selenium chromedriver
CHROME_DRIVER_PATH = '/Applications/driver/chromedriver'

# Enable image and file pipeline at the same time
ITEM_PIPELINES = {
                  'scrapy.pipelines.images.ImagesPipeline': 1,
                  'scrapy.pipelines.files.FilesPipeline': 2,
                 }
FILES_STORE = 'file_download'
IMAGES_STORE = 'img_download'

# # Avoid downloading file content that has been downloaded in the last 90 days
# FILES_EXPIRES = 90
# # Avoid downloading image content that has been downloaded in the last 90 days
# IMAGES_EXPIRES = 30

# # Set image thumbnail
# IMAGES_THUMBS = {
#     'small': (50, 50),
#     'big': (250, 250),
# }
# # Image filter, minimum height and width, no download below this size
# IMAGES_MIN_HEIGHT = 110
# IMAGES_MIN_WIDTH = 110


# # setting for scrapy_splash
# SPLASH_URL = 'http://localhost:8050'
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }