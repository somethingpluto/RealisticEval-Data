TEST_CASE("Size in Bytes", "[size]") {
    int a = 42;
    REQUIRE(size_in_bytes(&a) == sizeof(int));

    double b = 3.14;
    REQUIRE(size_in_bytes(&b) == sizeof(double));

    std::string c = "Hello";
    REQUIRE(size_in_bytes(c.c_str()) == sizeof(char) * c.length());

    // Add more tests as needed
}