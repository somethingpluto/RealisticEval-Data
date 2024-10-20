package org.real.temp;

import java.util.LinkedList;
import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;

public class Answer {
    static class UniqueDeque{
        private LinkedList<Integer> deque;
        private Set<Integer> set;

        public UniqueDeque() {
            // Initialize a UniqueDeque object using a LinkedList and a HashSet.
            // The LinkedList stores elements in order, while the HashSet ensures uniqueness.
            this.deque = new LinkedList<>();
            this.set = new HashSet<>();
        }

        public boolean add(int item) {
            // Add an item to the deque if it is not already present.
            if (!set.contains(item)) {
                deque.addLast(item);
                set.add(item);
                return true;
            }
            return false;
        }

        public boolean delete(int item) {
            // Remove an item from the deque if it exists.
            if (set.contains(item)) {
                deque.removeFirstOccurrence(item);
                set.remove(item);
                return true;
            }
            return false;
        }

        public boolean contains(int item) {
            // Check if an item is present in the deque.
            return set.contains(item);
        }

        public int size() {
            // Get the number of elements in the deque.
            return deque.size();
        }

        public Iterator<Integer> iterator() {
            // Create an iterator for the deque.
            return deque.iterator();
        }

        @Override
        public String toString() {
            // Get a string representation of the UniqueDeque.
            return "UniqueDeque(" + deque.toString() + ")";
        }
    }
}