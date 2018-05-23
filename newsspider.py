import scrapy
import jtalk


class NewsSpider(scrapy.Spider):
    name = 'newsspider'
    start_urls = ["http://www.asahi.com/news/"]

    def parse(self, response):
        url = response.css("a.SW ::attr('href')").extract_first()
        return scrapy.Request(response.urljoin(url), self.parse_contents)

    def parse_contents(self, response):
        content = "".join(response.css("div.ArticleText p::text").extract_first())
        jtalk.jtalk(content.strip().encode("utf-8"))
        return {"content": content.strip()}

# 実行方法
# scrapy runspider --nolog newspider.py
