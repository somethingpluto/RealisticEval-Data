TEST_CASE("Test BloomFilter functionality", "[BloomFilter]") {
    SECTION("Test add and check presence") {
        BloomFilter bf(1000, 5);
        std::string test_item = "hello world";
        bf.add(test_item);
        REQUIRE(bf.contains(test_item));
    }

    SECTION("Test check absence") {
        BloomFilter bf(1000, 5);
        REQUIRE_FALSE(bf.contains("random item"));
    }

    SECTION("Test false positives") {
        BloomFilter bf(1000, 5);
        std::vector<std::string> items_to_add = {"item1", "item2", "item3"};
        for (const auto& item : items_to_add) {
            bf.add(item);
        }
        REQUIRE_FALSE(bf.contains("item4"));
    }

    SECTION("Test collision handling") {
        BloomFilter bf(1000, 5);
        bf.add("item123");
        bf.add("item124");
        REQUIRE(bf.contains("item123"));
        REQUIRE(bf.contains("item124"));
    }

    SECTION("Test empty Bloom Filter") {
        BloomFilter bf(1000, 5);
        REQUIRE_FALSE(bf.contains("anything"));
    }
}