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
        items.addLast(element);
    }

    /**
     * Removes and returns the element from the front of the queue.
     * @returns The removed element from the front of the queue, or "Underflow" if the queue is empty.
     */
    public Object dequeue() {
        if (isEmpty()) {
            return "Underflow";
        }
        return items.removeFirst();
    }

    /**
     * Returns the front element of the queue without removing it.
     * @returns The front element of the queue, or "No elements in Queue" if the queue is empty.
     */
    public Object front() {
        if (isEmpty()) {
            return "No elements in Queue";
        }
        return items.getFirst();
    }

    /**
     * Checks if the queue is empty.
     * @returns True if the queue is empty, otherwise false.
     */
    public boolean isEmpty() {
        return items.isEmpty();
    }

    /**
     * Returns a string representation of all the elements in the queue.
     * @returns A string containing all elements in the queue, separated by spaces.
     */
    public String printQueue() {
        return String.join(" ", items.stream().map(Object::toString).toArray(String[]::new));
    }

    public static void main(String[] args) {
        Queue queue = new Queue();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        System.out.println("Queue: " + queue.printQueue()); // Output: Queue: 1 2 3
        System.out.println("Dequeue: " + queue.dequeue()); // Output: Dequeue: 1
        System.out.println("Front: " + queue.front()); // Output: Front: 2
        System.out.println("Is Empty: " + queue.isEmpty()); // Output: Is Empty: false
    }
}