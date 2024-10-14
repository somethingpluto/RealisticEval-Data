import java.util.LinkedList;

public class Queue {
    private LinkedList<Object> items;

    public Queue() {
        this.items = new LinkedList<>();
    }

    /**
     * Adds an element to the end of the queue.
     * @param element The element to be added to the queue.
     */
    public void enqueue(Object element) {
    }

    /**
     * Removes and returns the element from the front of the queue.
     * @returns The removed element from the front of the queue, or "Underflow" if the queue is empty.
     */
    public Object dequeue() {
    }

    /**
     * Returns the front element of the queue without removing it.
     * @returns The front element of the queue, or "No elements in Queue" if the queue is empty.
     */
    public Object front() {
    }

    /**
     * Checks if the queue is empty.
     * @returns True if the queue is empty, otherwise false.
     */
    public boolean isEmpty() {
    }

    /**
     * Returns a string representation of all the elements in the queue.
     * @returns A string containing all elements in the queue, separated by spaces.
     */
    public String printQueue() {
    }
}