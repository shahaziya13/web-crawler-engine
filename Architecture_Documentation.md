# Web Crawler & Data Extraction Engine
## Architecture Documentation

## 1. Project Overview

The Web Crawler & Data Extraction Engine is a Python-based application that automatically downloads webpages, extracts useful information from HTML content, follows internal links, and exports collected data into structured formats.

The system is designed using modular architecture where each component performs a specific responsibility.

---

# 2. System Architecture

```
                 User
                  |
                  |
                  v
          Command Line Interface
                  |
                  |
                  v
            Web Crawler Engine
                  |
        -----------------------
        |                     |
        v                     v
   URL Manager          Robots Handler
        |
        v
   Page Downloader
        |
        v
    HTML Parser
        |
        v
 Extracted Data
        |
 -----------------------------
 |        |        |          |
 v        v        v          v
 JSON    CSV    SQLite    Sitemap
 Export  Export Database Generator
```

---

# 3. Module Description

## Crawler Module

Location:

```
crawler/
```

Responsibilities:

- Manage crawling process
- Maintain visited URLs
- Control crawl depth
- Handle internal links
- Respect robots.txt rules


Files:

### crawler.py
Main crawling engine.

### downloader.py
Downloads webpage content using HTTP requests.

### async_crawler.py
Provides asynchronous crawling support.

### async_downloader.py
Handles asynchronous webpage downloads.

### link_manager.py
Tracks visited URLs and validates internal links.

### robots.py
Handles robots.txt permissions.

---

# 4. Parser Module

Location:

```
parser/
```

Responsibilities:

- Extract information from HTML pages.

Files:

### html_parser.py

Extracts:

- Titles
- Headings
- Paragraphs
- Links
- Images
- Metadata


### keyword_search.py

Provides keyword searching over collected content.


### keyword_frequency.py

Analyzes frequently occurring keywords.

---

# 5. Exporter Module

Location:

```
exporter/
```

Responsibilities:

Convert extracted information into different formats.

Files:

### json_exporter.py

Exports data into JSON format.

### csv_exporter.py

Exports data into CSV format.

### sqlite_exporter.py

Stores webpage information in SQLite database.

### sitemap_exporter.py

Generates sitemap containing crawled URLs.

---

# 6. Utility Module

Location:

```
utils/
```

Responsibilities:

Provides supporting functionality.

Files:

### config.py

Loads configuration values.

### logger.py

Maintains application logs.

### timer.py

Measures execution time.

### cli.py

Handles command-line arguments.

---

# 7. Data Flow

1. User provides seed URL.
2. CLI receives URL and crawl depth.
3. Crawler checks URL status.
4. Robots handler verifies crawling permission.
5. Downloader fetches webpage HTML.
6. Parser extracts required information.
7. Extracted data is stored.
8. Exporters generate JSON, CSV, SQLite, and sitemap files.
9. Statistics are displayed to the user.

---

# 8. Technologies Used

- Python 3.11+
- Requests
- BeautifulSoup4
- aiohttp
- SQLite
- Pandas
- Pytest
- Python-dotenv

---

# 9. Design Approach

The project follows:

- Object-oriented programming
- Modular architecture
- Separation of responsibilities
- Exception handling
- Configurable settings

This structure improves scalability, maintainability, and future enhancements.