from bs4 import BeautifulSoup

def remove_ads(html_content):
    """
    Iterate over list items on a web page and remove ads that contain a specific class name.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    ads_to_remove = ['ad-class-name']  # List of class names to remove

    for script in soup(['script', 'iframe','style']):
        script.decompose()

    for element in soup.find_all(['img', 'div']):
        if any(class_ in element['class'] for class_ in ads_to_remove):
            element.decompose()

    return str(soup)
class TestRemoveAds(unittest.TestCase):

    def setUp(self):
        """Reset the HTML content before each test."""
        self.html_content = ""

    def test_removes_single_sponsored_product(self):
        self.html_content = """
            <ul>
                <li><span class="css-16lshh0">Sponsored</span></li>
                <li>Regular Item</li>
            </ul>
        """
        modified_html = remove_ads(self.html_content)
        soup = BeautifulSoup(modified_html, 'html.parser')
        list_items = soup.find_all('li')

        self.assertEqual(len(list_items), 2)
        self.assertEqual(list_items[0].text.strip(), 'Sponsored')

    def test_removes_multiple_sponsored_products(self):
        self.html_content = """
            <ul>
                <li><span class="css-16lshh0">Sponsored</span></li>
                <li>Regular Item</li>
                <li><span class="css-16lshh0">Sponsored</span></li>
                <li>Another Regular Item</li>
            </ul>
        """
        modified_html = remove_ads(self.html_content)
        soup = BeautifulSoup(modified_html, 'html.parser')
        list_items = soup.find_all('li')

        self.assertEqual(len(list_items), 4)
        self.assertEqual(list_items[0].text.strip(), 'Sponsored')
        self.assertEqual(list_items[1].text.strip(), 'Regular Item')

    def test_does_not_remove_any_items_if_no_sponsored_products(self):
        self.html_content = """
            <ul>
                <li>Regular Item</li>
                <li>Another Regular Item</li>
            </ul>
        """
        modified_html = remove_ads(self.html_content)
        soup = BeautifulSoup(modified_html, 'html.parser')
        list_items = soup.find_all('li')

        self.assertEqual(len(list_items), 2)
        self.assertEqual(list_items[0].text.strip(), 'Regular Item')
        self.assertEqual(list_items[1].text.strip(), 'Another Regular Item')

    def test_removes_items_with_nested_sponsored_indicators(self):
        self.html_content = """
            <ul>
                <li>
                    <div>
                        <span class="css-16lshh0">Sponsored</span>
                    </div>
                </li>
                <li>Regular Item</li>
            </ul>
        """
        modified_html = remove_ads(self.html_content)
        soup = BeautifulSoup(modified_html, 'html.parser')
        list_items = soup.find_all('li')

        self.assertEqual(len(list_items), 2)

    def test_does_not_remove_items_with_similar_but_non_sponsored_class_names(self):
        self.html_content = """
            <ul>
                <li><span class="css-16lshh1">Not Sponsored</span></li>
                <li>Regular Item</li>
            </ul>
        """
        modified_html = remove_ads(self.html_content)
        soup = BeautifulSoup(modified_html, 'html.parser')
        list_items = soup.find_all('li')

        self.assertEqual(len(list_items), 2)
        self.assertEqual(list_items[0].text.strip(), 'Not Sponsored')
        self.assertEqual(list_items[1].text.strip(), 'Regular Item')

if __name__ == '__main__':
    unittest.main()