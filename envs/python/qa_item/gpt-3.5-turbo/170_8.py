from bs4 import BeautifulSoup

def convert(html: str) -> str:
    # Replace <br> or <br/> with newline characters
    html = html.replace("<br>", "\n").replace("<br/>", "\n")
    
    # Use BeautifulSoup to parse the HTML string
    soup = BeautifulSoup(html, "html.parser")
    
    # Replace paragraphs
    for p in soup.find_all("p"):
        p.string = p.get_text()
        if p.next_sibling and p.next_sibling.name == "p":
            p.string += "\n\n"
    
    # Replace strong emphasis
    for strong in soup.find_all("strong"):
        strong.string = "**" + strong.get_text() + "**"
        
    # Replace italics
    for em in soup.find_all("em"):
        em.string = "*" + em.get_text() + "*"
        
    # Replace underlined text
    for u in soup.find_all("u"):
        u.string = "*" + u.get_text() + "*"
        
    # Replace code snippets
    for code in soup.find_all("code"):
        code.string = "`" + code.get_text() + "`"
        
    # Replace unordered lists
    for ul in soup.find_all("ul"):
        ul.unwrap()
        
    # Replace ordered lists
    for ol in soup.find_all("ol"):
        ol.unwrap()
        
    # Replace list items
    for li in soup.find_all("li"):
        li.string = "* " + li.get_text() + "\n"
        
    # Replace hyperlinks
    for a in soup.find_all("a"):
        text = a.get_text()
        url = a["href"]
        a.replace_with(f"[{text}]({url})")
        
    return soup.get_text()
import unittest

class TestAnswer(unittest.TestCase):
    
    def test_simple_line_break(self):
        input_html = "Hello<br>World"
        expected_output = "Hello\nWorld"
        self.assertEqual(expected_output, convert(input_html))
    
    def test_strong_tags(self):
        input_html = "This is <strong>important</strong> text."
        expected_output = "This is **important** text."
        self.assertEqual(expected_output, convert(input_html))
    
    def test_emphasis_tags(self):
        input_html = "This is <em>emphasized</em> text."
        expected_output = "This is *emphasized* text."
        self.assertEqual(expected_output, convert(input_html))
    
    def test_unordered_list(self):
        input_html = "<ul><li>Item 1</li><li>Item 2</li></ul>"
        expected_output = "* Item 1\n* Item 2"
        self.assertEqual(expected_output, convert(input_html))
    
    def test_anchor_tags(self):
        input_html = 'Check this link: <a href="http://example.com">Example</a>.'
        expected_output = 'Check this link: [Example](http://example.com).'
        self.assertEqual(expected_output, convert(input_html))
if __name__ == '__main__':
    unittest.main()