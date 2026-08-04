from urllib.parse import urlparse


class LinkManager:
    def __init__(self):
        self.visited = set()

    def is_visited(self, url: str) -> bool:
        return url in self.visited

    def mark_visited(self, url: str):
        self.visited.add(url)

    def is_internal_link(self, base_url: str, target_url: str) -> bool:
        return urlparse(base_url).netloc == urlparse(target_url).netloc