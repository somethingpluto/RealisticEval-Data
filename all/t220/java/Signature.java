/**
 * A class representing a unique deque that maintains both order and uniqueness of elements.
 */
public class UniqueDeque {

    private LinkedList<Integer> deque;
    private Set<Integer> set;

    /**
     * Constructs a new UniqueDeque object.
     */
    public UniqueDeque() {
        this.deque = new LinkedList<>();
        this.set = new HashSet<>();
    }

    /**
     * Adds an item to the deque if it is not already present.
     *
     * @param item The item to add.
     * @return true if the item was added, false if it was already present.
     */
    public boolean add(int item) {
        if (!set.contains(item)) {
            deque.addLast(item);
            set.add(item);
            return true;
        }
        return false;
    }

    /**
     * Removes an item from the deque if it exists.
     *
     * @param item The item to remove.
     * @return true if the item was removed, false if it was not found.
     */
    public boolean delete(int item) {
        if (set.contains(item)) {
            deque.removeFirstOccurrence(item);
            set.remove(item);
            return true;
        }
        return false;
    }

    /**
     * Checks if an item is present in the deque.
     *
     * @param item The item to check.
     * @return true if the item is present, false otherwise.
     */
    public boolean contains(int item) {
        return set.contains(item);
    }

    /**
     * Gets the number of elements in the deque.
     *
     * @return the number of unique elements in the deque.
     */
    public int size() {
        return deque.size();
    }

    /**
     * Creates an iterator for the deque.
     *
     * @return an iterator over the elements in the deque.
     */
    public Iterator<Integer> iterator() {
        return deque.iterator();
    }

    /**
     * Gets a string representation of the UniqueDeque.
     *
     * @return the string representation of the deque.
     */
    @Override
    public String toString() {
        return "UniqueDeque(" + deque.toString() + ")";
    }

    // Example usage
    public static void main(String[] args) {
        UniqueDeque uniqueDeque = new UniqueDeque();
        System.out.println(uniqueDeque.add(1)); // true
        System.out.println(uniqueDeque.add(2)); // true
        System.out.println(uniqueDeque.add(1)); // false
        System.out.println(uniqueDeque.delete(2)); // true
        System.out.println(uniqueDeque.delete(3)); // false
        System.out.println(uniqueDeque.contains(1)); // true
        System.out.println(uniqueDeque.size()); // 1
        System.out.println(uniqueDeque.toString()); // UniqueDeque([1])
    }
}
