from collections import deque


class UniqueDeque:
    def __init__(self):
        """
        Initialize a UniqueDeque object using a deque and a set.
        The deque stores elements in order, while the set ensures uniqueness.
        """
        self._deque = deque()
        self._set = set()

    def add(self, item):
        """
        Add an item to the deque if it is not already present.

        Parameters:
        - item: The item to add.

        Returns:
        - bool: True if the item was added, False if it was already present.
        """
        if item not in self._set:
            self._deque.append(item)
            self._set.add(item)
            return True
        return False

    def delete(self, item):
        """
        Remove an item from the deque if it exists.

        Parameters:
        - item: The item to remove.

        Returns:
        - bool: True if the item was removed, False if it was not found.
        """
        if item in self._set:
            self._deque.remove(item)
            self._set.remove(item)
            return True
        return False

    def contains(self, item):
        """
        Check if an item is present in the deque.

        Parameters:
        - item: The item to check.

        Returns:
        - bool: True if the item is present, False otherwise.
        """
        return item in self._set

    def __len__(self):
        """
        Get the number of elements in the deque.

        Returns:
        - int: The number of unique elements in the deque.
        """
        return len(self._deque)

    def __iter__(self):
        """
        Create an iterator for the deque.

        Returns:
        - iterator: An iterator over the elements in the deque.
        """
        return iter(self._deque)

    def __repr__(self):
        """
        Get a string representation of the UniqueDeque.

        Returns:
        - str: The string representation of the deque.
        """
        return f"UniqueDeque({list(self._deque)})"