TEST_CASE("TestConvertToCommaSeparated", "[convert_to_comma_separated]") {
    SECTION("test_basic_separators") {
        CHECK(convert_to_comma_separated("apple;banana*orange/mango") == "apple,banana,orange,mango");
        INFO("Failed to convert basic separators.");
    }

    SECTION("test_mixed_separators") {
        CHECK(convert_to_comma_separated("grapes;lemon/melon*kiwi;litchi") == "grapes,lemon,melon,kiwi,litchi");
        INFO("Failed to convert mixed separators in a string.");
    }

    SECTION("test_mixed_separators2") {
        CHECK(convert_to_comma_separated("grapes/lemon/melon*kiwi*litchi") == "grapes,lemon,melon,kiwi,litchi");
        INFO("Failed to convert mixed separators in a string.");
    }

    SECTION("test_no_separators") {
        CHECK(convert_to_comma_separated("watermelon") == "watermelon");
        INFO("Failed when no separators are present.");
    }
}