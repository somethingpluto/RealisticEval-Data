class PrimeGame {
    private numPlayers: number;
    private head: Node | null;

    private class Node {
        data: number;
        next: Node | null;

        constructor(data: number) {
            this.data = data;
            this.next = null;
        }
    }

    constructor(numPlayers: number) {
        if (numPlayers < 2) {
            throw new Error("Number of players must be at least 2.");
        }
        this.numPlayers = numPlayers;
        this.head = this.createCircularLinkedList(numPlayers);
    }

    private createCircularLinkedList(n: number): Node {
        const head = new this.Node(1);
        let current = head;

        for (let i = 2; i <= n; i++) {
            current.next = new this.Node(i);
            current = current.next;
        }

        current.next = head; // Make the linked list circular
        return head;
    }

    public findOrder(): number[] {
        const primes = this.generatePrimes(this.numPlayers);
        const order: number[] = [];

        let current: Node | null = this.head;
        let remainingPlayers = this.numPlayers;

        while (remainingPlayers > 1 && primes.length > 0) {
            const step = primes.shift()! - 1; // Get the next prime number and decrement
            for (let i = 0; i < step; i++) {
                current = current?.next ?? null;
            }

            if (current && current.next) {
                const toRemove = current.next;
                order.push(toRemove.data);
                current.next = toRemove.next;
                remainingPlayers--;
            }
        }

        if (current) {
            order.push(current.data); // The last remaining player
        }

        return order;
    }

    private generatePrimes(limit: number): number[] {
        if (limit < 2) {
            return []; // No primes less than 2
        }

        const isPrime: boolean[] = Array(limit + 1).fill(true);
        const primes: number[] = [];

        for (let i = 2; i * i <= limit; i++) {
            if (isPrime[i]) {
                for (let j = i * i; j <= limit; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        for (let i = 2; i <= limit; i++) {
            if (isPrime[i]) {
                primes.push(i);
            }
        }

        return primes;
    }
}