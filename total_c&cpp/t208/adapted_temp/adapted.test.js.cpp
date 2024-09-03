#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../adapted.cpp"
// Test Case 1: Test insertion and extraction of the minimum element
TEST_CASE("Insertion and extraction of minimum element", "[PriorityQueue]") {
    PriorityQueue pq;

    SECTION("Inserting elements into the priority queue") {
        pq.insert(5);
        pq.insert(2);
        pq.insert(8);
        pq.insert(1);
        pq.insert(3);

        REQUIRE(pq.size() == 5);
        REQUIRE(pq.peekMin() == 1);
    }

    SECTION("Extracting the minimum element") {
        pq.insert(5);
        pq.insert(2);
        pq.insert(8);
        pq.insert(1);
        pq.insert(3);

        REQUIRE(pq.extractMin() == 1);
        REQUIRE(pq.extractMin() == 2);
        REQUIRE(pq.extractMin() == 3);
        REQUIRE(pq.extractMin() == 5);
        REQUIRE(pq.extractMin() == 8);
        REQUIRE(pq.isEmpty() == true);
    }
}

// Test Case 2: Test peekMin operation
TEST_CASE("Peek minimum element", "[PriorityQueue]") {
    PriorityQueue pq;

    SECTION("Peeking at the minimum element without extraction") {
        pq.insert(10);
        pq.insert(4);
        pq.insert(15);

        REQUIRE(pq.peekMin() == 4);
        REQUIRE(pq.size() == 3); // Size should remain the same
        REQUIRE(pq.peekMin() == 4); // Peek should not remove the element
    }
}

// Test Case 3: Test edge case of extracting from an empty queue
TEST_CASE("Extract from empty queue", "[PriorityQueue]") {
    PriorityQueue pq;

    SECTION("Attempting to extract from an empty queue should throw an exception") {
        REQUIRE_THROWS_AS(pq.extractMin(), std::runtime_error);
    }
}

// Test Case 4: Test isEmpty function
TEST_CASE("Check if the priority queue is empty", "[PriorityQueue]") {
    PriorityQueue pq;

    SECTION("Newly created queue should be empty") {
        REQUIRE(pq.isEmpty() == true);
    }

    SECTION("Queue should not be empty after insertion") {
        pq.insert(7);
        REQUIRE(pq.isEmpty() == false);
    }

    SECTION("Queue should be empty after extracting all elements") {
        pq.insert(7);
        pq.extractMin();
        REQUIRE(pq.isEmpty() == true);
    }
}

// Test Case 5: Test multiple insertions and order of extraction
TEST_CASE("Multiple insertions and extraction order", "[PriorityQueue]") {
    PriorityQueue pq;

    SECTION("Inserting multiple elements and checking extraction order") {
        pq.insert(9);
        pq.insert(4);
        pq.insert(6);
        pq.insert(1);
        pq.insert(8);

        std::vector<int> extractedElements;
        while (!pq.isEmpty()) {
            extractedElements.push_back(pq.extractMin());
        }

        std::vector<int> expectedOrder = {1, 4, 6, 8, 9};
        REQUIRE(extractedElements == expectedOrder);
    }
}