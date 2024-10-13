import unittest

class Tester(unittest.TestCase):
    
    def setUp(self):
        """ Set up a new PriorityQueue instance for each test """
        self.pq = PriorityQueue()
    
    def test_insert_and_access_maximum_element(self):
        """ Test case: Insert and access maximum element """
        self.pq.push(10)
        self.pq.push(20)
        self.pq.push(5)
        self.pq.push(30)
        self.pq.push(15)
        self.assertEqual(self.pq.top(), 30)  # Ensure the max element is 30
    
    def test_remove_maximum_element(self):
        """ Test case: Remove maximum element """
        self.pq.push(10)
        self.pq.push(20)
        self.pq.push(5)
        self.pq.push(30)
        self.pq.pop()  # Remove 30
        self.assertEqual(self.pq.top(), 20)  # Now the max should be 20
        self.pq.pop()  # Remove 20
        self.assertEqual(self.pq.top(), 10)  # Now the max should be 10
    
    def test_check_empty_queue(self):
        """ Test case: Check if the queue is empty """
        self.assertTrue(self.pq.isEmpty())  # Initially empty
        self.pq.push(10)
        self.assertFalse(self.pq.isEmpty())  # Now not empty
        self.pq.pop()
        self.assertTrue(self.pq.isEmpty())  # Back to empty
    
    def test_pop_from_empty_queue(self):
        """ Test case: Pop from empty queue (should raise exception) """
        with self.assertRaises(RuntimeError):
            self.pq.pop()  # Should raise an error
    
    def test_access_top_of_empty_queue(self):
        """ Test case: Access top of empty queue (should raise exception) """
        with self.assertRaises(RuntimeError):
            self.pq.top()  # Should raise an error
    
    def test_maintain_max_heap_property(self):
        """ Test case: Maintain max-heap property """
        self.pq.push(3)
        self.pq.push(1)
        self.pq.push(4)
        self.pq.push(2)
        self.assertEqual(self.pq.top(), 4)  # Ensure max is 4
        self.pq.pop()  # Remove 4
        self.assertEqual(self.pq.top(), 3)  # Now max is 3
        self.pq.push(5)  # Add 5
        self.assertEqual(self.pq.top(), 5)  # Ensure max is now 5
