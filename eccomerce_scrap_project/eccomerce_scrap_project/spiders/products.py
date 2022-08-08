"""
 This module have an ProductsSpider that is a Crawl spider
 it will crawl the all the urls from the given domains
 based on the rules that is defined in it.

"""
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items import EcommerceScrapProjectItem
from typing import Any


class ProductsSpider(CrawlSpider):
    """
      ProductsSpider is a crawl spider it will crawl the all pages according to
      given rules , it has rules that allow the crawl spider either which url will be
      crawled and which should be ignored.
      Three rules are defined below for link extraction
    """
    name = 'products'
    allowed_domains = ['www.6pm.com']
    start_urls = ['https://www.6pm.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//header/div[@class="ja-z"]/ul/li//div/a[@class="oa-z"]')),
        Rule(LinkExtractor(restrict_xpaths='//a[@rel="next"]')),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="products"]/article/a'), callback='parse_cats')
    )

    def parse_cats(self, response):
        product_loader = ItemLoader(item=EcommerceScrapProjectItem(), response=response)
        list_of_category = response.xpath('//div[@id = "breadcrumbs"]/div/a/text()').getall()
        product_loader.add_value('prod_category', list_of_category[1])
        product_loader.add_xpath('brand_name', '//span[@itemprop="name"]/text()')
        product_loader.add_xpath('product_name', '//h1/div/span[@class = "ys-z"]/text()')
        product_loader.add_xpath('product_img_links', '//*[@id="productThumbnails"]//img/@src')
        product_loader.add_xpath('product_colors', '//*[@id="buyBoxForm"]/div[1]//img/@src')
        product_loader.add_xpath('current_price', '//div[@class = "Yr-z"]/span/@content')
        product_loader.add_xpath('previous_price', '//span[@class = "js-z"]/text()')
        list_of_discount = response.xpath('//span[@class = "ds-z"]/span/text()').getall()
        off_percentage = ''.join(list_of_discount)
        product_loader.add_value('off_percentage', off_percentage)
        product_loader.add_xpath('prod_information', '//div[@class = "f4-z"]/ul/li/text()')
        product_loader.add_xpath('available_sizes',
                                 '//form[@id = "buyBoxForm"]//div[@class = "qD-z rD-z"]/div/label/text()')
        yield product_loader.load_item()
