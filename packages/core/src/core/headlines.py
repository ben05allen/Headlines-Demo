from bs4 import BeautifulSoup
import httpx

NEWS_URL = "https://news.ycombinator.com"


def fetch(limit: int = 5) -> list[str]:
    response = httpx.get(NEWS_URL, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    titles = [a.get_text() for a in soup.select(".titleline a")]
    return titles[:limit]
