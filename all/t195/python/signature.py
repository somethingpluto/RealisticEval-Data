class Stack:
    """
    Implement a floating-point stack structure based on arrays.

    This class provides basic stack operations including push, pop, peek, and checking if the stack is empty.
    The stack is implemented using a fixed-size array. If the stack reaches its maximum capacity, no more elements
    can be pushed onto it until space is freed by popping elements.
    """

    def push(self, value: float):
        """
        Pushes a floating-point number onto the stack.

        :param value: The floating-point number to be pushed onto the stack.
        :raises StackOverflowError: If the stack is full.
        """

    def pop(self) -> float:
        """
        Pops the top element off the stack and returns it.

        :return: The floating-point number that was popped from the stack.
        :raises StackUnderflowError: If the stack is empty.
        """

    def peek(self) -> float:
        """
        Returns the top element of the stack without removing it.

        :return: The floating-point number at the top of the stack.
        :raises StackUnderflowError: If the stack is empty.
        """

    def is_empty(self) -> bool:
        """
        Checks whether the stack is empty.

        :return: True if the stack is empty; False otherwise.
        """
