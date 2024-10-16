package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    private List<Integer> heap; // This will store the elements of the heap

    public Answer() {
        heap = new ArrayList<>();
    }

    // Helper function to get the index of the parent
    private int parent(int index) {
        return (index - 1) / 2;
    }

    // Helper function to get the index of the left child
    private int leftChild(int index) {
        return 2 * index + 1;
    }

    // Helper function to get the index of the right child
    private int rightChild(int index) {
        return 2 * index + 2;
    }

    // Helper function to swap two elements in the heap
    private void swap(int aIndex, int bIndex) {
        int temp = heap.get(aIndex);
        heap.set(aIndex, heap.get(bIndex));
        heap.set(bIndex, temp);
    }

    // Heapify up to maintain the max-heap property after insertion
    private void heapifyUp(int index) {
        while (index > 0 && heap.get(parent(index)) < heap.get(index)) {
            swap(parent(index), index);
            index = parent(index);
        }
    }

    // Heapify down to maintain the max-heap property after deletion
    private void heapifyDown(int index) {
        int size = heap.size();
        int largest = index;

        int left = leftChild(index);
        int right = rightChild(index);

        if (left < size && heap.get(left) > heap.get(largest)) {
            largest = left;
        }

        if (right < size && heap.get(right) > heap.get(largest)) {
            largest = right;
        }

        if (largest != index) {
            swap(index, largest);
            heapifyDown(largest);
        }
    }

    // Insert an element into the priority queue
    public void push(int value) {
        heap.add(value);
        heapifyUp(heap.size() - 1);
    }

    // Remove the maximum element from the priority queue
    public void pop() {
        if (heap.isEmpty()) {
            throw new RuntimeException("Priority queue is empty");
        }
        heap.set(0, heap.get(heap.size() - 1));
        heap.remove(heap.size() - 1);
        if (!heap.isEmpty()) {
            heapifyDown(0);
        }
    }

    // Get the maximum element without removing it
    public int top() {
        if (heap.isEmpty()) {
            throw new RuntimeException("Priority queue is empty");
        }
        return heap.get(0);
    }

    // Check if the priority queue is empty
    public boolean isEmpty() {
        return heap.isEmpty();
    }

    // Get the size of the priority queue
    public int size() {
        return heap.size();
    }
}