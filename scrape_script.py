import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://books.toscrape.com/'

def scrape_books():
    """Función para hacer scraping de los libros."""
    url = BASE_URL + 'catalogue/page-1.html'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        books = []
        for book in soup.select('article.product_pod'):
            title = book.h3.a['title']
            price = book.select_one('p.price_color').text
            books.append({'title': title, 'price': price})
        return books
    return None

def scrape_categories():
    """Función para hacer scraping de las categorías."""
    url = BASE_URL
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        categories = []
        for category in soup.select('div.side_categories ul li ul li a'):
            category_name = category.text.strip()
            category_url = BASE_URL + category['href']
            categories.append({'name': category_name, 'url': category_url})
        return categories
    return None
