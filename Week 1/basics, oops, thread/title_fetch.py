import concurrent.futures
import requests
from bs4 import BeautifulSoup


def fetch_title(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'
        print(f"URL: {url}, Title: {title}")
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")


urls = [

    "https://www.example.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://surveysparrow.com",
    "https://www.thrivesparrow.com"

]

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(fetch_title, urls)

