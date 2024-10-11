package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    private Trie trie;

    @Before
    public void setUp() {
        trie = new Trie();
    }

    @Test
    public void testInsert() {
        // Assuming you have an implementation for insert in Trie class
        trie.insert("apple");
        assertTrue(trie.search("apple"));
    }

    @Test
    public void testSearch() {
        // Assuming you have an implementation for search in Trie class
        trie.insert("apple");
        assertTrue(trie.search("apple"));
        assertFalse(trie.search("banana"));
    }

    @Test
    public void testStartsWith() {
        // Assuming you have an implementation for startsWith in Trie class
        trie.insert("apple");
        assertTrue(trie.startsWith("app"));
        assertFalse(trie.startsWith("ban"));
    }
}