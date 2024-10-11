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
    bool isEmpty() const {
        return head == nullptr; // Queue is empty if head is nullptr
    }

    // Function to add an element to the end of the queue
    void enqueue(int value) {
        Node* newNode = new Node(value); // Create a new node

        if (tail) {
            tail->next = newNode; // Link the new node at the end
        } else {
            head = newNode; // If the queue is empty, the new node is also the head
        }
        tail = newNode; // Update the tail to the new node
    }

    // Function to remove and return the front element of the queue
    int dequeue() {
        if (isEmpty()) {
            std::cerr << "Queue is empty. Cannot dequeue." << std::endl;
            return -1; // Return an invalid value or throw an exception
        }

        Node* temp = head; // Temporarily store the head node
        int value = head->data; // Get the data from the head node
        head = head->next; // Move head to the next node

        if (head == nullptr) {
            tail = nullptr; // If the queue becomes empty, update the tail as well
        }

        delete temp; // Free the memory of the old head node
        return value; // Return the dequeued value
    }

    // Function to get the front element without removing it
    int front() const {
        if (isEmpty()) {
            std::cerr << "Queue is empty. Cannot access front." << std::endl;
            return -1; // Return an invalid value
        }
        return head->data; // Return the front value
    }
};