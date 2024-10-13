class MaxHeap:
    def __init__(self):
        self.heap = []  # List to store heap elements

    # Helper function to maintain the max heap property
    def heapify_up(self, index):
        if index == 0:
            return  # If the index is 0, it's already the root
        parent_index = (index - 1) // 2  # Calculate the parent index
        # If the current node is greater than its parent, swap them
        if self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)  # Recursively heapify up

    # Helper function to maintain the max heap property after deletion
    def heapify_down(self, index):
        left_child = 2 * index + 1  # Left child index
        right_child = 2 * index + 2  # Right child index
        largest = index

        # Check if left child exists and is greater than current largest
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        # Check if right child exists and is greater than current largest
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        # If largest is not the current index, swap and heapify down
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)  # Recursively heapify down

    # Insert a new element into the heap
    def insert(self, value):
        self.heap.append(value)  # Add value to the end of the list
        self.heapify_up(len(self.heap) - 1)  # Restore the heap property

    # Remove and return the maximum element from the heap
    def extract_max(self):
        if not self.heap:
            raise RuntimeError("Heap is empty")
        max_element = self.heap[0]  # Store the max element
        self.heap[0] = self.heap[-1]  # Move the last element to the root
        self.heap.pop()  # Remove the last element
        self.heapify_down(0)  # Restore the heap property
        return max_element  # Return the max element

    # Get the maximum element without removing it
    def get_max(self):
        if not self.heap:
            raise RuntimeError("Heap is empty")
        return self.heap[0]  # Return the root element

    # Check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # Get the size of the heap
    def size(self):
        return len(self.heap)

    # Display the elements of the heap
    def display(self):
        if not self.heap:
            print("Heap is empty.")
            return
        print("Heap elements:", ' '.join(map(str, self.heap)))