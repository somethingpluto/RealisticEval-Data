class PriorityQueue:
    def __init__(self):
        self.heap = []  # This will store the elements of the heap

    # Helper function to get the index of the parent
    def parent(self, index):
        return (index - 1) // 2

    # Helper function to get the index of the left child
    def left_child(self, index):
        return 2 * index + 1

    # Helper function to get the index of the right child
    def right_child(self, index):
        return 2 * index + 2

    # Helper function to swap two elements in the heap
    def swap(self, a_index, b_index):
        self.heap[a_index], self.heap[b_index] = self.heap[b_index], self.heap[a_index]

    # Heapify up to maintain the max-heap property after insertion
    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.swap(self.parent(index), index)
            index = self.parent(index)

    # Heapify down to maintain the max-heap property after deletion
    def heapify_down(self, index):
        size = len(self.heap)
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.heapify_down(largest)

    # Insert an element into the priority queue
    def push(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    # Remove the maximum element from the priority queue
    def pop(self):
        if self.is_empty():
            raise RuntimeError("Priority queue is empty")
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if not self.is_empty():
            self.heapify_down(0)

    # Get the maximum element without removing it
    def top(self):
        if self.is_empty():
            raise RuntimeError("Priority queue is empty")
        return self.heap[0]

    # Check if the priority queue is empty
    def is_empty(self):
        return len(self.heap) == 0

    # Get the size of the priority queue
    def size(self):
        return len(self.heap)
