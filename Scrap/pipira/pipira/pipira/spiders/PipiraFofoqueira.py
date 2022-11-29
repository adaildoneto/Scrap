import scrapy


class PipirafofoqueiraSpider(scrapy.Spider):
    name = 'PipiraFofoqueira'
    allowed_domains = ['ac24horas.com/ultimas-noticias']
    start_urls = ['https://ac24horas.com/ultimas-noticias/']

    def parse(self, response):
        pass
