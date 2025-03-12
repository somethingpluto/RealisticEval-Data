// ... (previous code for context)

class PrimeGame {
  // ... (existing class members)

  private isPrime(num: number): boolean {
    if (num <= 1) return false;
    for (let i = 2; i * i <= num; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  private getNextPrime(current: number): number {
    let nextPrime = current + 1;
    while (!this.isPrime(nextPrime)) {
      nextPrime++;
    }
    return nextPrime;
  }

  private findPrimeOrder(): number[] {
    const primeOrder: number[] = [];
    let currentPrime = 2;
    while (primeOrder.length < this.players.length) {
      primeOrder.push(currentPrime);
      currentPrime = this.getNextPrime(currentPrime);
    }
    return primeOrder;
  }

  public findOrder(): number[] {
    const primeOrder = this.findPrimeOrder();
    const removalOrder: number[] = [];
    let index = 0;
    while (primeOrder.length > 0) {
      const prime = primeOrder.shift()!;
      const playerIndex = (this.currentPlayer + prime - 1) % this.players.length;
      removalOrder.push(this.players[playerIndex]);
      this.players.splice(playerIndex, 1);
      this.currentPlayer = (this.currentPlayer + 1) % this.players.length;
    }
    return removalOrder;
  }
}

// ... (rest of the code)
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
