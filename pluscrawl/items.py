# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PluscrawlItem(Item):
    # define the fields for your item here like:
    # name = Field()
    _id = Field()
    name = Field()
    work = Field()
    edu = Field()
    links = Field()
    outfriends = Field()
    infriends = Field()
    pass
