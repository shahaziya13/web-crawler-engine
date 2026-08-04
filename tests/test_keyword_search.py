from parser.keyword_search import KeywordSearch


def test_keyword_search():
    pages = [
        {
            "title": "Python",
            "paragraphs": [
                "Python is a programming language."
            ]
        }
    ]

    search = KeywordSearch()

    result = search.search(pages, "python")

    assert len(result) == 1