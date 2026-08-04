from typing import Optional
from utils.config import Config

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from utils.logger import logger


class Downloader:
    """
    Downloads web pages with retries and timeout handling.
    """

    def __init__(self, timeout: int = 10):
        self.timeout = timeout

        self.session = requests.Session()

        retry = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
        )

        adapter = HTTPAdapter(max_retries=retry)

        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        self.headers = {
            "User-Agent": Config.USER_AGENT
        }

    def download(self, url: str) -> Optional[str]:
        """
        Download HTML from the given URL.
        """

        try:
            logger.info(f"Downloading: {url}")

            response = self.session.get(
                url,
                headers=self.headers,
                timeout=self.timeout
            )

            response.raise_for_status()

            logger.info(f"Success: {url}")

            return response.text

        except requests.RequestException as error:
            logger.error(f"Failed to download {url}: {error}")
            return None