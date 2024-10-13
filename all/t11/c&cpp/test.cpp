TEST_CASE("Test Trie operations", "[Trie]") {
    Trie trie;
    trie.insert("apple");
    trie.insert("app");
    trie.insert("apricot");
    trie.insert("banana");
    trie.insert("carrot");
    trie.insert("car");
    trie.insert("care");
    trie.insert("");
    trie.insert("Hello");
    trie.insert("hello");

    SECTION("Basic search") {
        REQUIRE(trie.search("apple"));
        REQUIRE(trie.search("app"));
        REQUIRE(trie.search("apricot"));
    }

    SECTION("Unsuccessful search") {
        REQUIRE_FALSE(trie.search("bandana"));
    }

    SECTION("Prefix search") {
        REQUIRE(trie.starts_with("car"));
        REQUIRE(trie.starts_with("care"));
        REQUIRE_FALSE(trie.starts_with("cat"));
    }

    SECTION("Empty string") {
        REQUIRE(trie.search(""));
        REQUIRE(trie.starts_with(""));
    }

    SECTION("Case sensitivity") {
        REQUIRE(trie.search("Hello"));
        REQUIRE(trie.search("hello"));
        REQUIRE_FALSE(trie.search("HELLO"));
    }
}