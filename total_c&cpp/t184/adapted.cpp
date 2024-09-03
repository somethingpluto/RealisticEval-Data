#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
class PriorityQueue {
private:
    std::vector<int> heap;

    // Function to maintain the heap property by moving elements down
    void heapifyDown(int index) {
        int size = heap.size();
        int largest = index;
        int leftChildIdx = 2 * index + 1;
        int rightChildIdx = 2 * index + 2;

        if (leftChildIdx < size && heap[leftChildIdx] > heap[largest])
            largest = leftChildIdx;
        if (rightChildIdx < size && heap[rightChildIdx] > heap[largest])
            largest = rightChildIdx;

        if (largest != index) {
            std::swap(heap[index], heap[largest]);
            heapifyDown(largest);
        }
    }

    // Function to maintain the heap property by moving elements up
    void heapifyUp(int index) {
        if (index && heap[(index - 1) / 2] < heap[index]) {
            std::swap(heap[index], heap[(index - 1) / 2]);
            heapifyUp((index - 1) / 2);
        }
    }

public:
    // Function to check if the priority queue is empty
    bool isEmpty() const {
        return heap.empty();
    }

    // Function to return the size of the priority queue
    int size() const {
        return heap.size();
    }

    // Function to insert a new element into the priority queue
    void push(int key) {
        heap.push_back(key);
        int index = heap.size() - 1;
        heapifyUp(index);
    }

    // Function to remove the element with the highest priority
    void pop() {
        if (isEmpty())
            throw std::runtime_error("Priority queue underflow!");
        heap[0] = heap.back();
        heap.pop_back();
        heapifyDown(0);
    }

    // Function to get the element with the highest priority
    int top() const {
        if (isEmpty())
            throw std::runtime_error("Priority queue underflow!");
        return heap[0];
    }
};