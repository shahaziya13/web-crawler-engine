# Web Crawler & Data Extraction Engine

A scalable Python-based web crawler that automatically downloads webpages, extracts human-readable information, follows internal links, and exports structured datasets.

This project was developed as part of the Python Development Internship Task.

---

# Features

## Core Features

- Accepts seed URLs from users
- Downloads webpages using Python requests
- Parses HTML using BeautifulSoup
- Extracts:
  - Page titles
  - Headings
  - Paragraphs
  - Hyperlinks
  - Images
  - Metadata
- Queue-based internal link crawling
- Duplicate URL tracking
- robots.txt support
- Configurable crawl delay
- Retry and timeout handling
- JSON export
- CSV export
- Crawl statistics
- Keyword search
- Logging system
- Configuration using environment file

## Additional Features

- SQLite database storage
- Sitemap generation
- Keyword frequency analysis
- Command-line interface
- Async crawling support
- Unit testing

---

# Technologies Used

- Python 3.11+
- Requests
- BeautifulSoup4
- aiohttp
- SQLite
- Pandas
- Pytest
- Python-dotenv

---

# Project Structure

```
web-crawler-engine/

│
├── crawler/
│   ├── crawler.py
│   ├── downloader.py
│   ├── async_crawler.py
│   ├── async_downloader.py
│   ├── link_manager.py
│   └── robots.py
│
├── parser/
│   ├── html_parser.py
│   ├── keyword_search.py
│   └── keyword_frequency.py
│
├── exporter/
│   ├── json_exporter.py
│   ├── csv_exporter.py
│   ├── sqlite_exporter.py
│   └── sitemap_exporter.py
│
├── utils/
│   ├── config.py
│   ├── logger.py
│   ├── timer.py
│   └── cli.py
│
├── data/
│   ├── output.json
│   ├── output.csv
│   ├── crawler.db
│   └── sitemap.txt
│
├── tests/
│
├── main.py
├── requirements.txt
└── config.env
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
```

Navigate to project folder:

```bash
cd web-crawler-engine
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Run the crawler using:

```bash
python main.py --url https://example.com --depth 1
```

Example Output:

```
========== CRAWL STATISTICS ==========

Pages Visited : 1
Failed Pages  : 0
Execution Time: 0.45 seconds

JSON Export : data/output.json
CSV Export  : data/output.csv
```

---

# Generated Files

The crawler exports collected data into different formats.

## JSON Export

```
data/output.json
```

## CSV Export

```
data/output.csv
```

## SQLite Database

```
data/crawler.db
```

## Sitemap

```
data/sitemap.txt
```

---

# Keyword Search

The crawler supports searching keywords from collected webpage content.

Example:

```
Enter keyword to search:
python

Found in 2 page(s).
```

---

# Keyword Frequency Analysis

The system analyzes collected content and displays the most frequently used keywords.

Example:

```
Top Keywords

python       20
crawler      15
html         10
```

---

# Testing

Run unit tests using:

```bash
pytest
```

---

# Configuration

Crawler settings can be modified using:

```
config.env
```

Example:

```
CRAWL_DELAY=1
MAX_DEPTH=2
REQUEST_TIMEOUT=10
USER_AGENT=WebCrawlerEngine/1.0
```

---

# Author

**Ayshath Shahaziya**

Artificial Intelligence and Machine Learning

---

# License

This project is created for educational and internship purposes.