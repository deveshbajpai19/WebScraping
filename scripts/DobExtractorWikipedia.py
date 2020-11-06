"""
Using Gazpacho to scrape Wikipedia pages of personalities and finding their Date of Births.

"""
import time
from gazpacho import get, Soup
from urllib.error import HTTPError, URLError


# Main script driver
def find_dob_driver(name):
    url = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"
    website = get_soup(url)
    if website is not None:
        return query_bday_span_value(website)
    

# GET the url and return the Soup object of the HTML contents
def get_soup(url):
    try:
        html = get(url)
        return Soup(html)
    except (HTTPError, URLError) as e:
        print(f"Error occurred: {e}")


# Query for the specific HTML span tag for the dob value
def query_bday_span_value(website: Soup):
    bday_span = website.find('span', {'class': 'bday'}, mode='first')
    if bday_span is not None:
        return bday_span.text


# main method
if __name__ == "__main__":
    names = ["Bob Dylan", "Michael Jackson", "Amy Winehouse", "Axl Rose"]
    for name in names:
        print(f"Name: {name} \t\t Date of Birth: {find_dob_driver(name)}")
        time.sleep(0.5)
