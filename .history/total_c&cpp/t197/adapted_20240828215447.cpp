#include <iostream>
#include <vector>
#include <stdexcept>
#include <list>

/**
 * @brief Simulate a game based on the order of prime numbers, using a circular linked list to represent the cyclic structure of players, and remove players one by one
 */
class PrimeGame {
public:
    /**
     * @brief Constructor that initializes the game with a given number of players.
     *
     * @param numPlayers The number of players participating in the game.
     */
    PrimeGame(int numPlayers) {
        if (numPlayers < 2) {
            throw std::invalid_argument("Number of players must be at least 2.");
        }

        for (int i = 1; i <= numPlayers; ++i) {
            players.push_back(i);
        }
        current = players.begin();
    }

    /**
     * @brief Starts the game and removes players based on the sequence of prime numbers.
     *
     * @return The player number who wins the game (the last remaining player).
     */
    int startGame() {
        int primeIndex = 0;

        while (players.size() > 1) {
            int steps = nextPrime(primeIndex) - 1;  // Prime numbers start with the first prime (2)
            for (int i = 0; i < steps; ++i) {
                ++current;
                if (current == players.end()) {
                    current = players.begin();
                }
            }
            current = players.erase(current);
            if (current == players.end()) {
                current = players.begin();
            }
            ++primeIndex;
        }
        return players.front();
    }

private:
    std::list<int> players;         // Circular linked list of players
    std::list<int>::iterator current; // Iterator to the current player

    /**
     * @brief Finds the next prime number based on its index in the sequence.
     *
     * @param index The index of the prime number to find.
     * @return The prime number at the given index.
     */
    int nextPrime(int index) {
        static std::vector<int> primes;
        if (index < primes.size()) {
            return primes[index];
        }

        int candidate = (primes.empty()) ? 2 : primes.back() + 1;
        while (primes.size() <= index) {
            if (isPrime(candidate)) {
                primes.push_back(candidate);
            }
            ++candidate;
        }
        return primes[index];
    }

    /**
     * @brief Determines whether a given number is prime.
     *
     * @param n The number to check for primality.
     * @return true if the number is prime, false otherwise.
     */
    bool isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;

        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
};