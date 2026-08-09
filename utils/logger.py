import logging
import os

# Vercel provides /tmp as a writable directory
LOG_DIR = "/tmp/logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "crawler.log")

logger = logging.getLogger("web_crawler")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers during serverless imports
if not logger.handlers:
    # Console handler - visible in Vercel logs
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # File handler - temporary storage only
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)