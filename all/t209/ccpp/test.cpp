TEST_CASE("LinkedList operations", "[LinkedList]") {

    SECTION("Insertion at the head") {
        LinkedList list;
        list.insertAtHead(10);
        list.insertAtHead(20);
        list.insertAtHead(30);

        std::ostringstream output;
        list.printList(); // Expected: 30 -> 20 -> 10 -> nullptr
        REQUIRE(list.search(10) == true);
        REQUIRE(list.search(20) == true);
        REQUIRE(list.search(30) == true);
        REQUIRE(list.search(40) == false);
    }

    SECTION("Insertion at the tail") {
        LinkedList list;
        list.insertAtTail(1);
        list.insertAtTail(2);
        list.insertAtTail(3);

        std::ostringstream output;
        list.printList(); // Expected: 1 -> 2 -> 3 -> nullptr
        REQUIRE(list.search(1) == true);
        REQUIRE(list.search(2) == true);
        REQUIRE(list.search(3) == true);
        REQUIRE(list.search(4) == false);
    }

    SECTION("Deletion of elements") {
        LinkedList list;
        list.insertAtHead(5);
        list.insertAtHead(10);
        list.insertAtHead(15);

        list.deleteValue(10);
        std::ostringstream output;
        list.printList(); // Expected: 15 -> 5 -> nullptr
        REQUIRE(list.search(10) == false);
        REQUIRE(list.search(15) == true);
        REQUIRE(list.search(5) == true);

        list.deleteValue(15);
        list.printList(); // Expected: 5 -> nullptr
        REQUIRE(list.search(15) == false);
        REQUIRE(list.search(5) == true);

        list.deleteValue(5);
        list.printList(); // Expected: nullptr
        REQUIRE(list.search(5) == false);
    }

    SECTION("Search functionality") {
        LinkedList list;
        list.insertAtTail(100);
        list.insertAtTail(200);
        list.insertAtTail(300);

        REQUIRE(list.search(100) == true);
        REQUIRE(list.search(200) == true);
        REQUIRE(list.search(300) == true);
        REQUIRE(list.search(400) == false);
    }

    SECTION("Edge case: Empty list") {
        LinkedList list;

        REQUIRE(list.search(1) == false);  // Searching in an empty list
        list.deleteValue(1);               // Deleting from an empty list should not crash
        std::ostringstream output;
        list.printList();                  // Expected: nullptr (still empty)
    }
}