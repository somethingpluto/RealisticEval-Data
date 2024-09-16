#include <iostream>

// Node structure for the linked list
struct Node {
    int data;       // Data held by the node
    Node* next;     // Pointer to the next node in the list

    // Constructor to initialize a new node with given data
    Node(int value) : data(value), next(nullptr) {}
};

// LinkedList class definition
class LinkedList {
private:
    Node* head;     // Pointer to the first node in the list

public:
    // Constructor initializes an empty list
    LinkedList() : head(nullptr) {}

    // Destructor to clean up memory
    ~LinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }

    // Method to add a node at the beginning of the list
    void insertAtHead(int value) {
        Node* newNode = new Node(value); // Create a new node
        newNode->next = head;            // Link the new node to the current head
        head = newNode;                  // Update the head to the new node
    }

    // Method to add a node at the end of the list
    void insertAtTail(int value) {
        Node* newNode = new Node(value);
        if (head == nullptr) {
            head = newNode; // If the list is empty, new node becomes the head
        } else {
            Node* current = head;
            while (current->next != nullptr) {
                current = current->next; // Traverse to the end of the list
            }
            current->next = newNode; // Link the last node to the new node
        }
    }

    // Method to delete a node with a specific value
    void deleteValue(int value) {
        if (head == nullptr) return; // List is empty, nothing to delete

        // If the head needs to be deleted
        if (head->data == value) {
            Node* temp = head;
            head = head->next; // Update head to the next node
            delete temp;       // Delete the old head
            return;
        }

        // Traverse to find the node to delete
        Node* current = head;
        while (current->next != nullptr && current->next->data != value) {
            current = current->next;
        }

        // If the node was found, delete it
        if (current->next != nullptr) {
            Node* temp = current->next;
            current->next = current->next->next; // Unlink the node from the list
            delete temp; // Delete the node
        }
    }

    // Method to search for a value in the list
    bool search(int value) {
        Node* current = head;
        while (current != nullptr) {
            if (current->data == value) {
                return true; // Value found
            }
            current = current->next;
        }
        return false; // Value not found
    }

    // Method to print all elements in the list
    void printList() {
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->data << " -> ";
            current = current->next;
        }
        std::cout << "nullptr" << std::endl;
    }
};