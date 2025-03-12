class Stack:
    def __init__(self, max_size: int = 10):
        self.stack = []
        self.max_size = max_size

    def push(self, value: float):
        if len(self.stack) >= self.max_size:
            raise StackOverflowError("Stack is full, cannot push new element.")
        self.stack.append(value)

    def pop(self) -> float:
        if len(self.stack) == 0:
            raise StackUnderflowError("Stack is empty, cannot pop element.")
        return self.stack.pop()

    def peek(self) -> float:
        if len(self.stack) == 0:
            raise StackUnderflowError("Stack is empty, cannot peek.")
        return self.stack[-1]

    def is_empty(self) -> bool:
        return len(self.stack) == 0
class Tester(unittest.TestCase):

    def test_stack_operations(self):
        """Test stack_t Test Cases"""
        stack = Stack(10)  # Provide capacity when creating the stack

        # Test Case 1: Pushing and popping a single element
        stack.push(3.14)
        self.assertEqual(stack.pop(), 3.14)
        self.assertTrue(stack.is_empty())  # Change to is_empty

        # Test Case 2: Pushing multiple elements and checking peek
        stack.push(1.23)
        stack.push(4.56)
        self.assertEqual(stack.peek(), 4.56)
        self.assertEqual(stack.pop(), 4.56)
        self.assertEqual(stack.pop(), 1.23)
        self.assertTrue(stack.is_empty())  # Change to is_empty

        # Test Case 3: Pop from an empty stack (should throw an exception)
        with self.assertRaises(StackUnderflowError):
            stack.pop()

        # Test Case 4: Peek on an empty stack (should throw an exception)
        with self.assertRaises(StackUnderflowError):
            stack.peek()

        # Test Case 5: Push elements until stack is full and attempt to push another element
        full_stack = Stack(100)  # Provide capacity when creating the stack
        for i in range(100):
            full_stack.push(float(i) + 0.5)

        with self.assertRaises(StackOverflowError):
            full_stack.push(100.5)

if __name__ == '__main__':
    unittest.main()