// Test cases for the Queue class
TEST_CASE("Queue Operations", "[Queue]") {
    Queue queue;

    SECTION("Queue should be empty initially") {
        REQUIRE(queue.isEmpty() == true);
    }

    SECTION("Enqueue elements") {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);

        REQUIRE(queue.isEmpty() == false);
        REQUIRE(queue.front() == 10); // Front element should be 10
    }

    SECTION("Dequeue elements") {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);

        int value = queue.dequeue();
        REQUIRE(value == 10); // First dequeued element should be 10
        REQUIRE(queue.front() == 20); // Now front should be 20
    }

    SECTION("Dequeue from an empty queue") {
        int value = queue.dequeue();
        REQUIRE(value == -1); // Should indicate that the queue is empty
    }

    SECTION("Front element of an empty queue") {
        int frontValue = queue.front();
        REQUIRE(frontValue == -1); // Should indicate that the queue is empty
    }

    SECTION("Queue should become empty after dequeuing all elements") {
        queue.enqueue(10);
        queue.enqueue(20);

        queue.dequeue(); // Remove 10
        queue.dequeue(); // Remove 20

        REQUIRE(queue.isEmpty() == true); // Queue should be empty
    }
}