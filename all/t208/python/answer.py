class PriorityQueue:
    def __init__(self):
        """Constructor to initialize the priority queue."""
        self.heap = []  # Internal storage for the binary heap

    def swap(self, a, b):
        """Helper function to swap two elements in the heap."""
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def heapify_up(self, index):
        """Maintain the heap property by "bubbling up" the element at index."""
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        """Maintain the heap property by "bubbling down" the element at index."""
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)

    def insert(self, value):
        """Insert a new element into the priority queue."""
        self.heap.append(value)  # Add the new element at the end of the heap
        self.heapify_up(len(self.heap) - 1)  # Restore the heap property

    def extract_min(self):
        """Get and remove the minimum element from the priority queue."""
        if self.is_empty():
            raise RuntimeError("Priority queue is empty.")

        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]  # Move the last element to the root
        self.heap.pop()  # Remove the last element
        self.heapify_down(0)  # Restore the heap property

        return min_value

    def peek_min(self):
        """Peek at the minimum element without removing it."""
        if self.is_empty():
            raise RuntimeError("Priority queue is empty.")

        return self.heap[0]

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.heap) == 0

    def size(self):
        """Get the size of the priority queue."""
        return len(self.heap)

    def print_heap(self):
        """Print the contents of the priority queue (for debugging purposes)."""
        print("Heap contents:", ' '.join(map(str, self.heap)))