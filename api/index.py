import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from flask import Flask, render_template, request, jsonify
from crawler.crawler import WebCrawler


app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/crawl", methods=["POST"])
def crawl():
    data = request.get_json()

    url = data.get("url", "").strip()
    depth = int(data.get("depth", 1))

    if not url:
        return jsonify({
            "success": False,
            "error": "Please enter a URL."
        }), 400

    try:
        crawler = WebCrawler(max_depth=depth)
        crawler.crawl(url)

        return jsonify({
            "success": True,
            "pages_visited": crawler.pages_visited,
            "failed_pages": crawler.failed_pages,
            "results": crawler.results
        })

    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run()