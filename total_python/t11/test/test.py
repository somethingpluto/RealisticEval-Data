import unittest

from total.t11.adapted import WordTrie


class TestWordTrie(unittest.TestCase):

    def test_add_and_find_word(self):
        trie = WordTrie()
        trie.add_word("hello")
        self.assertTrue(trie.find_word("hello"))
        self.assertFalse(trie.find_word("hel"))

    def test_prefix(self):
        trie = WordTrie()
        trie.add_word("hello")
        trie.add_word("hell")
        self.assertTrue(trie.has_prefix("hel"))
        self.assertFalse(trie.has_prefix("heaven"))

    def test_collect_words(self):
        trie = WordTrie()
        trie.add_word("hello")
        trie.add_word("hell")
        trie.add_word("helium")
        collected = trie.collect_words_with_prefix("hel")
        self.assertEqual(set(collected), {"hello", "hell", "helium"})
