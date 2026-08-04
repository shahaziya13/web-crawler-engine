from crawler.crawler import WebCrawler
from exporter.json_exporter import JSONExporter
from exporter.csv_exporter import CSVExporter
from utils.timer import Timer
from parser.keyword_search import KeywordSearch
from exporter.sqlite_exporter import SQLiteExporter
from parser.keyword_frequency import KeywordFrequency
from exporter.sitemap_exporter import SitemapExporter
from utils.cli import parse_arguments


def main():
    timer = Timer()
    timer.start()

    args = parse_arguments()

    crawler = WebCrawler(max_depth=args.depth)

    crawler.crawl(args.url)
    
    JSONExporter().export(crawler.results)
    CSVExporter().export(crawler.results)

    database = SQLiteExporter()
    database.export(crawler.results)
    database.close()

    SitemapExporter().export(crawler.link_manager.visited)

    timer.stop()

    print("\n========== CRAWL STATISTICS ==========")
    print(f"Pages Visited : {crawler.pages_visited}")
    print(f"Failed Pages  : {crawler.failed_pages}")
    print(f"Execution Time: {timer.elapsed:.2f} seconds")
    print(f"JSON Export   : data/output.json")
    print(f"CSV Export    : data/output.csv")
    search = KeywordSearch()

    keyword = input("\nEnter keyword to search: ")

    results = search.search(crawler.results, keyword)

    print(f"\nFound in {len(results)} page(s).\n")

    for page in results:
        print(page["title"])

    frequency = KeywordFrequency()

    print("\nTop Keywords\n")

    for word, count in frequency.analyze(crawler.results):
        print(f"{word:<20} {count}")


if __name__ == "__main__":
    main()