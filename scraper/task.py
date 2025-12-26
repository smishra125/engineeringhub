import requests
from bs4 import BeautifulSoup
from .models import ScrapedPost

def scrape_engineering_news():
    url = "https://example.com/engineering-news"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    items = soup.select(".news-item")
    for item in items[:5]:
        headline = item.text.strip()
        link = item['href']
        ScrapedPost.objects.get_or_create(headline=headline, url=link)
