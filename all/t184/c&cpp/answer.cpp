#include <iostream>
#include <vector>
#include <stdexcept>

class PriorityQueue {
private:
    std::vector<int> heap; // This will store the elements of the heap

    // Helper function to get the index of the parent
    int parent(int index) {
        return (index - 1) / 2;
    }

    // Helper function to get the index of the left child
    int leftChild(int index) {
        return 2 * index + 1;
    }

    // Helper function to get the index of the right child
    int rightChild(int index) {
        return 2 * index + 2;
    }

    // Helper function to swap two elements in the heap
    void swap(int &a, int &b) {
        int temp = a;
        a = b;
        b = temp;
    }

    // Heapify up to maintain the max-heap property after insertion
    void heapifyUp(int index) {
        while (index > 0 && heap[parent(index)] < heap[index]) {
            swap(heap[parent(index)], heap[index]);
            index = parent(index);
        }
    }

    // Heapify down to maintain the max-heap property after deletion
    void heapifyDown(int index) {
        int size = heap.size();
        int largest = index;

        int left = leftChild(index);
        int right = rightChild(index);

        if (left < size && heap[left] > heap[largest]) {
            largest = left;
        }

        if (right < size && heap[right] > heap[largest]) {
            largest = right;
        }

        if (largest != index) {
            swap(heap[index], heap[largest]);
            heapifyDown(largest);
        }
    }

public:
    // Insert an element into the priority queue
    void push(int value) {
        heap.push_back(value);
        heapifyUp(heap.size() - 1);
    }

    // Remove the maximum element from the priority queue
    void pop() {
        if (heap.empty()) {
            throw std::runtime_error("Priority queue is empty");
        }
        heap[0] = heap.back();
        heap.pop_back();
        if (!heap.empty()) {
            heapifyDown(0);
        }
    }

    // Get the maximum element without removing it
    int top() {
        if (heap.empty()) {
            throw std::runtime_error("Priority queue is empty");
        }
        return heap[0];
    }

    // Check if the priority queue is empty
    bool isEmpty() {
        return heap.empty();
    }

    // Get the size of the priority queue
    int size() {
        return heap.size();
    }
};