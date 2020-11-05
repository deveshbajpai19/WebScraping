__author__ = 'Devesh Bajpai'

'''
Re-implementation of the Gazpacho tutorial for scraping a static HTML website

Usage: python Simple.py
'''
from gazpacho import get, Soup


# Main script driver
def driver(url):
    soup = get_soup(url)
    books = extract_books(soup)
    for book in books:
        parse_book(book)


# GET the url and return the Soup object of the HTML contents
def get_soup(url):
    html = get(url)
    return Soup(html)


# Query and return the div tag with a partial matching of div class name
def extract_books(website: Soup):
    return website.find('div', {'class': 'book-'}, partial=True)


# Parse each book's Soup object to find the title and price via h4 and p tags respectively
def parse_book(book: Soup):
    title = book.find('h4').text
    price = book.find('p').text
    print("____________________________________________")
    # Uncomment to see each book's Soup object
    #print(book)
    print("Title : " + title)
    print("Price : " + price)


# main method
if __name__ == "__main__":
    driver("https://scrape.world/books")
