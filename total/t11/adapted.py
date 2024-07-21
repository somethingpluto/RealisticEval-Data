class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordTrie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        current = self.root
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.end_of_word = True

    def find_word(self, word):
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current.end_of_word

    def has_prefix(self, prefix):
        current = self.root
        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]
        return True

    def collect_words_with_prefix(self, prefix=''):
        words_collected = []
        current = self.root
        for character in prefix:
            if character not in current.children:
                return words_collected
            current = current.children[character]
        self._depth_first_search(current, prefix, words_collected)
        return words_collected

    def _depth_first_search(self, node, word_accumulator, collected_words):
        if node.end_of_word:
            collected_words.append(word_accumulator)
        for char, next_node in node.children.items():
            self._depth_first_search(next_node, word_accumulator + char, collected_words)
