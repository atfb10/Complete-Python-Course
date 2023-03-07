from bs4 import BeautifulSoup

# Args: 1. File you wish to parse. 2. Type of parser you wish to use
filepath = "d://coding/udemy/python_introduction/webscraping/lessons/beautifulsoup/simple.html"
page = open(filepath)
soup = BeautifulSoup(page.read(), 'html.parser')

# Find first h1 tag
first_header = soup.find('h1')
print(first_header)

# Find all list items
find_list_items = lambda soup: soup.find_all('li')

# Get only the string portion of the result
def string_only(soup, tag):
    if tag == 'li':
        return [item.string for item in soup.find_all(tag)]
    return (soup.find(tag)).string

list_items = string_only(soup, 'li')
print(list_items)

# search by class
find_by_class = lambda classname: soup.find('p', {'class': classname})
print(find_by_class('subtitle'))


# Find paragraphs with no class
def no_class_paragraphs(soup):
    paragraphs = soup.find_all('p')
    # for each paragraph, see if class name is None, meaning it does not have a class.
    # If None, append to list being returned
    # Else do nothing, because it has a class
    return [paragraph for paragraph in paragraphs if paragraph.attrs.get('class') == None]

paragraphs_with_no_class = no_class_paragraphs(soup)
print(paragraphs_with_no_class)


def find_by_children():
    # Points to an 'a' tag inside li with class test, that is inside a ul, that is inside body
    locator = 'body ul li.test a'
    item = soup.select_one(locator)
    item_link = item.attrs.get('href')
    return item_link

print(find_by_children())

def get_money_value():
    locator = 'body p.iClass'
    item_text = soup.select_one(locator).string
    return float(item_text.strip('$'))

print(get_money_value())
    

# NOTE(s): DRY code
# YOU SHOULD create a class that has the soup object and all of its functions
# YOU SHOULD create a class that is just locators
# This will be demonstrated in milestone projects under webscraping/exercises