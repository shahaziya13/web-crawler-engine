import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Python Web Crawler & Data Extraction Engine"
    )

    parser.add_argument(
        "--url",
        required=True,
        help="Seed URL to crawl"
    )

    parser.add_argument(
        "--depth",
        type=int,
        default=2,
        help="Maximum crawl depth"
    )

    return parser.parse_args()