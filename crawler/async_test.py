import asyncio

from crawler.async_crawler import AsyncCrawler


async def main():
    crawler = AsyncCrawler()
    await crawler.crawl("https://example.com")


asyncio.run(main())