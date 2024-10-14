TEST_CASE("Queue Class", "[queue]") {
    Queue queue;

    SECTION("should initialize an empty queue") {
        REQUIRE(queue.isEmpty() == true);
    }

    SECTION("should enqueue elements to the queue") {
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        REQUIRE(queue.printQueue() == "1 2 3");
        REQUIRE(queue.isEmpty() == false);
    }

    SECTION("should dequeue elements from the queue") {
        queue.enqueue(1);
        queue.enqueue(2);
        std::string dequeuedElement = queue.dequeue();
        REQUIRE(dequeuedElement == "1");
    }

    SECTION("should return the front element without removing it") {
        queue.enqueue(10);
        queue.enqueue(20);
        std::string frontElement = queue.front();
        REQUIRE(frontElement == "10");
    }

    SECTION("should check if the queue is empty") {
        REQUIRE(queue.isEmpty() == true);
        queue.enqueue(5);
        REQUIRE(queue.isEmpty() == false);
        queue.dequeue();
        REQUIRE(queue.isEmpty() == true);
    }
}