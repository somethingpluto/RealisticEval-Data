TEST_CASE("convertThreadToJSONFile Function Tests") {
    SECTION("should return a Blob object for a basic thread object") {
        json thread1 = {{"id", 1}, {"title", "First Thread"}, {"content", "This is the first thread."}};
        Blob blob1 = encodeStringAsBlob(convertThreadToJSONFile(thread1));
        REQUIRE(blob1.type == "application/json");
        REQUIRE(blob1.size > 0); // Ensure it has some data
    }

    SECTION("should return a Blob object for an empty thread object") {
        json thread2 = {};
        Blob blob2 = encodeStringAsBlob(convertThreadToJSONFile(thread2));
        REQUIRE(blob2.type == "application/json");
        REQUIRE(blob2.size == 2); // "{}" has a size of 2 bytes
    }

    SECTION("should return a Blob object for a thread object with nested objects") {
        json thread3 = {{"id", 2}, {"title", "Second Thread"}, {"comments", json::array({{{"user", "Alice"}, {"comment", "Great post!"}}})}};
        Blob blob3 = encodeStringAsBlob(convertThreadToJSONFile(thread3));
        REQUIRE(blob3.type == "application/json");
        REQUIRE(blob3.size > 0); // Ensure it has some data
    }

    SECTION("should return a Blob object for a thread object with special characters") {
        json thread4 = {{"id", 3}, {"title", "Thread & Special <Characters>"}, {"content", "This is a thread with special characters: <, >, &, \". "}};
        Blob blob4 = encodeStringAsBlob(convertThreadToJSONFile(thread4));
        REQUIRE(blob4.type == "application/json");
        REQUIRE(blob4.size > 0); // Ensure it has some data
    }

    SECTION("should return a Blob object for a thread object with arrays") {
        json thread5 = {{"id", 4}, {"title", "Thread with Array"}, {"tags", json::array({"JavaScript", "JSON", "Blob"})}};
        Blob blob5 = encodeStringAsBlob(convertThreadToJSONFile(thread5));
        REQUIRE(blob5.type == "application/json");
        REQUIRE(blob5.size > 0); // Ensure it has some data
    }
}