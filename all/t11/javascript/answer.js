class TrieNode {
    constructor() {
        this.children = {};
        this.isEndOfWord = false;
    }

    hasChild(ch) {
        return this.children.hasOwnProperty(ch);
    }

    getChild(ch) {
        return this.children[ch];
    }

    addChild(ch) {
        if (!this.children.hasOwnProperty(ch)) {
            this.children[ch] = new TrieNode();
        }
    }

    setEndOfWord() {
        this.isEndOfWord = true;
    }

    isEnd() {
        return this.isEndOfWord;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let current = this.root;
        for (let ch of word) {
            current.addChild(ch);
            current = current.getChild(ch);
        }
        current.setEndOfWord();
    }

    search(word) {
        let current = this.root;
        for (let ch of word) {
            if (!current.hasChild(ch)) {
                return false;
            }
            current = current.getChild(ch);
        }
        return current.isEnd();
    }

    startsWith(prefix) {
        let current = this.root;
        for (let ch of prefix) {
            if (!current.hasChild(ch)) {
                return false;
            }
            current = current.getChild(ch);
        }
        return true;
    }
}