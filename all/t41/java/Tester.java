package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Test class for the BloomFilter implementation.
 */
public class Tester {

    private Answer.BloomFilter bf;

    @Before
    public void setUp() {
        // Initialize BloomFilter with reasonable size and hash count for testing
        bf = new Answer.BloomFilter(1000, 5);
    }

    @Test
    public void testAddAndCheckPresence() {
        // Test that added elements are reported as present
        String testItem = "hello world";
        bf.add(testItem);
        assertTrue(bf.contains(testItem));
    }

    @Test
    public void testCheckAbsence() {
        // Test that an unadded element is not present
        assertFalse(bf.contains("random item"));
    }

    @Test
    public void testFalsePositives() {
        // Adding some elements and check for a false positive
        String[] itemsToAdd = {"item1", "item2", "item3"};
        for (String item : itemsToAdd) {
            bf.add(item);
        }
        // Check for an item not added, expecting a very low chance of false positive due to size and hash count
        assertFalse(bf.contains("item4"));
    }

    @Test
    public void testCollisionHandling() {
        // Test how the Bloom filter handles hash collisions by adding similar items
        bf.add("item123");
        bf.add("item124");
        assertTrue(bf.contains("item123"));
        assertTrue(bf.contains("item124"));
    }

    @Test
    public void testEmptyBloomFilter() {
        // Ensure that an empty Bloom Filter reports no items
        assertFalse(bf.contains("anything"));
    }
}
