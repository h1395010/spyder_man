from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from link_traverser.items import LinkTraverserItem

class DmozSpider(BaseSpider):
    name = "traverser"
    allowed_domains = ["tool.httpcn.com"]
    start_urls = ["http://tool.httpcn.com/Html/Zi/28/PWMETBAZTBTBBDTB.shtml"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        
        items = []
        item =  LinkTraverserItem()

        item["the_strokes"] = hxs.xpath('//*[@id="div_a1"]/div[2]').extract()
        item["character"] = hxs.xpath('//*[@id="div_a1"]/div[3]').extract()
        items.append(item)
        return items
