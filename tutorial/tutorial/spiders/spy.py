from scrapy.spider import Spider


class DoubanMovie(Spider):
    """docstring for DoubanMovie"""
    name="DoubanMovie"
    allow_domains=["douban.com"]
    start_urls=["https://movie.douban.com/"]


    def parse(self,response):
        filename=response.url.split("/")[-2]
        open(filename,'wb').write(response.body)
