TEST_CASE("getPrice", "[getPrice]") {
    SECTION("should return a number within the default range for a given recipe ID") {
        double price = getPrice("recipe123");
        REQUIRE(price >= 10);
        REQUIRE(price <= 30);
    }

    SECTION("should return the same price for the same recipe ID") {
        double price1 = getPrice("recipe123");
        double price2 = getPrice("recipe123");
        REQUIRE(price1 == price2);
    }

    SECTION("should return different prices for different recipe IDs") {
        double price1 = getPrice("recipe123");
        double price2 = getPrice("recipe456");
        REQUIRE(price1 != price2);
    }

    SECTION("should return a price within a custom range") {
        double minVal = 20;
        double maxVal = 50;
        double price = getPrice("recipe789", minVal, maxVal);
        REQUIRE(price >= minVal);
        REQUIRE(price <= maxVal);
    }

    SECTION("should handle very long recipe IDs without error") {
        std::string longRecipeId = "recipe" + std::string(1000, 'A');
        double price = getPrice(longRecipeId);
        REQUIRE(price >= 10);
        REQUIRE(price <= 30);
    }
}