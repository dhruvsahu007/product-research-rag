
import requests
from bs4 import BeautifulSoup

def crawl_product_page(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status() 

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'No title found'

    description = soup.find('meta', {'name': 'description'})
    description_text = description['content'] if description else 'No description found'

    price = soup.find(class_='price')
    price_text = price.get_text(strip=True) if price else 'No price found'

    return {
        "title": title,
        "description": description_text,
        "price": price_text
    }