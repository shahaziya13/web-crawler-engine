import asyncio
import aiohttp

from crawler.async_downloader import AsyncDownloader
from parser.html_parser import HTMLParser


class AsyncCrawler:

    def __init__(self):
        self.downloader = AsyncDownloader()
        self.parser = HTMLParser()

    async def crawl(self, url):

        async with aiohttp.ClientSession() as session:

            html = await self.downloader.download(session, url)

            if html:

                data = self.parser.parse(html, url)

                print("\nAsync Crawl Successful")
                print(data["title"])