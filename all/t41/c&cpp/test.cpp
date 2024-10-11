TEST_CASE("BloomFilter Test", "[bloomfilter]") {
    MockBloomFilter bloomFilter;

    SECTION("Adding an item should not throw an exception") {
        REQUIRE_NOTHROW(bloomFilter.add("testItem"));
    }

    SECTION("Checking for the presence of an added item should return true") {
        bloomFilter.add("testItem");
        CHECK(bloomFilter.contains("testItem")); // Assuming contains() is a member function that checks if an item is present
    }

    SECTION("Checking for the absence of an item should return false") {
        CHECK(!bloomFilter.contains("nonExistentItem")); // Assuming contains() is a member function that checks if an item is present
    }
}