package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
public class Tester {

    private Trie trie;

    @Before
    public void setUp() {
        trie = new Trie();
        trie.insert("apple");
        trie.insert("app");
        trie.insert("apricot");
        trie.insert("banana");
        trie.insert("carrot");
        trie.insert("car");
        trie.insert("care");
        trie.insert("");
        trie.insert("Hello");
        trie.insert("hello");
    }

    @Test
    public void testBasicSearch() {
        assertTrue(trie.search("apple"));
        assertTrue(trie.search("app"));
        assertTrue(trie.search("apricot"));
    }

    @Test
    public void testUnsuccessfulSearch() {
        assertFalse(trie.search("bandana"));
    }

    @Test
    public void testPrefixSearch() {
        assertTrue(trie.startsWith("car"));
        assertTrue(trie.startsWith("care"));
        assertFalse(trie.startsWith("cat"));
    }

    @Test
    public void testEmptyString() {
        assertTrue(trie.search(""));
        assertTrue(trie.startsWith(""));
    }

    @Test
    public void testCaseSensitivity() {
        assertTrue(trie.search("Hello"));
        assertTrue(trie.search("hello"));
        assertFalse(trie.search("HELLO"));
    }
}