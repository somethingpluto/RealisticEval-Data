TEST_CASE("saveAsJSON", "[json]") {
    const std::string mockFilePath = "test.json";

    // Clean up after each test
    auto cleanup = [&]() {
        if (std::filesystem::exists(mockFilePath)) {
            std::filesystem::remove(mockFilePath);
        }
    };

    // Run cleanup after each test case
    SECTION("Cleanup") { cleanup(); }

    SECTION("should save valid object to JSON file") {
        nlohmann::json data = {{"name", "Alice"}, {"age", 25}};
        saveAsJSON(data, mockFilePath);
        std::ifstream savedFile(mockFilePath);
        std::string savedData((std::istreambuf_iterator<char>(savedFile)), std::istreambuf_iterator<char>());
        REQUIRE(savedData == data.dump(2));
        cleanup();
    }

    SECTION("should handle empty object") {
        nlohmann::json data = {};
        saveAsJSON(data, mockFilePath);
        std::ifstream savedFile(mockFilePath);
        std::string savedData((std::istreambuf_iterator<char>(savedFile)), std::istreambuf_iterator<char>());
        REQUIRE(savedData == data.dump(2));
        cleanup();
    }

    SECTION("should save nested object to JSON file") {
        nlohmann::json data = {{"user", {{"name", "Bob"}, {"age", 30}}}, {"active", true}};
        saveAsJSON(data, mockFilePath);
        std::ifstream savedFile(mockFilePath);
        std::string savedData((std::istreambuf_iterator<char>(savedFile)), std::istreambuf_iterator<char>());
        REQUIRE(savedData == data.dump(2));
        cleanup();
    }

    SECTION("should save array of objects to JSON file") {
        nlohmann::json data = {
            {{"product", {{"id", 1}, {"name", "Laptop"}, {"price", 999.99}}}, {"inStock", true}},
            {{"product", {{"id", 2}, {"name", "Phone"}, {"price", 499.99}}}, {"inStock", false}}
        };
        saveAsJSON(data, mockFilePath);
        std::ifstream savedFile(mockFilePath);
        std::string savedData((std::istreambuf_iterator<char>(savedFile)), std::istreambuf_iterator<char>());
        REQUIRE(savedData == data.dump(2));
        cleanup();
    }

    SECTION("should save object with mixed data types to JSON file") {
        nlohmann::json data = {{"title", "Shopping List"}, {"items", {"Milk", "Eggs", "Bread"}}, {"total", 3.50}, {"completed", false}};
        saveAsJSON(data, mockFilePath);
        std::ifstream savedFile(mockFilePath);
        std::string savedData((std::istreambuf_iterator<char>(savedFile)), std::istreambuf_iterator<char>());
        REQUIRE(savedData == data.dump(2));
        cleanup();
    }

    SECTION("should save deeply nested object to JSON file") {
        nlohmann::json data = {
            {"company", {
                {"name", "TechCorp"},
                {"employees", {
                    {{"id", 1}, {"name", "Alice"}, {"role", "Developer"}, {"contact", {{"email", "alice@techcorp.com"}, {"phone", "123-456-7890"}}}},
                    {{"id", 2}, {"name", "Bob"}, {"role", "Designer"}, {"contact", {{"email", "bob@techcorp.com"}, {"phone", "098-765-4321"}}}}
                }}
            }},
            {"established", 2010}
        };
        saveAsJSON(data, mockFilePath);
        std::ifstream savedFile(mockFilePath);
        std::string savedData((std::istreambuf_iterator<char>(savedFile)), std::istreambuf_iterator<char>());
        REQUIRE(savedData == data.dump(2));
        cleanup();
    }
}