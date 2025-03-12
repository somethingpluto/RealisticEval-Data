
class Trie:
    """
    Implement a dictionary tree for fast string retrieval and storage
    """

    def insert(self, word):
        """Insert a word into the trie and store it in the root node"""
        root = TrieNode()
        root.children[word] = self
        return root

    def search(self, word):
        """Search for a word in the trie and return the index of the word"""
        for child in self.children:
            if child.starts_with(word):
                return child.index
        return -1

    def starts_with(self, prefix):
        """Return True if the word starts with the given prefix, False otherwise"""
        for child in self.children:
            if child.starts_with(prefix):
                return True
        return False


class TrieNode:
    """Node in the trie for storing and retrieving strings"""

    def __init__(self):
        """Create a new trie node"""
        self.children = {}

    def insert(self, word):
        """Insert a word into the trie and store it in the node"""
        if word not in self.children:
            self.children[word] = TrieNode()
        self.children[word].insert(word)
        return self

    def search(self, word):
        """Search for a word in the trie and return the index of the word"""
        for child in self.children:
            if child.starts_with(word):
                return child.index
        return -1


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