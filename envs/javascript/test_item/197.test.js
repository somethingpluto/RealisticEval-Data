/**
 * Node class for a circular linked list
 */
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

/**
 * PrimeGame class to encapsulate the game logic
 */
class PrimeGame {
  constructor(n) {
    this.head = null;
    this.tail = null;
    this.n = n;
    this.createPlayers();
  }

  /**
   * Create a circular linked list of players
   */
  createPlayers() {
    for (let i = 1; i <= this.n; i++) {
      const newNode = new Node(i);
      if (!this.head) {
        this.head = newNode;
        this.tail = newNode;
      } else {
        this.tail.next = newNode;
        this.tail = newNode;
      }
      this.tail.next = this.head; // Make it circular
    }
  }

  /**
   * Check if a number is prime
   * @param {number} num - The number to check
   * @return {boolean} - True if the number is prime, false otherwise
   */
  isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  /**
   * Find the order of players being removed
   * @return {Array<number>} - An array of integers representing the order of players being removed from the ring
   */
  findOrder() {
    const order = [];
    let current = this.head;
    let count = 1;

    while (this.n > 0) {
      if (this.isPrime(count)) {
        order.push(current.data);
        if (current === this.head) {
          this.head = current.next;
        }
        if (current === this.tail) {
          this.tail = this.head;
        }
        const temp = current.next;
        current.next = null;
        current = temp;
        this.n--;
      } else {
        current = current.next;
      }
      count++;
    }

    return order;
  }
}

/**
 * Simulate a game based on the order of prime numbers, using a circular linked list to represent the cyclic structure of players, and remove players one by one.
 *
 * @param {number} n - The number of players in the game.
 * @return {Array<number>} - An array of integers representing the order of players being removed from the ring.
 */
function findOrder(n) {
  const game = new PrimeGame(n);
  return game.findOrder();
}
describe("FindOrder Test Cases", () => {
    // Test Case 1: Minimum valid input with 2 players
    test("should return [2, 1] for 2 players", () => {
        expect(findOrder(2)).toEqual([2, 1]);
    });

    // Test Case 2: 3 players
    test("should return [2, 3, 1] for 3 players", () => {
        expect(findOrder(3)).toEqual([2, 3, 1]);
    });

    // Test Case 3: 5 players
    test("should return [2, 5, 3, 4, 1] for 5 players", () => {
        expect(findOrder(5)).toEqual([2, 5, 3, 4, 1]);
    });

    // Test Case 4: 7 players
    test("should return [2, 5, 4, 1, 6, 7, 3] for 7 players", () => {
        expect(findOrder(7)).toEqual([2, 5, 4, 1, 6, 7, 3]);
    });

    // Test Case 5: 10 players
    test("should return [2, 5, 10, 9, 7, 3, 4, 6, 8, 1] for 10 players", () => {
        expect(findOrder(10)).toEqual([2, 5, 10, 9, 7, 3, 4, 6, 8, 1]);
    });
});
