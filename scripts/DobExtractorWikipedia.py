"""
Using Gazpacho to scrape Wikipedia pages of celebrities and finding their Date of births.

TODO:
Handle HTTP response codes before building Soup object
"""
import time
from gazpacho import get, Soup


# Main script driver
def find_dob_driver(name):
    url = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"
    website = get_soup(url)
    return query_bday_span_value(website)
    

# GET the url and return the Soup object of the HTML contents
def get_soup(url):
    html = get(url)
    return Soup(html)


def query_bday_span_value(website: Soup):
    bday_span = website.find('span', {'class': 'bday'}, mode='first')
    if bday_span is not None:
        return bday_span.text
    else:
        return "No birthday found"


# main method
if __name__ == "__main__":
    names = ["Bob Dylan", "Michael Jackson", "Amy Winehouse", "Axl Rose"]
    for name in names:
        print(f"Name: {name} Date of Birth: {find_dob_driver(name)}")
        time.sleep(0.5)
