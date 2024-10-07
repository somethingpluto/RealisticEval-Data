#include <iostream>
#include <vector>
#include <stdexcept>

class PriorityQueue {
private:
    std::vector<int> heap; // Internal storage for the binary heap

    // Helper function to swap two elements in the heap
    void swap(int& a, int& b) {
        int temp = a;
        a = b;
        b = temp;
    }

    // Function to maintain the heap property by "bubbling up" the element at index
    void heapifyUp(int index) {
        while (index > 0) {
            int parentIndex = (index - 1) / 2;
            if (heap[index] < heap[parentIndex]) {
                swap(heap[index], heap[parentIndex]);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    // Function to maintain the heap property by "bubbling down" the element at index
    void heapifyDown(int index) {
        int leftChild = 2 * index + 1;
        int rightChild = 2 * index + 2;
        int smallest = index;

        if (leftChild < heap.size() && heap[leftChild] < heap[smallest]) {
            smallest = leftChild;
        }

        if (rightChild < heap.size() && heap[rightChild] < heap[smallest]) {
            smallest = rightChild;
        }

        if (smallest != index) {
            swap(heap[index], heap[smallest]);
            heapifyDown(smallest);
        }
    }

public:
    // Constructor
    PriorityQueue() {}

    // Function to insert a new element into the priority queue
    void insert(int value) {
        heap.push_back(value);  // Add the new element at the end of the heap
        heapifyUp(heap.size() - 1); // Restore the heap property
    }

    // Function to get and remove the minimum element from the priority queue
    int extractMin() {
        if (heap.empty()) {
            throw std::runtime_error("Priority queue is empty.");
        }

        int minValue = heap[0];
        heap[0] = heap.back(); // Move the last element to the root
        heap.pop_back();       // Remove the last element
        heapifyDown(0);        // Restore the heap property

        return minValue;
    }

    // Function to peek at the minimum element without removing it
    int peekMin() const {
        if (heap.empty()) {
            throw std::runtime_error("Priority queue is empty.");
        }
        return heap[0];
    }

    // Function to check if the priority queue is empty
    bool isEmpty() const {
        return heap.empty();
    }

    // Function to get the size of the priority queue
    int size() const {
        return heap.size();
    }

    // Function to print the contents of the priority queue (for debugging purposes)
    void print() const {
        for (int value : heap) {
            std::cout << value << " ";
        }
        std::cout << std::endl;
    }
};
