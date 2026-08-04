import os
import sqlite3


class SQLiteExporter:
    def __init__(self, database: str = "data/crawler.db"):
        os.makedirs("data", exist_ok=True)

        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                headings TEXT,
                paragraphs TEXT,
                links TEXT,
                images TEXT
            )
        """)

        self.connection.commit()

    def export(self, data: list):
        for page in data:
            self.cursor.execute("""
                INSERT INTO pages
                (title, headings, paragraphs, links, images)
                VALUES (?, ?, ?, ?, ?)
            """, (
                page["title"],
                "\n".join(page["headings"]),
                "\n".join(page["paragraphs"]),
                "\n".join(page["links"]),
                "\n".join(page["images"])
            ))

        self.connection.commit()

    def close(self):
        self.connection.close()