import logging
import os

LOG_DIR = "logs"

# Vercel/serverless environments have a read-only filesystem.
# Use local file logging only when running outside Vercel.
IS_VERCEL = os.getenv("VERCEL") == "1"

logger = logging.getLogger("WebCrawler")

logger.setLevel(logging.INFO)

if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if not IS_VERCEL:
        os.makedirs(LOG_DIR, exist_ok=True)

        file_handler = logging.FileHandler(
            os.path.join(LOG_DIR, "crawler.log"),
            encoding="utf-8"
        )

        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)