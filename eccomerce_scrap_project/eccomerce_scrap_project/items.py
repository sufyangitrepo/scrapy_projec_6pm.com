"""
  This module contains the structure of the item details that will be
  extracted from url it has an item that defines the structure for data
"""
import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from scrapy.item import Field


def add_currency_symbol(price: str) -> str:
    symbol = '$'
    return symbol + price


class ProductItem(scrapy.Item):
    """
      This is an item that define the different fields these are
        category:                   it is the category of product like shoes , clothes
        brand_name:                      it is the brand name of product
        prod_name:                            Name of the product
        product_img_links                product related images links
        product_colors:                  different colors images of product
        current_price:                   it is the current price of prodcut with discount
        previous_price:                  it is the actual price of product
        off_percentage:                  the off perentage of the product
        detail_info:                          product related all information
        available_sizes:                 product's available sizes

    """
    # define the fields for your item here like:
    category = Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst()
    )
    brand_name = Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst()
    )
    product_name = Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst()
    )
    product_img_links = Field(
        input_processor=MapCompose(),
    )
    product_colors = Field(
        input_processor=MapCompose(),
    )
    current_price = Field(
        input_processor=MapCompose(add_currency_symbol),
        output_processor=TakeFirst()
    )
    previous_price = Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst()
    )
    off_percentage = Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst()
    )
    detail_info = Field(
        input_processor=MapCompose(),
    )
    available_sizes = Field(
        input_processor=MapCompose()
    )
