from bs4 import BeautifulSoup

def remove_ads(html):
    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')

    # Find all 'li' elements
    list_items = soup.find_all('li')

    # Iterate over list items and remove sponsored ads
    for item in list_items:
        is_sponsored = item.find(class_='css-16lshh0')
        if is_sponsored:
            item.decompose()  # Remove the item from the tree

    # Return the modified HTML
    return str(soup)
