# 🤖 What is Scrapy?

Scrapy is an open-source Python framework for fast, efficient, and structured web scraping. It allows you to define reusable components (spiders) that:

- Crawl websites from starting URLs
- Extract structured data from pages
- Follow links automatically
- Export data to formats like JSON, CSV, or databases

## 🔥 Why Use Scrapy?

- Fast & Async (built on Twisted)
- Built-in support for pagination, selectors, export
- Works great for scraping hundreds/thousands of pages

## 🛠️ Core Concepts

- **Spider**: A class that defines how to crawl and extract
- **Selectors**: Use CSS/XPath to grab content
- **Pipelines**: Optional logic to clean or save data
- **Middleware**: Control requests (headers, retry, proxy, etc.)

## 🧪 Sample Output

```json
{
  "text": "I have not failed. I've just found 10,000 ways that won't work.",
  "author": "Thomas A. Edison",
  "tags": ["failure", "learning"]
}
