class TrieNode:
    def __init__(self):
        self.children = {}
        
class Trie:
    """
    Implement a dictionary tree for fast string retrieval and storage
    """
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.children['$'] = None
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return '$' in node.children
        
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
import unittest


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.insert("apricot")
        self.trie.insert("banana")
        self.trie.insert("carrot")
        self.trie.insert("car")
        self.trie.insert("care")
        self.trie.insert("")
        self.trie.insert("Hello")
        self.trie.insert("hello")

    def test_basic_search(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("apricot"))

    def test_unsuccessful_search(self):
        self.assertFalse(self.trie.search("bandana"))

    def test_prefix_search(self):
        self.assertTrue(self.trie.starts_with("car"))
        self.assertTrue(self.trie.starts_with("care"))
        self.assertFalse(self.trie.starts_with("cat"))

    def test_empty_string(self):
        self.assertTrue(self.trie.search(""))
        self.assertTrue(self.trie.starts_with(""))

    def test_case_sensitivity(self):
        self.assertTrue(self.trie.search("Hello"))
        self.assertTrue(self.trie.search("hello"))
        self.assertFalse(self.trie.search("HELLO"))

if __name__ == '__main__':
    unittest.main()