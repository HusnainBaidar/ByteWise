import scrapy
from ..items import AmazonScrapingItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.com']
    page_num = 2
    start_urls = ['https://www.amazon.com/Books-Last-30-days/s?i=stripbooks&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&qid=1663859053&ref=sr_pg_2']

    def parse(self, response):
        items = AmazonScrapingItem()
        product_name = response.css('.a-size-medium::text').extract()
        product_author = response.css('.a-color-secondary .a-row .a-size-base+ .a-size-base , .a-color-secondary .a-size-base.s-link-style').css('::text').extract()
        product_price = response.css('.widgetId\=search-results_2 .a-spacing-mini:nth-child(1) .a-price-whole , .s-price-instructions-style .a-price-whole').css('::text').extract()
        product_imglink = response.css('.s-image::attr(src)').extract()

        items ['product_name'] = product_name
        items ['product_author'] = product_author
        items ['product_price'] = product_price
        items ['product_imglink'] = product_imglink

        yield items

        next_page = 'https://www.amazon.com/Books-Last-30-days/s?i=stripbooks&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&page='+ str(AmazonSpiderSpider.page_num) +'&qid=1663859053&ref=sr_pg_2'

        if AmazonSpiderSpider.page_num <= 100:
            print(AmazonSpiderSpider.page_num)
            AmazonSpiderSpider.page_num += 1
            yield response.follow(next_page, callback = self.parse)