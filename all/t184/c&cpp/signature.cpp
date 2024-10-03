#include <iostream>
#include <vector>
#include <stdexcept>

class PriorityQueue {
private:
    std::vector<int> heap; // This will store the elements of the heap

    // Helper function to get the index of the parent
    int parent(int index) {}

    // Helper function to get the index of the left child
    int leftChild(int index) {}

    // Helper function to get the index of the right child
    int rightChild(int index) {}

    // Helper function to swap two elements in the heap
    void swap(int &a, int &b) {}

    // Heapify up to maintain the max-heap property after insertion
    void heapifyUp(int index) {}

    // Heapify down to maintain the max-heap property after deletion
    void heapifyDown(int index) {}

public:
    // Insert an element into the priority queue
    void push(int value) {}

    // Remove the maximum element from the priority queue
    void pop() {}

    // Get the maximum element without removing it
    int top() {}

    // Check if the priority queue is empty
    bool isEmpty() {}

    // Get the size of the priority queue
    int size() {}
};