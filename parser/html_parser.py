from bs4 import BeautifulSoup
from urllib.parse import urljoin


class HTMLParser:
    """
    Extracts useful information from HTML pages.
    """

    def parse(self, html: str, base_url: str) -> dict:
        soup = BeautifulSoup(html, "lxml")

        title = soup.title.string.strip() if soup.title and soup.title.string else ""

        headings = [
            heading.get_text(strip=True)
            for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        ]

        paragraphs = [
            paragraph.get_text(strip=True)
            for paragraph in soup.find_all("p")
        ]

        links = [
            urljoin(base_url, link.get("href"))
            for link in soup.find_all("a", href=True)
        ]

        images = [
            urljoin(base_url, image.get("src"))
            for image in soup.find_all("img", src=True)
        ]

        metadata = {}

        for meta in soup.find_all("meta"):
            key = meta.get("name") or meta.get("property")
            value = meta.get("content")

            if key and value:
                metadata[key] = value

        return {
            "title": title,
            "headings": headings,
            "paragraphs": paragraphs,
            "links": links,
            "images": images,
            "metadata": metadata,
        }