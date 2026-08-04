from collections import deque

from crawler.downloader import Downloader
from crawler.link_manager import LinkManager
from crawler.robots import RobotsHandler
from parser.html_parser import HTMLParser
from utils.config import Config


class WebCrawler:
    def __init__(self, max_depth: int = Config.MAX_DEPTH):
        self.max_depth = max_depth

        self.downloader = Downloader()
        self.parser = HTMLParser()
        self.link_manager = LinkManager()
        self.robots = RobotsHandler()

        self.delay = Config.CRAWL_DELAY

        self.results = []

        self.pages_visited = 0
        self.failed_pages = 0

    def crawl(self, seed_url: str):
        queue = deque()
        queue.append((seed_url, 0))

        while queue:

            url, depth = queue.popleft()

            if depth > self.max_depth:
                continue

            if self.link_manager.is_visited(url):
                continue

            self.link_manager.mark_visited(url)

            if not self.robots.can_fetch(url):
                continue

            html = self.downloader.download(url)

            if html is None:
                self.failed_pages += 1
                continue

            self.pages_visited += 1

            page = self.parser.parse(html, url)

            self.results.append(page)

            for link in page["links"]:

                if (
                    self.link_manager.is_internal_link(url, link)
                    and not self.link_manager.is_visited(link)
                ):
                    queue.append((link, depth + 1))