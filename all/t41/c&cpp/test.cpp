#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include "BloomFilter.h" // Assuming BloomFilter is defined in this header

TEST_CASE("BloomFilter test cases") {

    BloomFilter bf(1000, 5);

    SECTION("test_add_and_check_presence") {
        std::string test_item = "hello world";
        bf.add(test_item);
        REQUIRE(bf.contains(test_item) == true);
    }

    SECTION("test_check_absence") {
        REQUIRE(bf.contains("random item") == false);
    }

    SECTION("test_false_positives") {
        std::vector<std::string> items_to_add = {"item1", "item2", "item3"};
        for (const auto& item : items_to_add) {
            bf.add(item);
        }
        REQUIRE(bf.contains("item4") == false);
    }

    SECTION("test_collision_handling") {
        bf.add("item123");
        bf.add("item124");
        REQUIRE(bf.contains("item123") == true);
        REQUIRE(bf.contains("item124") == true);
    }

    SECTION("test_empty_bloom_filter") {
        REQUIRE(bf.contains("anything") == false);
    }
}