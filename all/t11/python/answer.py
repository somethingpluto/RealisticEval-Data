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
