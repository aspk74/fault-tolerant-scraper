BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

# Retry config
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

# Proxy middleware (uncomment if using proxies)
# DOWNLOADER_MIDDLEWARES = {
#    'scraper.middlewares.RotatingProxyMiddleware': 543,
# }

# Monitoring
EXTENSIONS = {
    'scrapy.extensions.closespider.CloseSpider': 500,
}
CLOSESPIDER_ERRORCOUNT = 50  # Auto-shutdown after 50 errors