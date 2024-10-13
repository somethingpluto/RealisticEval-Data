class Node:
    """A node in a circular linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class PrimeGame:
    """A class that simulates a game where players are removed based on the order of prime numbers."""

    def __init__(self, num_players):
        if num_players < 2:
            raise ValueError("Number of players must be at least 2.")
        self.num_players = num_players
        self.head = self.create_circular_linked_list(num_players)

    def __del__(self):
        """Destructor to clean up the circular linked list."""
        current = self.head
        for _ in range(self.num_players):
            temp = current
            current = current.next
            del temp

    def find_order(self):
        """Finds the order of players going out of the ring based on prime number steps."""
        primes = self.generate_primes(self.num_players)
        order = []
        current = self.head
        remaining_players = self.num_players

        while remaining_players > 1 and primes:
            step = primes.pop(0) - 1  # Get the next prime and decrease by 1
            for _ in range(step):
                current = current.next

            to_remove = current.next
            order.append(to_remove.data)
            current.next = to_remove.next  # Remove the player from the list
            del to_remove
            remaining_players -= 1

        order.append(current.data)  # The last remaining player
        return order

    def create_circular_linked_list(self, n):
        """Creates a circular linked list with n nodes."""
        head = Node(1)
        current = head
        for i in range(2, n + 1):
            current.next = Node(i)
            current = current.next
        current.next = head  # Make the linked list circular
        return head

    def generate_primes(self, limit):
        """Generates all prime numbers up to a given limit using the Sieve of Eratosthenes."""
        if limit < 2:
            return []  # No primes less than 2
        is_prime = [True] * (limit + 1)
        primes = []

        for i in range(2, int(limit ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        for i in range(2, limit + 1):
            if is_prime[i]:
                primes.append(i)

        return primes


def find_order(n):
    """Simulate a game based on the order of prime numbers."""
    game = PrimeGame(n)  # Create an instance of PrimeGame with n players
    return game.find_order()  # Get the order of removed players