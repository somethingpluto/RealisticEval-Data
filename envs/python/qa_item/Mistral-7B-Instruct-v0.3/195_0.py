import sys

class Stack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = [0.0] * self.capacity
        self.top = -1

    def push(self, value: float):
        if self.top == self.capacity - 1:
            raise StackOverflowError("Stack Overflow Error: Stack is full.")
        self.stack[self.top + 1] = value
        self.top += 1

    def pop(self) -> float:
        if self.top == -1:
            raise StackUnderflowError("Stack Underflow Error: Stack is empty.")
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self) -> float:
        if self.top == -1:
            raise StackUnderflowError("Stack Underflow Error: Stack is empty.")
        return self.stack[self.top]

    def is_empty(self) -> bool:
        return self.top == -1
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