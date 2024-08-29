#include <iostream>
#include <vector>

using namespace std;

/**
 * @brief A class that simulates a game where players are removed based on the order of prime numbers.
 */
class PrimeGame {
public:
    /**
     * @brief Constructs a PrimeGame object with a specified number of players.
     * 
     * @param numPlayers The number of players in the game.
     */
    PrimeGame(int numPlayers) {
        if (numPlayers < 2) {
            throw invalid_argument("Number of players must be at least 2.");
        }
        this->numPlayers = numPlayers;
        this->head = createCircularLinkedList(numPlayers);
    }

    /**
     * @brief Destructor to clean up the circular linked list.
     */
    ~PrimeGame() {
        // Clean up the linked list
        Node* current = head;
        for (int i = 0; i < numPlayers; ++i) {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
    }

    /**
     * @brief Finds the order of players going out of the ring based on prime number steps.
     *
     * @return A vector of integers representing the order of players going out of the ring.
     */
    vector<int> findOrder() {
        vector<int> primes = generatePrimes(numPlayers);
        vector<int> order;

        Node* current = head;
        int remainingPlayers = numPlayers;

        while (remainingPlayers > 1 && !primes.empty()) {
            int step = primes.front() - 1;
            primes.erase(primes.begin());

            for (int i = 0; i < step; ++i) {
                current = current->next;
            }

            Node* toRemove = current->next;
            order.push_back(toRemove->data);
            current->next = toRemove->next;
            delete toRemove;

            --remainingPlayers;
        }

        order.push_back(current->data); // The last remaining player

        return order;
    }

private:
    struct Node {
        int data;
        Node* next;

        Node(int d) : data(d), next(nullptr) {}
    };

    int numPlayers;
    Node* head;

    /**
     * @brief Creates a circular linked list with n nodes.
     *
     * @param n The number of nodes to create in the circular linked list.
     * @return A pointer to the head of the circular linked list.
     */
    Node* createCircularLinkedList(int n) {
        Node* head = new Node(1);
        Node* current = head;

        for (int i = 2; i <= n; ++i) {
            current->next = new Node(i);
            current = current->next;
        }

        current->next = head; // Make the linked list circular
        return head;
    }

    /**
     * @brief Generates all prime numbers up to a given limit using the Sieve of Eratosthenes.
     *
     * @param limit The upper bound (inclusive) for generating prime numbers.
     * @return A vector of integers containing all prime numbers up to the limit.
     */
    vector<int> generatePrimes(int limit) {
        if (limit < 2) {
            return {}; // No primes less than 2
        }

        vector<bool> isPrime(limit + 1, true);
        vector<int> primes;

        for (int i = 2; i * i <= limit; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        for (int i = 2; i <= limit; ++i) {
            if (isPrime[i]) {
                primes.push_back(i);
            }
        }

        return primes;
    }
};

/**
 * @brief Function to start the game and return the order of players being removed.
 *
 * This function creates an instance of the PrimeGame class, which encapsulates the logic
 * for simulating the game. It then calls the findOrder method on the PrimeGame object
 * to determine and return the order in which players are removed based on the sequence of prime numbers.
 *
 * @param n The number of players in the game.
 * @return A vector of integers representing the order of players being removed from the ring.
 */
vector<int> findOrder(int n) {
    // Create an instance of PrimeGame with n players.
    PrimeGame game(n);

    // Call the findOrder method of the PrimeGame instance to get the order of removed players.
    return game.findOrder();
}