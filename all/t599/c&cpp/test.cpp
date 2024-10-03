TEST_CASE("MaxHeap Operations", "[MaxHeap]") {
    MaxHeap maxHeap;

    SECTION("Initial state of the heap") {
        REQUIRE(maxHeap.isEmpty() == true);
        REQUIRE(maxHeap.size() == 0);
    }

    SECTION("Insert elements into the heap") {
        maxHeap.insert(10);
        maxHeap.insert(20);
        maxHeap.insert(5);

        REQUIRE(maxHeap.isEmpty() == false);
        REQUIRE(maxHeap.size() == 3);
        REQUIRE(maxHeap.getMax() == 20); // The maximum should be 20
    }

    SECTION("Extract maximum element from the heap") {
        maxHeap.insert(10);
        maxHeap.insert(30);
        maxHeap.insert(20);

        int maxElement = maxHeap.extractMax();
        REQUIRE(maxElement == 30); // The maximum extracted should be 30
        REQUIRE(maxHeap.getMax() == 20); // The next maximum should be 20
        REQUIRE(maxHeap.size() == 2); // Size should be 2 after extraction
    }

    SECTION("Heap should maintain max heap property after multiple operations") {
        maxHeap.insert(15);
        maxHeap.insert(10);
        maxHeap.insert(30);
        maxHeap.insert(20);
        maxHeap.insert(25);

        // Current max should be 30
        REQUIRE(maxHeap.getMax() == 30);

        maxHeap.extractMax(); // Remove 30
        // After removal, the new max should be 25
        REQUIRE(maxHeap.getMax() == 25);

        maxHeap.extractMax(); // Remove 25
        // After removal, the new max should be 20
        REQUIRE(maxHeap.getMax() == 20);

        // The size of the heap should be 3 now
        REQUIRE(maxHeap.size() == 3);
    }
}