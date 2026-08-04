from urllib.parse import urlparse, urljoin
from urllib.robotparser import RobotFileParser

from utils.logger import logger


class RobotsHandler:
    def __init__(self, user_agent: str = "*"):
        self.user_agent = user_agent
        self.parsers = {}

    def can_fetch(self, url: str) -> bool:
        base = "{0.scheme}://{0.netloc}".format(__import__("urllib.parse").parse.urlparse(url))

        if base not in self.parsers:
            robots_url = urljoin(base, "/robots.txt")

            parser = RobotFileParser()
            parser.set_url(robots_url)

            try:
                parser.read()
                logger.info(f"Loaded robots.txt: {robots_url}")
            except Exception:
                logger.warning(f"Could not load robots.txt: {robots_url}")

            self.parsers[base] = parser

        return self.parsers[base].can_fetch(self.user_agent, url)