TEST_CASE("PriorityQueue operations", "[priority_queue]") {
    PriorityQueue pq;

    SECTION("New priority queue is empty") {
        REQUIRE(pq.isEmpty() == true);
        REQUIRE(pq.size() == 0);
    }

    SECTION("Single element push and top") {
        pq.push(10);
        REQUIRE(pq.isEmpty() == false);
        REQUIRE(pq.top() == 10);
        REQUIRE(pq.size() == 1);
    }

    SECTION("Multiple element push and correct ordering") {
        pq.push(5);
        pq.push(10);
        pq.push(3);
        REQUIRE(pq.top() == 10);
        pq.pop();
        REQUIRE(pq.top() == 5);
    }

    SECTION("Pop from priority queue until empty") {
        pq.push(5);
        pq.push(10);
        pq.push(3);
        pq.pop();  // Removes 10
        pq.pop();  // Removes 5
        pq.pop();  // Removes 3
        REQUIRE(pq.isEmpty() == true);
    }

    SECTION("Throw exception when popping from empty queue") {
        REQUIRE_THROWS_AS(pq.pop(), std::runtime_error);
    }

    SECTION("Throw exception when accessing top of empty queue") {
        REQUIRE_THROWS_AS(pq.top(), std::.runtime_error);
    }
}