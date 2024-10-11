#include <iostream>
#include <vector>
#include <stdexcept>

class MaxHeap {
private:
    std::vector<int> heap; // Vector to store heap elements

    // Helper function to maintain the max heap property
    void heapifyUp(int index) {
        if (index == 0) return; // If the index is 0, it's already the root
        int parentIndex = (index - 1) / 2; // Calculate the parent index

        // If the current node is greater than its parent, swap them
        if (heap[index] > heap[parentIndex]) {
            std::swap(heap[index], heap[parentIndex]);
            heapifyUp(parentIndex); // Recursively heapify up
        }
    }

    // Helper function to maintain the max heap property after deletion
    void heapifyDown(int index) {
        int leftChild = 2 * index + 1; // Left child index
        int rightChild = 2 * index + 2; // Right child index
        int largest = index;

        // Check if left child exists and is greater than current largest
        if (leftChild < heap.size() && heap[leftChild] > heap[largest]) {
            largest = leftChild;
        }

        // Check if right child exists and is greater than current largest
        if (rightChild < heap.size() && heap[rightChild] > heap[largest]) {
            largest = rightChild;
        }

        // If largest is not the current index, swap and heapify down
        if (largest != index) {
            std::swap(heap[index], heap[largest]);
            heapifyDown(largest); // Recursively heapify down
        }
    }

public:
    // Insert a new element into the heap
    void insert(int value) {
        heap.push_back(value); // Add value to the end of the vector
        heapifyUp(heap.size() - 1); // Restore the heap property
    }

    // Remove and return the maximum element from the heap
    int extractMax() {
        if (heap.empty()) {
            throw std::runtime_error("Heap is empty");
        }

        int maxElement = heap[0]; // Store the max element
        heap[0] = heap.back(); // Move the last element to the root
        heap.pop_back(); // Remove the last element
        heapifyDown(0); // Restore the heap property
        return maxElement; // Return the max element
    }

    // Get the maximum element without removing it
    int getMax() const {
        if (heap.empty()) {
            throw std::runtime_error("Heap is empty");
        }
        return heap[0]; // Return the root element
    }

    // Check if the heap is empty
    bool isEmpty() const {
        return heap.empty();
    }

    // Get the size of the heap
    size_t size() const {
        return heap.size();
    }

    // Display the elements of the heap
    void display() const {
        if (heap.empty()) {
            std::cout << "Heap is empty." << std::endl;
            return;
        }
        std::cout << "Heap elements: ";
        for (const int& value : heap) {
            std::cout << value << " ";
        }
        std::cout << std::endl;
    }
};

