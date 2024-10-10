package org.real.temp;

import java.util.Deque;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class Answer {
    private Deque<Integer> deque;
    private Set<Integer> set;

    public Answer() {
        deque = new ArrayDeque<>();
        set = new HashSet<>();
    }

    /**
     * Add an item to the deque if it is not already present.
     *
     * @param item The item to add.
     * @return true if the item was added, false if it was already present.
     */
    public boolean add(int item) {
        if (!set.contains(item)) {
            deque.addLast(item);
            set.add(item);
            return true;
        }
        return false;
    }

    /**
     * Remove an item from the deque if it exists.
     *
     * @param item The item to remove.
     * @return true if the item was removed, false if it was not found.
     */
    public boolean delete(int item) {
        if (set.remove(item)) {
            deque.removeFirstOccurrence(item);
            return true;
        }
        return false;
    }

    /**
     * Check if an item is present in the deque.
     *
     * @param item The item to check.
     * @return true if the item is present, false otherwise.
     */
    public boolean contains(int item) {
        return set.contains(item);
    }

    /**
     * Get the number of elements in the deque.
     *
     * @return The number of unique elements in the deque.
     */
    public int size() {
        return set.size();
    }

    /**
     * Create an iterator for the deque.
     *
     * @return An iterator over the elements in the deque.
     */
    public Iterator<Integer> iterator() {
        return deque.iterator();
    }
}