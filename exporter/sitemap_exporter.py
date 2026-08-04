import os


class SitemapExporter:
    def export(self, visited_urls: set, filename: str = "data/sitemap.txt"):
        os.makedirs("data", exist_ok=True)

        with open(filename, "w", encoding="utf-8") as file:
            for url in sorted(visited_urls):
                file.write(url + "\n")
                