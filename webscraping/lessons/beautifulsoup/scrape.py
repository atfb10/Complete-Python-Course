import requests

from bs4 import BeautifulSoup

# Get website
url = 'https://www.example.com/'

class ParsedItem:
    def __init__(self, url):
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
    
webpage = ParsedItem(url)
print(webpage.soup.find('h1').string)