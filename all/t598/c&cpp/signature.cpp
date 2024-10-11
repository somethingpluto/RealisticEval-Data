#include <iostream>

// Node structure for linked list
struct Node {
    int data;      // Data value of the node
    Node* next;    // Pointer to the next node in the linked list

    Node(int val) : data(val), next(nullptr) {} // Constructor to initialize the node
};

// Queue class
class Queue {
private:
    Node* head; // Pointer to the front of the queue
    Node* tail; // Pointer to the end of the queue

public:
    // Constructor to initialize the queue
    Queue() : head(nullptr), tail(nullptr) {}

    // Destructor to clean up the queue
    ~Queue() {
        while (!isEmpty()) {
            dequeue();
        }
    }

    // Function to check if the queue is empty
    bool isEmpty() const {}

    // Function to add an element to the end of the queue
    void enqueue(int value) {}

    // Function to remove and return the front element of the queue
    int dequeue() {}

    // Function to get the front element without removing it
    int front() const {}
};