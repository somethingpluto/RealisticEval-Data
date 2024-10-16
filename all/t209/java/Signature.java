package org.real.temp;

/**
 * Node structure for the linked list.
 */
class Node {
    int data;       // Data held by the node
    Node next;     // Pointer to the next node in the list

    /**
     * Constructor to initialize a new node with given data.
     *
     * @param value the data value for the node
     */
    Node(int value) {
        this.data = value;
        this.next = null;
    }
}

/**
 * LinkedList class definition.
 */
class LinkedList {
    /**
     * Method to add a node at the beginning of the list.
     *
     * @param value the data value for the new node
     */
    void insertAtHead(int value) {
        // Implementation goes here
    }

    /**
     * Method to add a node at the end of the list.
     *
     * @param value the data value for the new node
     */
    void insertAtTail(int value) {
        // Implementation goes here
    }

    /**
     * Method to delete a node with a specific value.
     *
     * @param value the data value of the node to delete
     */
    void deleteValue(int value) {
        // Implementation goes here
    }

    /**
     * Method to search for a value in the list.
     *
     * @param value the data value to search for
     * @return true if the value is found, false otherwise
     */
    boolean search(int value) {
        // Implementation goes here
        return false;
    }

    /**
     * Method to print all elements in the list.
     */
    void printList() {
        // Implementation goes here
    }
}