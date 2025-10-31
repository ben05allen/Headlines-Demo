from .create_logger import app_logger

from core.headlines import fetch


def main():
    headlines = fetch(5)
    for i, headline in enumerate(headlines, start=1):
        app_logger.info(f"{i} - {headline}")
