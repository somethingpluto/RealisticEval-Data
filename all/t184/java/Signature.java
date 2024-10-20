/**
 * A class representing a max-heap priority queue.
 */
public class Answer {
    static class PriorityQueue{
private List<Integer> heap; // This will store the elements of the heap

    /** 
     * Constructor to initialize the priority queue.
     */
    public PriorityQueue() {
        heap = new ArrayList<>();
    }

    /**
     * Helper function to get the index of the parent.
     * 
     * @param index The index of the child node.
     * @return The index of the parent node.
     */
    private int parent(int index) {
        return (index - 1) / 2;
    }

    /**
     * Helper function to get the index of the left child.
     * 
     * @param index The index of the parent node.
     * @return The index of the left child node.
     */
    private int leftChild(int index) {
        return 2 * index + 1;
    }

    /**
     * Helper function to get the index of the right child.
     * 
     * @param index The index of the parent node.
     * @return The index of the right child node.
     */
    private int rightChild(int index) {
        return 2 * index + 2;
    }

    /**
     * Helper function to swap two elements in the heap.
     * 
     * @param aIndex The index of the first element.
     * @param bIndex The index of the second element.
     */
    private void swap(int aIndex, int bIndex) {

    }

    /**
     * Heapify up to maintain the max-heap property after insertion.
     * 
     * @param index The index of the newly inserted element.
     */
    private void heapifyUp(int index) {
        
    }

    /**
     * Heapify down to maintain the max-heap property after deletion.
     * 
     * @param index The index of the element to be heapified down.
     */
    private void heapifyDown(int index) {
        
    }

    /**
     * Insert an element into the priority queue.
     * 
     * @param value The value to be inserted.
     */
    public void push(int value) {
        
    }

    /**
     * Remove the maximum element from the priority queue.
     * 
     * @throws RuntimeException if the priority queue is empty.
     */
    public void pop() {
        
    }

    /**
     * Get the maximum element without removing it.
     * 
     * @return The maximum element.
     * @throws RuntimeException if the priority queue is empty.
     */
    public int top() {
        
    }

    /**
     * Check if the priority queue is empty.
     * 
     * @return true if the priority queue is empty, false otherwise.
     */
    public boolean isEmpty() {
        return heap.isEmpty();
    }

    /**
     * Get the size of the priority queue.
     * 
     * @return The number of elements in the priority queue.
     */
    public int size() {
        return heap.size();
    }
    }
    
}