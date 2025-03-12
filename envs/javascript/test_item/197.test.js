/**
 * Simulate a game based on the order of prime numbers, using a circular linked list to represent the cyclic structure of players, and remove players one by one.
 *
 * This function creates an instance of the PrimeGame class, which encapsulates the logic
 * for simulating the game. It then calls the findOrder method on the PrimeGame object
 * to determine and return the order in which players are removed based on the sequence of prime numbers.
 *
 * @param {number} n - The number of players in the game.
 * @return {Array<number>} - An array of integers representing the order of players being removed from the ring.
 */
function findOrder(n) {
    class Node {
        constructor(value) {
            this.value = value;
            this.next = null;
        }
    }

    class CircularLinkedList {
        constructor() {
            this.head = null;
            this.tail = null;
            this.size = 0;
        }

        append(value) {
            const newNode = new Node(value);
            if (!this.head) {
                this.head = newNode;
                this.tail = newNode;
                newNode.next = newNode;
            } else {
                this.tail.next = newNode;
                newNode.next = this.head;
                this.tail = newNode;
            }
            this.size++;
        }

        remove(node) {
            if (this.size === 1) {
                this.head = null;
                this.tail = null;
            } else {
                let current = this.head;
                while (current.next !== node) {
                    current = current.next;
                }
                current.next = node.next;
                if (node === this.head) {
                    this.head = node.next;
                }
                if (node === this.tail) {
                    this.tail = current;
                }
            }
            this.size--;
        }
    }

    class PrimeGame {
        constructor(n) {
            this.players = new CircularLinkedList();
            for (let i = 1; i <= n; i++) {
                this.players.append(i);
            }
        }

        *generatePrimes() {
            const isPrime = (num) => {
                if (num <= 1) return false;
                if (num <= 3) return true;
                if (num % 2 === 0 || num % 3 === 0) return false;
                for (let i = 5; i * i <= num; i += 6) {
                    if (num % i === 0 || num % (i + 2) === 0) return false;
                }
                return true;
            };

            let num = 2;
            while (true) {
                if (isPrime(num)) {
                    yield num;
                }
                num++;
            }
        }

        findOrder() {
            const order = [];
            let current = this.players.head;
            const primeGenerator = this.generatePrimes();

            while (this.players.size > 0) {
                const prime = primeGenerator.next().value;
                for (let i = 1; i < prime; i++) {
                    current = current.next;
                }
                order.push(current.value);
                const next = current.next;
                this.players.remove(current);
                current = next;
            }

            return order;
        }
    }

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
