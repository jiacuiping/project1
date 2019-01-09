import scrapy

class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["shicimingju.com"]
    start_urls = [
        "http://www.shicimingju.com/",
    ]

    def parse(self, response):
        authors = response.xpath('//a[@class="www-main-container"]/li/a/text()').extract()
        for author in authors:
            print(author.strip())