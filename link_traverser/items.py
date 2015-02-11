from scrapy.item import Item, Field


class LinkTraverserItem(Item):
    the_strokes = Field()
    character = Field()