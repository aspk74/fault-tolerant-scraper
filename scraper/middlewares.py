import random

class RotatingProxyMiddleware:
    def __init__(self, proxies):
        self.proxies = proxies

    @classmethod
    def from_crawler(cls, crawler):
        return cls(proxies=[
            'http://proxy1.example.com:8080',
            'http://proxy2.example.com:8080'
        ])

    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(self.proxies)