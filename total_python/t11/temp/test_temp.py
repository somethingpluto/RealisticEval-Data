import unittest

from total_python.t11.adapted import Trie


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
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def has_child(self, ch):
        return ch in self.children

    def get_child(self, ch):
        return self.children.get(ch)

    def add_child(self, ch):
        if ch not in self.children:
            self.children[ch] = TrieNode()

    def set_end_of_word(self):
        self.is_end_of_word = True

    def is_end(self):
        return self.is_end_of_word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            current.add_child(ch)
            current = current.get_child(ch)
        current.set_end_of_word()

    def search(self, word):
        current = self.root
        for ch in word:
            if not current.has_child(ch):
                return False
            current = current.get_child(ch)
        return current.is_end()

    def starts_with(self, prefix):
        current = self.root
        for ch in prefix:
            if not current.has_child(ch):
                return False
            current = current.get_child(ch)
        return True
