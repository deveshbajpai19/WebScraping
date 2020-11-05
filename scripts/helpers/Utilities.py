

# GET the url and return the Soup object of the HTML contents
def get_soup(url):
    html = get(url)
    return Soup(html)