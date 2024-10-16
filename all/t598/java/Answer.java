package org.real.temp;

// Node class for linked list
class Node {
    int data;      // Data value of the node
    Node next;    // Reference to the next node in the linked list

    // Constructor to initialize the node
    Node(int val) {
        this.data = val;
        this.next = null;
    }
}

// Queue class
public class Answer {
    private Node head; // Reference to the front of the queue
    private Node tail; // Reference to the end of the queue

    // Constructor to initialize the queue
    public Answer() {
        this.head = null;
        this.tail = null;
    }

    // Function to check if the queue is empty
    public boolean isEmpty() {
        return head == null; // Queue is empty if head is null
    }

    // Function to add an element to the end of the queue
    public void enqueue(int value) {
        Node newNode = new Node(value); // Create a new node

        if (tail != null) {
            tail.next = newNode; // Link the new node at the end
        } else {
            head = newNode; // If the queue is empty, the new node is also the head
        }
        tail = newNode; // Update the tail to the new node
    }

    // Function to remove and return the front element of the queue
    public int dequeue() {
        if (isEmpty()) {
            System.err.println("Queue is empty. Cannot dequeue.");
            return -1; // Return an invalid value or throw an exception
        }

        Node temp = head; // Temporarily store the head node
        int value = head.data; // Get the data from the head node
        head = head.next; // Move head to the next node

        if (head == null) {
            tail = null; // If the queue becomes empty, update the tail as well
        }

        return value; // Return the dequeued value
    }

    // Function to get the front element without removing it
    public int front() {
        if (isEmpty()) {
            System.err.println("Queue is empty. Cannot access front.");
            return -1; // Return an invalid value
        }
        return head.data; // Return the front value
    }
}