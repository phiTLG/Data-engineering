import scrapy


class StackoverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    allowed_domains = ['https://stackoverflow.com/questions?tab=Bounties']
    start_urls = ['http://https://stackoverflow.com/questions?tab=Bounties/']

    def parse(self, response):
        pass
