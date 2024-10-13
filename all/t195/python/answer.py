class StackOverflowError(Exception):
    """Custom exception for stack overflow."""
    pass


class StackUnderflowError(Exception):
    """Custom exception for stack underflow."""
    pass


class Stack:
    """
    Implement a floating-point stack structure based on arrays.

    This class provides basic stack operations including push, pop, peek,
    and checking if the stack is empty. The stack is implemented using a
    fixed-size list. If the stack reaches its maximum capacity, no more
    elements can be pushed onto it until space is freed by popping elements.
    """

    MAX_SIZE = 100  # Maximum size of the stack

    def __init__(self):
        """Constructor that initializes the stack."""
        self.stack = [0.0] * self.MAX_SIZE  # Initialize stack with zeros
        self.top = -1  # Indicates that the stack is empty

    def push(self, value: float):
        """
        Pushes a floating-point number onto the stack.

        :param value: The floating-point number to be pushed onto the stack.
        :raises StackOverflowError: If the stack is full.
        """
        if self.top >= self.MAX_SIZE - 1:
            raise StackOverflowError("Stack overflow: Cannot push onto a full stack.")
        self.top += 1
        self.stack[self.top] = value

    def pop(self) -> float:
        """
        Pops the top element off the stack and returns it.

        :return: The floating-point number that was popped from the stack.
        :raises StackUnderflowError: If the stack is empty.
        """
        if self.top < 0:
            raise StackUnderflowError("Stack underflow: Cannot pop from an empty stack.")
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self) -> float:
        """
        Returns the top element of the stack without removing it.

        :return: The floating-point number at the top of the stack.
        :raises StackUnderflowError: If the stack is empty.
        """
        if self.top < 0:
            raise StackUnderflowError("Stack underflow: Cannot peek on an empty stack.")
        return self.stack[self.top]

    def is_empty(self) -> bool:
        """
        Checks whether the stack is empty.

        :return: True if the stack is empty; False otherwise.
        """
        return self.top < 0