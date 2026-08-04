from parser.html_parser import HTMLParser


def test_title_extraction():
    html = """
    <html>
        <head>
            <title>My Test Page</title>
        </head>
        <body>
            <h1>Welcome</h1>
            <p>Hello World</p>
        </body>
    </html>
    """

    parser = HTMLParser()
    data = parser.parse(html, "https://example.com")

    assert data["title"] == "My Test Page"
    assert data["headings"] == ["Welcome"]
    assert data["paragraphs"] == ["Hello World"]