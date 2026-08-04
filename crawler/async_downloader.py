import aiohttp


class AsyncDownloader:
    def __init__(self, timeout: int = 10):
        self.timeout = aiohttp.ClientTimeout(total=timeout)

    async def download(self, session: aiohttp.ClientSession, url: str):
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()

        except Exception:
            return None