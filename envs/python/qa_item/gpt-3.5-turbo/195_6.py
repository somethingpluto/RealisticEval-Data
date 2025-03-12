class Stack:
    """
    Implement a floating-point stack structure based on arrays.

    This class provides basic stack operations including push, pop, peek, and checking if the stack is empty.
    The stack is implemented using a fixed-size array. If the stack reaches its maximum capacity, no more elements
    can be pushed onto it until space is freed by popping elements.
    """

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.stack = []
    
    def push(self, value: float):
        """
        Pushes a floating-point number onto the stack.

        :param value: The floating-point number to be pushed onto the stack.
        :raises StackOverflowError: If the stack is full.
        """
        if len(self.stack) == self.max_size:
            raise StackOverflowError("Stack is full")
        self.stack.append(value)

    def pop(self) -> float:
        """
        Pops the top element off the stack and returns it.

        :return: The floating-point number that was popped from the stack.
        :raises StackUnderflowError: If the stack is empty.
        """
        if not self.stack:
            raise StackUnderflowError("Stack is empty")
        return self.stack.pop()

    def peek(self) -> float:
        """
        Returns the top element of the stack without removing it.

        :return: The floating-point number at the top of the stack.
        :raises StackUnderflowError: If the stack is empty.
        """
        if not self.stack:
            raise StackUnderflowError("Stack is empty")
        return self.stack[-1]

    def is_empty(self) -> bool:
        """
        Checks whether the stack is empty.

        :return: True if the stack is empty; False otherwise.
        """
        return len(self.stack) == 0

class StackOverflowError(Exception):
    pass

class StackUnderflowError(Exception):
    pass
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