from dotenv import load_dotenv
import os

load_dotenv("config.env")


class Config:
    CRAWL_DELAY = int(os.getenv("CRAWL_DELAY", 1))
    MAX_DEPTH = int(os.getenv("MAX_DEPTH", 2))
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 10))
    USER_AGENT = os.getenv("USER_AGENT", "WebCrawlerEngine/1.0")