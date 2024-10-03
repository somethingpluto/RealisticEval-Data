TEST_CASE("Priority Queue - Test Cases") {
    PriorityQueue pq;

    SECTION("Insert and access maximum element") {
        pq.push(10);
        pq.push(20);
        pq.push(5);
        pq.push(30);
        pq.push(15);

        REQUIRE(pq.top() == 30); // Ensure the max element is 30
    }

    SECTION("Remove maximum element") {
        pq.push(10);
        pq.push(20);
        pq.push(5);
        pq.push(30);

        pq.pop(); // Remove 30
        REQUIRE(pq.top() == 20); // Now the max should be 20
        pq.pop(); // Remove 20
        REQUIRE(pq.top() == 10); // Now the max should be 10
    }

    SECTION("Check empty queue") {
        REQUIRE(pq.isEmpty() == true); // Initially empty
        pq.push(10);
        REQUIRE(pq.isEmpty() == false); // Now not empty
        pq.pop();
        REQUIRE(pq.isEmpty() == true); // Back to empty
    }

    SECTION("Pop from empty queue") {
        REQUIRE_THROWS_AS(pq.pop(), std::runtime_error); // Should throw an error
    }

    SECTION("Access top of empty queue") {
        REQUIRE_THROWS_AS(pq.top(), std::runtime_error); // Should throw an error
    }

    SECTION("Maintain max-heap property") {
        pq.push(3);
        pq.push(1);
        pq.push(4);
        pq.push(2);

        REQUIRE(pq.top() == 4); // Ensure max is 4

        pq.pop(); // Remove 4
        REQUIRE(pq.top() == 3); // Now max is 3

        pq.push(5); // Add 5
        REQUIRE(pq.top() == 5); // Ensure max is now 5
    }
}