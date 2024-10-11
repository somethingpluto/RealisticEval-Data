TEST_CASE("UniqueDeque Tests", "[UniqueDeque]") {
    UniqueDeque uqDeq;

    SECTION("Adding Items") {
        REQUIRE(uqDeq.add(1));
        REQUIRE_FALSE(uqDeq.add(1)); // Duplicate should not be added again
        REQUIRE(uqDeq.contains(1));
        REQUIRE(uqDeq.size() == 1);

        uqDeq.add(2);
        REQUIRE(uqDeq.contains(2));
        REQUIRE(uqDeq.size() == 2);
    }

    SECTION("Deleting Items") {
        uqDeq.add(3);
        uqDeq.add(4);

        REQUIRE(uqDeq.deleteItem(3));
        REQUIRE_FALSE(uqDeq.contains(3));
        REQUIRE(uqDeq.size() == 1);

        REQUIRE_FALSE(uqDeq.deleteItem(5)); // Item not in deque
        REQUIRE(uqDeq.size() == 1);
    }

    SECTION("Iterating Over Items") {
        uqDeq.add(6);
        uqDeq.add(7);

        int count = 0;
        for (auto it = uqDeq.begin(); it != uqDeq.end(); ++it) {
            ++count;
        }
        REQUIRE(count == 2);
    }
}