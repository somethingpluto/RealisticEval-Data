
class Stack:
    def __init__(self):
        self._array = []

    def push(self, value: float):
        """
        Pushes a floating-point number onto the stack.

        :param value: The floating-point number to be pushed onto the stack.
        :raises StackOverflowError: If the stack is full.
        """
        self._array.append(value)

    def pop(self) -> float:
        """
        Pops the top element off the stack and returns it.

        :return: The floating-point number that was popped from the stack.
        :raises StackUnderflowError: If the stack is empty.
        """
        top = self._array.pop()
        if top is None:
            raise StackUnderflowError("Stack is empty")
        return top

    def peek(self) -> float:
        """
        Returns the top element of the stack without removing it.

        :return: The floating-point number at the top of the stack.
        :raises StackUnderflowError: If the stack is empty.
        """
        top = self._array.pop()
        if top is None:
            raise StackUnderflowError("Stack is empty")
        return top

    def is_empty(self) -> bool:
        """
        Checks whether the stack is empty.

        :return: True if the stack is empty; False otherwise.
        """
        return self._array == []

import unittest


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