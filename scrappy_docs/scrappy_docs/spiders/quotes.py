import scrapy

# Define a new Spider class for scraping quotes
class QuotesSpider(scrapy.Spider):
    # Name of the spider, used to run it from the command line
    name = "quotes"
    # List of URLs where the spider will begin to crawl from
    start_urls = ["http://quotes.toscrape.com"]

    # The main method called with the HTTP response of each crawled page
    def parse(self, response):
        # Loop through each quote block found on the page
        for quote in response.css("div.quote"):
            # Yield a dictionary with the extracted data for each quote
            yield {
                # Extract the quote text
                "text": quote.css("span.text::text").get(),
                # Extract the author of the quote
                "author": quote.css("small.author::text").get(),
                # Extract all tags associated with the quote
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        # Find the link to the next page, if it exists
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            # If there is a next page, follow the link and call parse() again
            yield response.follow(next_page, self.parse)
